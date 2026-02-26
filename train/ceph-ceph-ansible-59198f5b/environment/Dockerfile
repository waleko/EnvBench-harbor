FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ceph/ceph-ansible.git /data/project \
    && cd /data/project \
    && git checkout 59198f5bcdf2eca5cc99c25951d93513c508c01e
