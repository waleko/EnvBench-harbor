FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pajbot/pajbot.git /data/project \
    && cd /data/project \
    && git checkout a0d969a570c7bd06fcf1829b6f3465c1b250f0a3
