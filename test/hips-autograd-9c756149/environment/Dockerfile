FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/hips/autograd.git /data/project \
    && cd /data/project \
    && git checkout 9c756149ec3020286b21434023064226c9174b1a
