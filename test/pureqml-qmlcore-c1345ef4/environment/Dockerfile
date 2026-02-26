FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pureqml/qmlcore.git /data/project \
    && cd /data/project \
    && git checkout c1345ef4bd8493cadf628d78c892423005528c46
