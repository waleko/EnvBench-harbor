FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dlubal-software/rfem_python_client.git /data/project \
    && cd /data/project \
    && git checkout 76e517ec0dc61e28f7c5c4b5e51df451185bc99a
