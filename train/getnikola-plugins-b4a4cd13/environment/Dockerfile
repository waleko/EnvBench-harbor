FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/getnikola/plugins.git /data/project \
    && cd /data/project \
    && git checkout b4a4cd1332d4c149bef9c0b884e8f7045327cbf1
