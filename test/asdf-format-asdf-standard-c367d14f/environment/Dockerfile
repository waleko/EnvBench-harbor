FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/asdf-format/asdf-standard.git /data/project \
    && cd /data/project \
    && git checkout c367d14fae4b5155679e2c40b531140586e25daf
