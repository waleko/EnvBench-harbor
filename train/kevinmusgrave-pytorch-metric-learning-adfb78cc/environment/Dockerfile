FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/kevinmusgrave/pytorch-metric-learning.git /data/project \
    && cd /data/project \
    && git checkout adfb78ccb275e5bd7a84d2693da41ff3002eed32
