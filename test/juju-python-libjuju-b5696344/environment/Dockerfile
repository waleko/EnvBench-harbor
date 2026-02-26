FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/juju/python-libjuju.git /data/project \
    && cd /data/project \
    && git checkout b56963442a6deffe46ce1fb5cb41970344263649
