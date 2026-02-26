FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/lmcinnes/umap.git /data/project \
    && cd /data/project \
    && git checkout b45cece876513b3f95bd2dc7cb400240b1edab2a
