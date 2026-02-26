FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/xknx/xknx.git /data/project \
    && cd /data/project \
    && git checkout 69129602b7504b21c62fa085761d8b2e6697e4ae
