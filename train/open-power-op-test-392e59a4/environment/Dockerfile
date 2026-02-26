FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/open-power/op-test.git /data/project \
    && cd /data/project \
    && git checkout 392e59a46ee10ff462e78ec884f21b785628190f
