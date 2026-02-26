FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/beeware/briefcase.git /data/project \
    && cd /data/project \
    && git checkout 448b58bcf928ae4e933fa342795785fb3211cd17
