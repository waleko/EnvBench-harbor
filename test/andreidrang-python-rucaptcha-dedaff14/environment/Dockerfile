FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/andreidrang/python-rucaptcha.git /data/project \
    && cd /data/project \
    && git checkout dedaff141ece2f949bfda321cedf9e985111d995
