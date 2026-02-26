FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nrbnlulu/strawberry-django-auth.git /data/project \
    && cd /data/project \
    && git checkout da75552a58f038c638db3945bb85b36a1489f990
