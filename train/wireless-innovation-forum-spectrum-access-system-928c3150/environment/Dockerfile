FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/wireless-innovation-forum/spectrum-access-system.git /data/project \
    && cd /data/project \
    && git checkout 928c3150adf7b31e53a96b695bf1fbdd3284ecb2
