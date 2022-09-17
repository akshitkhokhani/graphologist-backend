FROM ubuntu
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3-opencv \
    libsndfile1-dev\
    ca-certificates \
    g++ \
    python3.8-dev \
    python3-pip \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN cd /tmp \
    && curl -O https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py
WORKDIR /.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8080
ENTRYPOINT ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8080","--timeout-keep-alive","300"]