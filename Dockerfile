###################################
########## Builder image ##########
###################################
FROM python:3.11-slim-bullseye AS builder

# Install poetry
# See https://python-poetry.org/docs/#ci-recommendations
ENV POETRY_HOME /opt/poetry
ENV POETRY_VERSION 1.3.1
RUN python3 -m venv $POETRY_HOME; \
    $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION
ENV PATH $POETRY_HOME/bin:$PATH

WORKDIR /app

# Install dependencies into a virtual environment
# hadolint global ignore=SC1091
COPY pyproject.toml poetry.lock ./
RUN python3 -m venv --copies /app/venv; \
    source venv/bin/activate; \
    poetry install --no-root --no-interaction --without dev

###################################
######## Production image #########
###################################
FROM python:3.11-slim-bullseye as prod

# Copy the virtual environment from the build stage
COPY --from=builder /app/venv /app/venv/
ENV PATH /app/venv/bin:$PATH

# Set up non-root user
ARG USERNAME=non-priviliged-user
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME; \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
USER $USERNAME

WORKDIR /app
COPY --chown=non-priviliged-user:non-priviliged-user src src

ENV ENV prod
ENV APP_ENV $ENV

CMD ["python", "src/hello_world/hello_world.py"]
