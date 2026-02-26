FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/adamchainz/django-mysql.git /data/project \
    && cd /data/project \
    && git checkout d6f0500565b1e4bc94044ca061e745cada955c11
