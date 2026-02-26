FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dtmilano/androidviewclient.git /data/project \
    && cd /data/project \
    && git checkout 8738d3af40921b861f25780b4a92b5b6d4990af1
