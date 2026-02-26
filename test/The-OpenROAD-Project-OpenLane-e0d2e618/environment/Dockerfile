FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/The-OpenROAD-Project/OpenLane.git /data/project \
    && cd /data/project \
    && git checkout e0d2e618a8834e733d28dfcc02fa166941be7e71
