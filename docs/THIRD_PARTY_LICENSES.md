# Danh mục Giấy phép Phần mềm Bên thứ ba (Third-Party Licenses)

Dự án **AI Career Coach** được cấp phép và phân phối dưới giấy phép nguồn mở **[MIT License](./LICENSE)**.

Tài liệu này liệt kê toàn bộ các thư viện, công cụ và thành phần bên thứ ba được khai báo trong `requirements.txt`, `Dockerfile`, `docker-compose.yml` và giao diện `front_end/`. Tất cả các thành phần này đều được nạp qua trình quản lý gói chuẩn (`pip`, `Docker Hub`, `CDN`), **không sao chép mã nguồn của dự án khác vào kho lưu trữ**, và có giấy phép **tương thích 100% với giấy phép MIT** của dự án.

---

## 1. Thư viện Backend Python (`requirements.txt`)

| Tên thư viện | Phiên bản yêu cầu | Giấy phép (SPDX) | Tương thích MIT | Mục đích sử dụng trong dự án |
| :--- | :---: | :---: | :---: | :--- |
| **FastAPI** (`fastapi`) | `>= 0.110.0` | `MIT` | Có | Xây dựng hệ thống RESTful API bất đồng bộ và tài liệu OpenAPI (Swagger UI) |
| **Uvicorn** (`uvicorn[standard]`) | `>= 0.29.0` | `BSD-3-Clause` | Có | Máy chủ ASGI hiệu năng cao vận hành ứng dụng FastAPI trong Docker |
| **SQLAlchemy** (`sqlalchemy`) | `>= 2.0.0` | `MIT` | Có | ORM quản lý 7 bảng dữ liệu và kết nối cơ sở dữ liệu PostgreSQL |
| **Psycopg2 Binary** (`psycopg2-binary`) | `>= 2.9.9` | `LGPL-3.0-or-later` | Có (Liên kết động qua driver DB) | Trình điều khiển (Adapter) kết nối Python với hệ quản trị PostgreSQL |
| **Pydantic** (`pydantic`) | `>= 2.0.0` | `MIT` | Có | Kiểm tra tính hợp lệ và chuẩn hóa cấu trúc dữ liệu đầu vào / đầu ra (Schemas) |
| **Ollama Python SDK** (`ollama`) | `>= 0.2.0` | `MIT` | Có | Giao tiếp trực tiếp với máy chủ mô hình ngôn ngữ lớn Ollama (`qwen3.5:4b`) |

---

## 2. Thư viện Giao diện Frontend (`front_end/index.html` - Nạp qua CDN)

| Tên thư viện | Nguồn nạp | Giấy phép (SPDX) | Tương thích MIT | Mục đích sử dụng trong dự án |
| :--- | :--- | :---: | :---: | :--- |
| **Tailwind CSS** | CDN (`cdn.tailwindcss.com`) | `MIT` | Có | Thiết kế hệ thống giao diện đáp ứng (Responsive UI) |
| **Chart.js** | jsDelivr CDN | `MIT` | Có | Vẽ biểu đồ Radar đối sánh năng lực ứng viên và yêu cầu công việc (JD) |
| **PDF.js** (`pdfjs-dist`) | Cloudflare CDN (`v2.16.105`) | `Apache-2.0` | Có | Đọc và bóc tách văn bản trực tiếp từ tệp CV định dạng `.pdf` phía trình duyệt |
| **Canvas Confetti** | jsDelivr CDN (`v1.6.0`) | `ISC` | Có | Hiệu ứng chúc mừng khi người học hoàn thành bài tập hoặc nâng cấp Mầm cây |
| **Google Fonts (Inter & JetBrains Mono)** | Google Fonts API | `OFL-1.1` | Có | Phông chữ hiển thị giao diện tiếng Việt và tiếng Anh |

---

## 3. Hạ tầng Container & Mô hình AI (`docker-compose.yml` & `Dockerfile`)

| Thành phần / Image | Nguồn chính thức | Giấy phép (SPDX) | Tương thích MIT | Vai trò trong kiến trúc 4 Containers |
| :--- | :--- | :---: | :---: | :--- |
| **Python 3.11 Slim** (`python:3.11-slim`) | Docker Official Image | `PSF-2.0` | Có | Môi trường thực thi Backend (`career_coach_backend`) |
| **Node.js 20 Alpine** (`node:20-alpine`) | Docker Official Image | `MIT` | Có | Máy chủ HTTP tĩnh phục vụ giao diện Web (`career_coach_frontend`) |
| **PostgreSQL 15** (`postgres:15`) | Docker Official Image | `PostgreSQL` | Có | Hệ quản trị cơ sở dữ liệu quan hệ (`career_coach_pg`) |
| **Ollama Server** (`ollama/ollama:latest`) | Ollama Official Image | `MIT` | Có | Máy chủ suy luận mô hình ngôn ngữ lớn cục bộ (`career_coach_ollama`) |
| **Qwen 3.5 (4B)** (`qwen3.5:4b`) | Alibaba Cloud Qwen | `Apache-2.0` | Có | Mô hình AI trích xuất CV/JD, lập lộ trình học và phỏng vấn STAR |

---

## 4. Kết luận Kiểm tra Tương thích Giấy phép

1. Toàn bộ tệp mã nguồn của dự án (`.py`, `.js`, `.css`, `.sh`) đều được gắn nhãn định danh chuẩn **`SPDX-License-Identifier: MIT`** ở dòng đầu tiên.
2. Không có bất kỳ thư viện nào thuộc nhóm giấy phép độc quyền hoặc xung đột bản quyền (như AGPL/GPL bắt buộc đóng mở mã nguồn trái phép).
3. Các giấy phép thành phần (`MIT`, `BSD-3-Clause`, `Apache-2.0`, `ISC`, `PSF-2.0`, `PostgreSQL`, và `LGPL-3.0` sử dụng qua thư viện động) đều hoàn toàn tương thích để phân phối cùng dự án dưới giấy phép **MIT License**.
