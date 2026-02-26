FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mampfes/hacs_waste_collection_schedule.git /data/project \
    && cd /data/project \
    && git checkout a107f0e393b8f77b0da7971e530d0996344c6248
