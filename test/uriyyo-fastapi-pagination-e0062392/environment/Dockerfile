FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/uriyyo/fastapi-pagination.git /data/project \
    && cd /data/project \
    && git checkout e00623920b1cc8b3d20eac2a96fb81343091569a
