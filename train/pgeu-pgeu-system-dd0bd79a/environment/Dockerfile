FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/pgeu/pgeu-system.git /data/project \
    && cd /data/project \
    && git checkout dd0bd79ae43b3a0cb1b604bd7f5cae0081e5a4dc
