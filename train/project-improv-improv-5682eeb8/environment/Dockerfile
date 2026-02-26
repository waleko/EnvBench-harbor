FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/project-improv/improv.git /data/project \
    && cd /data/project \
    && git checkout 5682eeb82b9a8acd3cd5a9960e5cef308efc7f3e
