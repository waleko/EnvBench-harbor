FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/hhursev/recipe-scrapers.git /data/project \
    && cd /data/project \
    && git checkout 4788af40bf47dba580b069d6ffc02fb071e967c1
