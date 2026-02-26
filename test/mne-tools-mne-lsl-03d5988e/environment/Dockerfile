FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/mne-tools/mne-lsl.git /data/project \
    && cd /data/project \
    && git checkout 03d5988ea6d940840e418b91f0d756134515e193
