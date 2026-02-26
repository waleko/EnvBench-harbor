FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/idaholab/civet.git /data/project \
    && cd /data/project \
    && git checkout 282f2cb1c72197cd34d4a38d396720bfaa6d7fc5
