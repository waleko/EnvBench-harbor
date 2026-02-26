FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/python-control/python-control.git /data/project \
    && cd /data/project \
    && git checkout dbc998dedf8e18dcdcc15acf15303f22adf9368f
