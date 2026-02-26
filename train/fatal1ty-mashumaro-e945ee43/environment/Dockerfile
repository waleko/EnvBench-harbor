FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/fatal1ty/mashumaro.git /data/project \
    && cd /data/project \
    && git checkout e945ee4319db49da9f7b8ede614e988cc8c8956b
