FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/facebookresearch/hydra.git /data/project \
    && cd /data/project \
    && git checkout 2e682d84e789d82dd11ab1f329f2dd1966fa6b54
