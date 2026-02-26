FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dbiir/uer-py.git /data/project \
    && cd /data/project \
    && git checkout 5743050cc41f0f21986c9f938db5ac1726052629
