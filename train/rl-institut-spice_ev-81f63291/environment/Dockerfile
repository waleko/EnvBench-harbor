FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/rl-institut/spice_ev.git /data/project \
    && cd /data/project \
    && git checkout 81f63291a7b52ce00ffc1a4746af6dacc92e3f1e
