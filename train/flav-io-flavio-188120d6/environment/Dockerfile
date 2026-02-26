FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/flav-io/flavio.git /data/project \
    && cd /data/project \
    && git checkout 188120d651c38419cd970957e5259071842f4cca
