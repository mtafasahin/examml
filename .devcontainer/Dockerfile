FROM python:3.12-slim-bookworm

# Çalışma klasörü
WORKDIR /app

# Gerekli sistem paketlerini yükle
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
RUN pip install --upgrade pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN pip install ultralytics opencv-python numpy pandas matplotlib notebook

# Varsayılan komut
# Container'ı sürekli açık tutacak komut
ENTRYPOINT ["sleep", "infinity"]
