FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/gamesdonequick/donation-tracker.git /data/project \
    && cd /data/project \
    && git checkout 63411a9fd9d803b5dd85507682b79835b99a99b0
