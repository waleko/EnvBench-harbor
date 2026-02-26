FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/openml/automlbenchmark.git /data/project \
    && cd /data/project \
    && git checkout f4aa6764c48ae069fd351ca508f72952ade0d2ee
