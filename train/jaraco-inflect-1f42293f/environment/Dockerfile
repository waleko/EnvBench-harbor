FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jaraco/inflect.git /data/project \
    && cd /data/project \
    && git checkout 1f42293f30caacb0637f7eb30a483b44489f4812
