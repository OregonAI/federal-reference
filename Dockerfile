# MCP server for the federal-reference corpus (HTTP transport).
#
#   docker build -t federal-reference-mcp .
#   docker run -p 8000:8000 federal-reference-mcp
#
# The corpus is baked in at build time; rebuild the image to pick up new commits. Mounting
# it instead was tried on executive-regulatory-frameworks and reverted the same day — it
# never shrank the image, and it made the FTS index shared mutable state between the
# deployer and the live container. See platform-deploy's README before repeating it.
#
# SNAPSHOTS ARE THE BULK OF THIS REPO AND THEY ARE NOT NEEDED AT RUNTIME. 13 MB of raw PDFs
# and XML under _meta/snapshots/ exist so provenance and src/check_extraction.py can verify
# the documents against their sources — both are CI concerns. The server reads instruments/
# and _meta/graph.json. .dockerignore drops them; see it for why .git is NOT dropped.
#
# BUILD FROM A SHALLOW CLONE, not your working tree. `.git` cannot be excluded — it is a
# RUNTIME dependency, because the FTS cache key is `git rev-parse HEAD` plus a hash of
# `git status --porcelain`, and corpus_overview() shells out to `git log -1`. Without it
# repo_state() collapses to a constant and content changes are never picked up, silently.
#
#   git clone --depth 1 --branch main https://github.com/OregonAI/federal-reference build/
#   docker build -t federal-reference-mcp build/
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /repo
# Deps BEFORE content, so a content-only change does not re-run pip. The template shipped
# these the other way round and every edited document forced a full reinstall.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Pre-build the FTS index so the first request is instant.
#
# 43 documents, so this is fast. The step earns its place for the OTHER reason: it fails the
# BUILD if content is missing, rather than shipping an image that starts fine, reports
# healthy, and answers nothing.
#
# It also proves src/citation_schemes.py IMPORTS. `plugins.citation_module` is loaded by
# CorpusFramework and nothing else, so a broken module passes every validator in CI and then
# refuses to start the server. That exact failure is why the file exists at all -- see its
# docstring. Here it is a build failure instead of a 3am one.
RUN python3 -c "\
from corpus_toolkit import config as config_mod; \
from corpus_toolkit.mcp.framework import CorpusFramework; \
CorpusFramework(config_mod.load('_meta/corpus.yml')).ensure_index()" \
 && python3 -c "import corpus_toolkit.mcp.server" \
 && corpus-mcp-serve --help >/dev/null
EXPOSE 8000

# --path and --public-hostname both matter behind the tunnel and are easy to omit:
#   * A Cloudflare Tunnel matches on path but does NOT strip it. Routing /federal-reference
#     here forwards the whole path, so the server must mount at that same prefix or every
#     request 404s with nothing in any log explaining why.
#   * Without --public-hostname the SDK's DNS-rebinding guard rejects the forwarded Host
#     header with 421 Invalid Host header.
# Override either at `docker run` for a different hostname or a dedicated-host deployment
# (in which case pass --path /mcp).
CMD ["corpus-mcp-serve", "--config", "_meta/corpus.yml", "--http", \
     "--host", "0.0.0.0", "--port", "8000", \
     "--path", "/federal-reference/mcp", \
     "--public-hostname", "oregonai.morficflux.com"]
