FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/camdavidsonpilon/lifelines.git /data/project \
    && cd /data/project \
    && git checkout b8f017446e81c8f2fec75970e3afbc130f7131ec
