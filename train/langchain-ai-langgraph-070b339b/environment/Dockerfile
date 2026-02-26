FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/langchain-ai/langgraph.git /data/project \
    && cd /data/project \
    && git checkout 070b339b67d64773fbfdf296a52a334fa27af2ac
