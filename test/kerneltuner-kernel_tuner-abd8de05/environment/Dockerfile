FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/kerneltuner/kernel_tuner.git /data/project \
    && cd /data/project \
    && git checkout abd8de05aafa25bc24ea86be3501e8ec3ab6682c
