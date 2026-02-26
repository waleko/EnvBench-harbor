FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/yourlabs/django-autocomplete-light.git /data/project \
    && cd /data/project \
    && git checkout 45a9ff6e95e58348b90b3c1f01f01cb6ca10b4d3
