FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/basxsoftwareassociation/bread.git /data/project \
    && cd /data/project \
    && git checkout b26203df8f81fcbf5f299dfe07dc808309349ecd
