FROM python:3.10

ENV PYTHONUNBUFFERED 1

ARG DOCKER_HOME="/opt/yijunx"
ARG DOCKER_CODE="/opt/yijunx/code"
ARG DOCKER_GROUP="yijunx"
ARG DOCKER_USER="yijunx"
ARG DOCKER_UID=5000

WORKDIR ${DOCKER_CODE}

RUN groupadd -g ${DOCKER_UID} ${DOCKER_GROUP} && \
    useradd -r -u ${DOCKER_UID} -g ${DOCKER_GROUP} -d ${DOCKER_HOME} ${DOCKER_USER} && \
    chown -R ${DOCKER_USER}:${DOCKER_GROUP} ${DOCKER_HOME}

RUN apt-get update && \
    apt-get install -y tree && \
    apt-get install -y nano && \
    apt-get install -y sudo && \
    pip install --upgrade pip && \
    echo ${DOCKER_USER} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${DOCKER_USER} && \
    chmod 0440 /etc/sudoers.d/${DOCKER_USER}

ENV PATH "$PATH:/opt/yijunx/.local/bin"

USER ${DOCKER_USER}

ENTRYPOINT [ "/bin/sh", "-c" ]