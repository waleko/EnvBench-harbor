FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dnarayanan/powderday.git /data/project \
    && cd /data/project \
    && git checkout d81ce05aa0baedaa4b63b17abc0963b64fb33bbc
