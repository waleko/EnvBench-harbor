FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/nixtla/neuralforecast.git /data/project \
    && cd /data/project \
    && git checkout 90b6fd06dc59fa3f320c57f361d4ca8379aa6be7
