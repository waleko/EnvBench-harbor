FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jazzband/tablib.git /data/project \
    && cd /data/project \
    && git checkout 2121267b45fe54b47b9dd4c74c203bf82eff8b97
