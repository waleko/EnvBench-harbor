FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ansible/ansible-zuul-jobs.git /data/project \
    && cd /data/project \
    && git checkout 33dd767b8609db931003583faa1eb47ac9fabfc1
