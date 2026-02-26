FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/google/uncertainty-baselines.git /data/project \
    && cd /data/project \
    && git checkout 15075c8973f4c5951a56788382ce490dae4f3c43
