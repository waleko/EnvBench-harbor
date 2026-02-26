FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mad-lab-fau/biopsykit.git /data/project \
    && cd /data/project \
    && git checkout 2ad99fba5f55328109c72bd3cbb72ba2444da078
