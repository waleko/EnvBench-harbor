FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/embeddings-benchmark/mteb.git /data/project \
    && cd /data/project \
    && git checkout e169fb30e4f2cb01cdd1fa0667a325a6a73b5c01
