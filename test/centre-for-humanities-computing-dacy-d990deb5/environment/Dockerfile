FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/centre-for-humanities-computing/dacy.git /data/project \
    && cd /data/project \
    && git checkout d990deb52cb56510d299aaf5e31c79e964e3aaae
