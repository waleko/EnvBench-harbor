FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/internetarchive/brozzler.git /data/project \
    && cd /data/project \
    && git checkout 8d7507f37757b6b9caf6f0d948666c7e5f972894
