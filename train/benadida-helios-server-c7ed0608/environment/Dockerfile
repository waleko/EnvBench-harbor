FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/benadida/helios-server.git /data/project \
    && cd /data/project \
    && git checkout c7ed0608e2cdfc75bf323a834f0ca579e6273e34
