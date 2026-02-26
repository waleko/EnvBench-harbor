FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fillll/reddit2telegram.git /data/project \
    && cd /data/project \
    && git checkout 9899113b47d24c3eaebaf566718903990794e07c
