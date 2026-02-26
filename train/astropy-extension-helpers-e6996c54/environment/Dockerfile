FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/astropy/extension-helpers.git /data/project \
    && cd /data/project \
    && git checkout e6996c540c5bf23e89b45f170e89bd8c9f22a86e
