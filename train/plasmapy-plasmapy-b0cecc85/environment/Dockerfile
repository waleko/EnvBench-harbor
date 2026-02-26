FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/plasmapy/plasmapy.git /data/project \
    && cd /data/project \
    && git checkout b0cecc85d74c5f9c666b4bfb06f5e3fbc308f321
