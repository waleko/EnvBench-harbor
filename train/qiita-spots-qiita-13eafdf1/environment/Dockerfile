FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/qiita-spots/qiita.git /data/project \
    && cd /data/project \
    && git checkout 13eafdf1a2eb0c8b5d4019ad294b7490cd396139
