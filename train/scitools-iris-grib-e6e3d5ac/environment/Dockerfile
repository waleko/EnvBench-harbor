FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/scitools/iris-grib.git /data/project \
    && cd /data/project \
    && git checkout e6e3d5ac1d90b8851b9625a2b3df2af1a14f168f
