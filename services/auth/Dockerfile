FROM cgr.dev/chainguard/wolfi-base as base-layer

ENV PYTHON_VERSION=3.12 \
    APP_USER=nonroot \
	PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache
RUN set -eux ;\
    apk update ;\
    apk upgrade ;\
    apk add python-${PYTHON_VERSION} py3-poetry ;

USER ${APP_USER}
WORKDIR /home/${APP_USER}
COPY --chown=${APP_USER}:${APP_USER} --chmod=775 src /home/${APP_USER}/project/src
COPY --chown=${APP_USER}:${APP_USER} --chmod=775 pyproject.toml poetry.lock README.md /home/${APP_USER}/

RUN set -eux; \
    poetry install --without dev ;\
    rm -rf $POETRY_CACHE_DIR pyproject.toml poetry.lock README.md ;\
    cd project && find . -type d -name '__pycache__' -exec rm -rf {} + ;


FROM cgr.dev/chainguard/wolfi-base as final

ENV APP_USER=nonroot \
    UID=1000 \
    GID=1000
ENV PYTHON_VERSION=3.12 \
	PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/home/${APP_USER}/.venv \
    PATH="/home/${APP_USER}/.venv/bin:$PATH"
# COPY --from=base-layer /usr/bin/supercronic /usr/bin/supercronic

RUN set -eux ;\
    apk update --no-cache ;\
    apk upgrade --no-cache ;\
    apk add --no-cache python-${PYTHON_VERSION} bash ;

USER ${APP_USER}
EXPOSE 8010
WORKDIR /home/${APP_USER}/
COPY --from=base-layer --chown=${UID}:${GID} --chmod=775 ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY --from=base-layer --chown=${UID}:${GID} --chmod=775 /home/${APP_USER}/project/ /home/${APP_USER}/project/

# COPY --chown=${APP_USER}:${APP_USER} --chmod=775 ./docker/stage.env /home/${APP_USER}/project/.env
# RUN (echo "58 5 * * * bash -c /home/${APP_USER}/project/scripts/daily_check.sh") >> /home/${APP_USER}/crontab

ENTRYPOINT ["bash", "-c", "cd project && granian --interface asgi src/main:app --host 0.0.0.0 --port 8010"]
