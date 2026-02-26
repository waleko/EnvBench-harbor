FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mercedes-benz/odxtools.git /data/project \
    && cd /data/project \
    && git checkout 4fb846fe59b749cd6dc75066f5a88bb236a86841
