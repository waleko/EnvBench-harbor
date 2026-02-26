FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tortoise/tortoise-orm.git /data/project \
    && cd /data/project \
    && git checkout bc18384bdb490cc14e96d27a18956fe1b122829d
