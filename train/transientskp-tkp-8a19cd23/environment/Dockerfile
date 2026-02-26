FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/transientskp/tkp.git /data/project \
    && cd /data/project \
    && git checkout 8a19cd23c7141c66c1ee8e42295957bbcf809531
