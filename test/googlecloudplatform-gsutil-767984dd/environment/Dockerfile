FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/googlecloudplatform/gsutil.git /data/project \
    && cd /data/project \
    && git checkout 767984ddf846c5216a0f8f00a580ce72c15c978e
