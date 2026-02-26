FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/simplistix/testfixtures.git /data/project \
    && cd /data/project \
    && git checkout 608b0532dbbeb6530d9dacce3a912bcc1dc40a87
