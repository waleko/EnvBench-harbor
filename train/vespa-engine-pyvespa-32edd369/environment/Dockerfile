FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/vespa-engine/pyvespa.git /data/project \
    && cd /data/project \
    && git checkout 32edd3699cc00c9bd7ad933fd74155acb59a4747
