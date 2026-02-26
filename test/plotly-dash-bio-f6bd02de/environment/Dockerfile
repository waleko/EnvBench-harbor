FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/plotly/dash-bio.git /data/project \
    && cd /data/project \
    && git checkout f6bd02de725a86779f6f0be260e730e1970cea5f
