FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nabla-ntnu/nablaweb.git /data/project \
    && cd /data/project \
    && git checkout c0f51ad0cfbfb73de52fd041c002a5a3e4590c03
