FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/piccolo-orm/piccolo.git /data/project \
    && cd /data/project \
    && git checkout 17c0a8859c19da48b33a19bb5a15d44d91bb6278
