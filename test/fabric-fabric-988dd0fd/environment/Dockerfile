FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fabric/fabric.git /data/project \
    && cd /data/project \
    && git checkout 988dd0fd05db47331cb43d0ea9787908ef33219c
