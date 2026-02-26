FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/basxsoftwareassociation/basxconnect.git /data/project \
    && cd /data/project \
    && git checkout a616dd61bb6012de1668ba0e3c289924e69cff68
