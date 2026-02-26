FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cvxgrp/cvxportfolio.git /data/project \
    && cd /data/project \
    && git checkout 831fc7c6e691c4e5d27ecf870ba52d7440bf4784
