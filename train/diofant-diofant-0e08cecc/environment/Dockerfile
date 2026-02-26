FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/diofant/diofant.git /data/project \
    && cd /data/project \
    && git checkout 0e08cecc3943ce35c91d9adcc4cdd42dc4bd7528
