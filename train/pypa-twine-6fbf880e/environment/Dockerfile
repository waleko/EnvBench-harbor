FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pypa/twine.git /data/project \
    && cd /data/project \
    && git checkout 6fbf880ee60915cf1666348c4bdd78a10415f2ac
