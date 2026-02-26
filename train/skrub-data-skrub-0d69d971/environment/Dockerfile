FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/skrub-data/skrub.git /data/project \
    && cd /data/project \
    && git checkout 0d69d97129aa638167e1e721686acb066daed007
