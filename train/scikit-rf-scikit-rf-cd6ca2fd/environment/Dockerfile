FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/scikit-rf/scikit-rf.git /data/project \
    && cd /data/project \
    && git checkout cd6ca2fd47597387cdaf0d4991b371de8fc2dd4e
