FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/Quantum-Accelerators/quacc.git /data/project \
    && cd /data/project \
    && git checkout f6bc96ca8f169e2474a09e96cb84f2dc14227ff2
