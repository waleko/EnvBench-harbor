FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/ellmetha/django-machina.git /data/project \
    && cd /data/project \
    && git checkout e34c8ba4f1ba13f6f76dfcc20f276d2affc7c416
