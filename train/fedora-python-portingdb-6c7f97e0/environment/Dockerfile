FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fedora-python/portingdb.git /data/project \
    && cd /data/project \
    && git checkout 6c7f97e01d35594833856bab7e187999fc78fea2
