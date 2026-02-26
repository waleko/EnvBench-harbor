FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/cherrypy/cheroot.git /data/project \
    && cd /data/project \
    && git checkout 1ff20b18e98e424e0616654c28c92524deef348a
