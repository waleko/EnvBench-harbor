FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/llm-random/llm-random.git /data/project \
    && cd /data/project \
    && git checkout 80c89d079aa004051fc14f5ffa6a6a62f22ea7da
