# to build run: docker build -t clapbackbot_container .
# to run container: docker run -p 5173:5173 -p 5000:5000 clapbackbot_container

FROM pytorch/pytorch

WORKDIR /

# install node
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# install backend
COPY backend/ ./backend/
RUN pip install --no-cache-dir --default-timeout=10000 -r backend/requirements.txt

# install frontend
COPY frontend/ ./frontend/
WORKDIR /frontend
RUN npm install

# expose ports
EXPOSE 5173
EXPOSE 5000

# run both servers
WORKDIR /
CMD ["bash", "-c", "python3 backend/server.py & cd /frontend && npm run dev -- --host"]
