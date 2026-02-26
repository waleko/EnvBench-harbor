FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/conda-forge/staged-recipes.git /data/project \
    && cd /data/project \
    && git checkout 1f39220fd7628f44a2432a74695ab64b8badf9f1
