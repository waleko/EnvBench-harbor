FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/brightway-lca/brightway2-io.git /data/project \
    && cd /data/project \
    && git checkout e315f08801fc928bc586f0004b07cf9d651b567d
