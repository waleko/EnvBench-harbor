FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/oarriaga/paz.git /data/project \
    && cd /data/project \
    && git checkout cede0aee7b0ce78357f884b916f96803f1cea202
