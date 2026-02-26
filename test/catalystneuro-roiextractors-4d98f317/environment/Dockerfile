FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/catalystneuro/roiextractors.git /data/project \
    && cd /data/project \
    && git checkout 4d98f317aab93c0a7069e7f07292ece13039a8f9
