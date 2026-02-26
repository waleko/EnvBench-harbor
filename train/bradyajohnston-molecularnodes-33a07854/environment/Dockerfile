FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/bradyajohnston/molecularnodes.git /data/project \
    && cd /data/project \
    && git checkout 33a07854f471eebe8f131d260b3fcbc9416f69b0
