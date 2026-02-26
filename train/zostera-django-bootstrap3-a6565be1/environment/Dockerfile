FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/zostera/django-bootstrap3.git /data/project \
    && cd /data/project \
    && git checkout a6565be14ed0edff98b84d2874dc709cbecb1118
