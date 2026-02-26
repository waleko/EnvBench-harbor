FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/naomiproject/naomi.git /data/project \
    && cd /data/project \
    && git checkout f0984bd57dd0adf3a379116f46316bd62bad2ace
