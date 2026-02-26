FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tensorflow/model-analysis.git /data/project \
    && cd /data/project \
    && git checkout 807bd626f18613a5bfc8a5cc96cf29deee62f0ea
