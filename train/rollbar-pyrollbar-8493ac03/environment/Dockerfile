FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rollbar/pyrollbar.git /data/project \
    && cd /data/project \
    && git checkout 8493ac03c3468c2349c968726adffa5fd5661d0e
