FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/jonlabelle/sublimejsprettier.git /data/project \
    && cd /data/project \
    && git checkout 59831ef0e3ac4653974948ad1698d31a61172212
