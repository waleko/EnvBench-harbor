FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mansenfranzen/autodoc_pydantic.git /data/project \
    && cd /data/project \
    && git checkout 98cdeddfeb632c0f68fef4f04ff26ead37ae56cd
