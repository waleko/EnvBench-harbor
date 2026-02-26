FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jacebrowning/memegen.git /data/project \
    && cd /data/project \
    && git checkout 40d58684d5eb073dbb1ad147a70ab31ca09b4c6f
