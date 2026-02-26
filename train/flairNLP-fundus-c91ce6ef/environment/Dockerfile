FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/flairNLP/fundus.git /data/project \
    && cd /data/project \
    && git checkout c91ce6ef6625c9ab2711e696643c3a5014695e66
