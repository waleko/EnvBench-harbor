FROM ghcr.io/jetbrains-research/envbench-python:latest
RUN mkdir -p /logs/verifier /logs/agent
WORKDIR /data/project
RUN rm -rf /data/project/* /data/project/.* 2>/dev/null; \
    git clone https://github.com/yubico/yubikey-manager.git /data/project \
    && cd /data/project \
    && git checkout fbdae2bc12ba0451bcfc62372bc9191c10ecad0c
