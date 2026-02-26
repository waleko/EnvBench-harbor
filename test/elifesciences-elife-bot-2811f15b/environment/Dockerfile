FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/elifesciences/elife-bot.git /data/project \
    && cd /data/project \
    && git checkout 2811f15bdc5b118e815be26dda843e527c403c26
