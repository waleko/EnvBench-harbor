FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/hackerspace-ntnu/website.git /data/project \
    && cd /data/project \
    && git checkout 3bb89d03675c1a9286085f07c17f6fc62968e9a8
