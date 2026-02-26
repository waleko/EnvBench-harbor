FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/castagnait/plugin.video.netflix.git /data/project \
    && cd /data/project \
    && git checkout e87aa8559e9b0d38699a5383e09381ee7756783b
