FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/spec-first/connexion.git /data/project \
    && cd /data/project \
    && git checkout a930303faa9e10603cdd820c497303b2e52d8253
