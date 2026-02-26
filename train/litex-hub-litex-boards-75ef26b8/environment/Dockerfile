FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/litex-hub/litex-boards.git /data/project \
    && cd /data/project \
    && git checkout 75ef26b8e54b7b0c1c5e2fba63336f0752b96c2b
