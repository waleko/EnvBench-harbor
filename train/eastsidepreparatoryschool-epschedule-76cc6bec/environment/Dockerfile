FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/eastsidepreparatoryschool/epschedule.git /data/project \
    && cd /data/project \
    && git checkout 76cc6bec7d37dedae67c6926142ae37cbf15194a
