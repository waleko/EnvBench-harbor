FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pysmt/pysmt.git /data/project \
    && cd /data/project \
    && git checkout d11b296fefcb29ef917259c6273e1541b3ec5c68
