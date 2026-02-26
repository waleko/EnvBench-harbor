FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/giskard-ai/giskard.git /data/project \
    && cd /data/project \
    && git checkout e724a9f5d7d90e88c1575cdb06ccd573548f033b
