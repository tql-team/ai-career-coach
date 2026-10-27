# Hướng dẫn Biên dịch, Cài đặt & Gỡ cài đặt (INSTALL)

Tài liệu này hướng dẫn chi tiết quy trình biên dịch từ mã nguồn, cài đặt hệ thống qua **Dockerfile / Docker Compose** và **GNU Make (`Makefile`)**, cách chạy chương trình từ ngoài thư mục mã nguồn, kiểm tra mô hình AI `qwen3.5:4b`, theo dõi nhật ký (Logs) và gỡ cài đặt hoàn toàn.

---

## 1. Yêu cầu hệ thống

* **Docker Engine & Docker Compose**: Cài đặt và khởi chạy sẵn [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/macOS) hoặc `docker-ce` + `docker-compose-plugin` (Linux).
* **GNU Make** *(Tùy chọn)*: Để sử dụng các lệnh tắt chuẩn hóa qua `Makefile` (`make install`, `make build`, `make uninstall`...).
* **Dung lượng ổ cứng trống**: Tối thiểu `4 GB` (để lưu trữ Docker images và mô hình ngôn ngữ lớn `qwen3.5:4b` ~2.7 GB).
* **Không cần cài đặt** Python, Node.js, PostgreSQL hay Ollama trên máy chủ thật vì toàn bộ đã được đóng gói độc lập trong 4 Docker Containers.

---

## 2. Tải mã nguồn và Cấu hình Biến môi trường

### Bước 1: Sao chép kho mã nguồn
```bash
git clone https://github.com/tql-team/ai-career-coach.git
cd ai-career-coach
```

### Bước 2: Khởi tạo tệp cấu hình môi trường (`.env`)
Hệ thống hỗ trợ tùy chỉnh toàn bộ cổng kết nối và thông tin cơ sở dữ liệu thông qua biến môi trường:
```bash
# Trên Linux / macOS / Git Bash:
cp scripts/.env.example .env

# Trên Windows PowerShell:
Copy-Item scripts/.env.example .env
```

---

## 3. Biên dịch & Cài đặt Hệ thống (Compilation & Installation)

Bạn có thể cài đặt hệ thống bằng **GNU Make** (Cách 1) hoặc trực tiếp bằng **Docker Compose / Dockerfile** (Cách 2).

### Cách 1: Sử dụng GNU Make (`Makefile`)
```bash
# Biên dịch các Docker image từ back_end/Dockerfile và front_end/Dockerfile
make build

# Cài đặt và khởi chạy toàn bộ 4 containers của hệ thống
make install
```

### Cách 2: Sử dụng trực tiếp Docker Compose & Dockerfile
```bash
# Biên dịch mới 2 Docker images (Backend & Frontend) và khởi chạy 4 containers ở chế độ nền
docker compose up --build -d
```

Nếu muốn biên dịch từng `Dockerfile` độc lập:
```bash
# 1. Biên dịch Backend Image (FastAPI + Python 3.11 + Timezone Asia/Ho_Chi_Minh)
docker build -t ai-career-coach-backend:latest ./back_end

# 2. Biên dịch Frontend Image (Node.js 20 Alpine - Cổng 5050)
docker build -t ai-career-coach-frontend:latest ./front_end
```

---

## 4. Chạy chương trình từ bên ngoài thư mục mã nguồn (Out-of-Source Execution)

Dự án được thiết kế để có thể biên dịch và khởi chạy từ bất kỳ thư mục làm việc nào trên hệ thống:

* **Qua Docker Compose**:
  ```bash
  docker compose -f /duong/dan/toi/ai-career-coach/docker-compose.yml up -d
  ```
* **Qua GNU Make**:
  ```bash
  make -f /duong/dan/toi/ai-career-coach/Makefile install
  ```
* **Qua trình quản lý gói Python (`pip` & `back_end/pyproject.toml`)**:
  ```bash
  pip install /duong/dan/toi/ai-career-coach/back_end
  ```

---

## 5. Kiểm tra Kết quả Cài đặt & Mô hình AI (`qwen3.5:4b`)

### 5.1. Địa chỉ truy cập dịch vụ
* **Giao diện Web ứng dụng (Frontend)**: [http://localhost:5050](http://localhost:5050)
* **Tài liệu REST API (Swagger UI)**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **Kiểm tra trạng thái Backend**: [http://localhost:8000/](http://localhost:8000/)

### 5.2. Kiểm tra Model AI đã tải về chưa
```bash
# Kiểm tra danh sách model AI trong container Ollama
docker exec -it career_coach_ollama ollama list
# Hoặc dùng Make:
make check-model
```
Nếu mạng gián đoạn khiến model chưa tải xong, bạn có thể chủ động kéo model kèm thanh tiến trình:
```bash
docker exec -it career_coach_ollama ollama pull qwen3.5:4b
```

### 5.3. Kiểm tra Nhật ký hoạt động (Check Logs)
```bash
# Xem trực tiếp log của Model AI (Trích xuất CV, JD, Lộ trình, Phỏng vấn STAR)
docker compose logs -f backend

# Xem tiến độ tải model của container Ollama
docker compose logs -f ollama
```

---

## 6. Hướng dẫn Gỡ cài đặt (Uninstallation)

* **Dừng tạm thời hệ thống (giữ lại dữ liệu Database & Model AI)**:
  ```bash
  docker compose down
  # Hoặc: make down
  ```
* **Gỡ cài đặt hoàn toàn (Xóa toàn bộ Containers, Volumes dữ liệu và Docker Images)**:
  ```bash
  docker compose down -v --rmi all --remove-orphans
  # Hoặc: make uninstall
  ```
