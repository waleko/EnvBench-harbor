FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/dj-stripe/dj-stripe.git /data/project \
    && cd /data/project \
    && git checkout f271062a7662968385113df2482cd26a2ec69ac9
