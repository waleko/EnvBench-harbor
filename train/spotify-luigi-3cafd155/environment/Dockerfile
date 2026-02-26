FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/spotify/luigi.git /data/project \
    && cd /data/project \
    && git checkout 3cafd155bbc35918cfce442f9cef445eaa97f13c
