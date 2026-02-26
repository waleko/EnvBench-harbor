FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ai4co/rl4co.git /data/project \
    && cd /data/project \
    && git checkout a6231241b8ddf2fd6f38f8931f42778d84e78603
