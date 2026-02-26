FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/kedro-org/kedro.git /data/project \
    && cd /data/project \
    && git checkout 9883223c9e03a58c2acc572ac65ce0d223d899ad
