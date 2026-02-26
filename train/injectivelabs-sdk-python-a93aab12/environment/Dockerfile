FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/injectivelabs/sdk-python.git /data/project \
    && cd /data/project \
    && git checkout a93aab1257174769db96e208ac61464999323b32
