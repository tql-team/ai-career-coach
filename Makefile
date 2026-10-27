# SPDX-License-Identifier: MIT
# Makefile chuẩn GNU Make điều phối biên dịch, cài đặt, vận hành và gỡ cài đặt bằng Docker

PROJECT_DIR := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
COMPOSE_FILE := $(PROJECT_DIR)docker-compose.yml
DOCKER_COMPOSE := docker compose -f "$(COMPOSE_FILE)"
PYTHON ?= python3
PIP ?= pip

.PHONY: all help build install up start run down stop restart logs logs-backend logs-ollama logs-frontend logs-db check-model ps clean uninstall check-spdx

all: build

help:
	@echo "=================================================================="
	@echo " AI Career Coach (v0.2.0) - Bảng điều khiển GNU Make & Docker"
	@echo "=================================================================="
	@echo "  make build         : Biên dịch Docker images (Backend & Frontend)"
	@echo "  make install       : Biên dịch và cài đặt trọn bộ 4 Docker containers"
	@echo "  make up            : Khởi chạy hệ thống ở chế độ nền (Detached)"
	@echo "  make down          : Dừng hệ thống (giữ lại dữ liệu DB & Model AI)"
	@echo "  make logs          : Xem trực tiếp nhật ký của Model AI & Backend"
	@echo "  make check-model   : Kiểm tra model AI qwen3.5:4b đã tải xong chưa"
	@echo "  make check-spdx    : Kiểm tra SPDX-License-Identifier trong mã nguồn"
	@echo "  make clean         : Dọn dẹp bộ nhớ đệm Python (__pycache__)"
	@echo "  make uninstall     : Gỡ cài đặt hoàn toàn containers, volumes, images"
	@echo "=================================================================="

build:
	$(DOCKER_COMPOSE) build

install:
	@if [ ! -f "$(PROJECT_DIR).env" ] && [ -f "$(PROJECT_DIR)scripts/.env.example" ]; then \
		cp "$(PROJECT_DIR)scripts/.env.example" "$(PROJECT_DIR).env"; \
	fi
	$(DOCKER_COMPOSE) up --build -d
	@echo "Cài đặt hoàn tất! Giao diện Web: http://localhost:5050 | API Docs: http://localhost:8000/docs"

up start run:
	$(DOCKER_COMPOSE) up -d

up-gpu:
	$(DOCKER_COMPOSE) -f "$(PROJECT_DIR)scripts/docker-compose.gpu.yml" up --build -d

down stop:
	$(DOCKER_COMPOSE) down

restart:
	$(DOCKER_COMPOSE) restart

ps:
	$(DOCKER_COMPOSE) ps

logs logs-backend:
	$(DOCKER_COMPOSE) logs -f backend

logs-ollama:
	$(DOCKER_COMPOSE) logs -f ollama

logs-frontend:
	$(DOCKER_COMPOSE) logs -f frontend

logs-db:
	$(DOCKER_COMPOSE) logs -f postgres_db

check-model:
	docker exec career_coach_ollama ollama list

check-spdx:
	@bash "$(PROJECT_DIR)scripts/add_spdx_headers.sh"

clean:
	find "$(PROJECT_DIR)" -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find "$(PROJECT_DIR)" -type f -name "*.pyc" -delete 2>/dev/null || true

uninstall:
	$(DOCKER_COMPOSE) down -v --rmi all --remove-orphans
