FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/karlicoss/hpi.git /data/project \
    && cd /data/project \
    && git checkout 35dd5d82a0e399f684fb3d09763bab44146927fc
