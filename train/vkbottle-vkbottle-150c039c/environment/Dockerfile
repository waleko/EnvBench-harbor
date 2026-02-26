FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/vkbottle/vkbottle.git /data/project \
    && cd /data/project \
    && git checkout 150c039c231785322a0e01cac40cc860b9ab74e5
