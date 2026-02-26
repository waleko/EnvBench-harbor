FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/owid/etl.git /data/project \
    && cd /data/project \
    && git checkout 461bcb9e87f0afd0c805ed477a125ca010d1461a
