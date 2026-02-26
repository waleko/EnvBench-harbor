FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nakagami/pyfirebirdsql.git /data/project \
    && cd /data/project \
    && git checkout 44f155d50e1668cf3e3f08ec15693eb72d4f1b60
