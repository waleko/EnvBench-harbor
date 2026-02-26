FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/Modalities/modalities.git /data/project \
    && cd /data/project \
    && git checkout 4aa2e88efe13c3eaab4c6b425fdb82caf0d2a443
