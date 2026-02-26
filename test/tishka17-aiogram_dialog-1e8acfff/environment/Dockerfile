FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tishka17/aiogram_dialog.git /data/project \
    && cd /data/project \
    && git checkout 1e8acfff912c720e2eae28aeca32abf696976363
