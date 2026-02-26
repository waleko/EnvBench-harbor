FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/thouska/spotpy.git /data/project \
    && cd /data/project \
    && git checkout 7e5e3f4f268e45e150ba8407dd6747c2f85c4cc0
