FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/scylladb/sphinx-scylladb-theme.git /data/project \
    && cd /data/project \
    && git checkout 4e3917945c5c194a7119cf10629f35664b451d61
