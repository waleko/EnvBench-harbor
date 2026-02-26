FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/getsentry/sentry-python.git /data/project \
    && cd /data/project \
    && git checkout ec7172e15311b88695827a76ca7fa83fba2efff4
