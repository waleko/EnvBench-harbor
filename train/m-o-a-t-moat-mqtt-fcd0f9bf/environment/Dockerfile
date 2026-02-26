FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/m-o-a-t/moat-mqtt.git /data/project \
    && cd /data/project \
    && git checkout fcd0f9bf07548604d19d159ffb5fc543e78ce597
