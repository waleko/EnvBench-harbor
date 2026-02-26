FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/sasview/sasview.git /data/project \
    && cd /data/project \
    && git checkout d1703801b437b8c8b604baf284053aee5fdf4e03
