FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/folio-fse/folio_migration_tools.git /data/project \
    && cd /data/project \
    && git checkout 4e994d26b7630d1dd994edf641759ca3f4dc1f28
