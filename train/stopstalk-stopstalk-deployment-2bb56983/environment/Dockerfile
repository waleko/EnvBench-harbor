FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/stopstalk/stopstalk-deployment.git /data/project \
    && cd /data/project \
    && git checkout 2bb56983cedeaf684aeea122d56bcb2996f66bc9
