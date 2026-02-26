FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/open-cas/open-cas-linux.git /data/project \
    && cd /data/project \
    && git checkout ba5bdf4796bca9995033584473da0075d7aef83d
