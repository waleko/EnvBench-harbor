FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/sassoftware/python-sasctl.git /data/project \
    && cd /data/project \
    && git checkout ebd0a63804ee752404e118762ab4bceb67705641
