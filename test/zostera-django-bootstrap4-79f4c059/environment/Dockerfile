FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/zostera/django-bootstrap4.git /data/project \
    && cd /data/project \
    && git checkout 79f4c059f33d3ad11b66c305f295eb42d71f95da
