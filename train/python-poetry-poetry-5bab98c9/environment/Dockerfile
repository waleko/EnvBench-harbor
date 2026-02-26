FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/python-poetry/poetry.git /data/project \
    && cd /data/project \
    && git checkout 5bab98c9500f1050c6bb6adfb55580a23173f18d
