FROM cgr.dev/chainguard/wolfi-base

ENV PYTHON_VERSION=3.12 \
    APP_USER=nonroot \
	PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    PROTOC_URL=https://github.com/protocolbuffers/protobuf/releases/download/v25.3/protoc-25.3-linux-x86_64.zip \
    PROTOC=protoc

WORKDIR /home/${APP_USER}
RUN set -eux ;\
    apk update ;\
    apk upgrade ;\
    apk add python-${PYTHON_VERSION} py3-pip curl ;\
    curl -fsSLO "$PROTOC_URL" \
    && unzip protoc-25.3-linux-x86_64.zip \
    && chmod +x "bin/$PROTOC" \
    && mv "bin/$PROTOC" "/usr/local/bin/${PROTOC}" \
    && ln -s "/usr/local/bin/${PROTOC}" /usr/local/bin/${PROTOC}
USER ${APP_USER}
COPY --chown=${APP_USER}:${APP_USER} --chmod=775 ./protos /home/${APP_USER}/protos
RUN set -eux ;\
    pip install --upgrade pip setuptools ;\
    pip install grpcio-tools ;\
    mkdir output ;\
    python -m grpc_tools.protoc -I./protos/auth --python_out=./output/ --pyi_out=./output/ --grpc_python_out=./output/ ./protos/auth/user.proto ;
CMD [ "sh" ]
