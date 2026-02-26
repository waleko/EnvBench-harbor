FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/google-deepmind/acme.git /data/project \
    && cd /data/project \
    && git checkout bea6d6b27c366cd07dd5202356f372e02c1f3f9b
