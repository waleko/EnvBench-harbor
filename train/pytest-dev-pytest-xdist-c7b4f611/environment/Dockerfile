FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pytest-dev/pytest-xdist.git /data/project \
    && cd /data/project \
    && git checkout c7b4f6114479d4053f0ef8411ed5e0a410b207f4
