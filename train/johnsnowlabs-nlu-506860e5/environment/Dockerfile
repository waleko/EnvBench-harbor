FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/johnsnowlabs/nlu.git /data/project \
    && cd /data/project \
    && git checkout 506860e546076b353969b5a3216c05d080ad923e
