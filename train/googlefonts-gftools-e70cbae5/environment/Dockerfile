FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/googlefonts/gftools.git /data/project \
    && cd /data/project \
    && git checkout e70cbae529bf512339dd55f63d7516dba5a22a85
