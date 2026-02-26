FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/zostera/django-bootstrap5.git /data/project \
    && cd /data/project \
    && git checkout f07d75182b27a351ad07ae89400591046f0b2f3d
