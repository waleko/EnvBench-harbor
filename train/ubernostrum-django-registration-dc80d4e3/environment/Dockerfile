FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ubernostrum/django-registration.git /data/project \
    && cd /data/project \
    && git checkout dc80d4e3f90d64d12c35a6c494aa1ec9b36a1705
