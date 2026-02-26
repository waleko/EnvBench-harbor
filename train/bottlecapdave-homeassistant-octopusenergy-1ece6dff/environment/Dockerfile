FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bottlecapdave/homeassistant-octopusenergy.git /data/project \
    && cd /data/project \
    && git checkout 1ece6dff9948051323f51aeee4c861ccaeb7d548
