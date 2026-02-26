FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/python-markdown/markdown.git /data/project \
    && cd /data/project \
    && git checkout 33359faa385f59b84cd87df5f4b0996055a482e2
