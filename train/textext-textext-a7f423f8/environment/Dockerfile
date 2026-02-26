FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/textext/textext.git /data/project \
    && cd /data/project \
    && git checkout a7f423f8a44285f0059299ed3f1286a46ef17218
