FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rubisco-sfa/ilamb.git /data/project \
    && cd /data/project \
    && git checkout c0aecd5ea97c0817c1ef74935bc2d9aa3667195a
