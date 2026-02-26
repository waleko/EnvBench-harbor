FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ansible/molecule.git /data/project \
    && cd /data/project \
    && git checkout fd3ed55b11bf896aa1892ee75a6f32761eed3032
