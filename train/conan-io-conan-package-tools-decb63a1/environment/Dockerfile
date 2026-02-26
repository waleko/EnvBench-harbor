FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/conan-io/conan-package-tools.git /data/project \
    && cd /data/project \
    && git checkout decb63a1a470a5ffd5adf3ae6074b740f086aef2
