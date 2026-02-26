FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/microsoftgraph/msgraph-sdk-python-core.git /data/project \
    && cd /data/project \
    && git checkout e36c17424c9d443bdfeafc32f32682529ce25f95
