FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/sphinx-gallery/sphinx-gallery.git /data/project \
    && cd /data/project \
    && git checkout 0d7823073f9307cfeaad370ad41207354dfe9713
