FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/wilcoxjay/mypyvy.git /data/project \
    && cd /data/project \
    && git checkout 3a055dfad3d13fb35b6125ab6f43fa6ea4493b5f
