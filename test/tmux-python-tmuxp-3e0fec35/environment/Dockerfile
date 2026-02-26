FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/tmux-python/tmuxp.git /data/project \
    && cd /data/project \
    && git checkout 3e0fec3596cc557456af4f51e66a72aebbfe7ff8
