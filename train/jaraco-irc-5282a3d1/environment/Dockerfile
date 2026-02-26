FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jaraco/irc.git /data/project \
    && cd /data/project \
    && git checkout 5282a3d1471d091da24f77adc75018dbc94cc912
