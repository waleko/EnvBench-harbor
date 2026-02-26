FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/smarr/rebench.git /data/project \
    && cd /data/project \
    && git checkout 1de0e22fb3e9578b3aeb7a994481ead300fa977f
