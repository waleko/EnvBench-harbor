FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/guardrails-ai/guardrails.git /data/project \
    && cd /data/project \
    && git checkout d85ea96e123850391e2667864f148639dc335b9e
