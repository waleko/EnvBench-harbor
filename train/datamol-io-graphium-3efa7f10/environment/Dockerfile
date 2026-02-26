FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/datamol-io/graphium.git /data/project \
    && cd /data/project \
    && git checkout 3efa7f106e6443f9213c498be115ced15556754d
