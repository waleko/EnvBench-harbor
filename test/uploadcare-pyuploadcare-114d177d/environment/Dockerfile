FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/uploadcare/pyuploadcare.git /data/project \
    && cd /data/project \
    && git checkout 114d177d479c55251c2cce9c401011903fe9a66b
