FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/Lightning-AI/litgpt.git /data/project \
    && cd /data/project \
    && git checkout 0c609550dfb61699ee513defd64da64634ee3788
