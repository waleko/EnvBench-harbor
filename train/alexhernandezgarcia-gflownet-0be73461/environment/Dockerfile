FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/alexhernandezgarcia/gflownet.git /data/project \
    && cd /data/project \
    && git checkout 0be734618221d5b4549af057ac3d4a7d7d8179b7
