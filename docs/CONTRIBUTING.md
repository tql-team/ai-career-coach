# Hướng dẫn Đóng góp Mã nguồn (Contributing Guide)

Cảm ơn bạn đã quan tâm và đóng góp cho dự án **AI Career Coach**! Tài liệu này hướng dẫn chi tiết cho người mới về quy trình làm việc với **Git**, cách tạo nhánh (Branch), quy chuẩn **Pull Request (PR)**, quy tắc bản quyền **SPDX** và cách kiểm thử trên **Docker** trước khi gửi đóng góp.

---

## 1. Quy trình làm việc với Git cho người mới (Git Workflow)

### Bước 1: Fork và Clone kho mã nguồn
1. Truy cập kho mã nguồn chính thức tại: [https://github.com/tql-team/ai-career-coach.git](https://github.com/tql-team/ai-career-coach.git)
2. Tải mã nguồn về máy cá nhân:
   ```bash
   git clone https://github.com/tql-team/ai-career-coach.git
   cd ai-career-coach
   ```

### Bước 2: Tạo nhánh phát triển mới (Branching Convention)
Tuyệt đối không làm việc trực tiếp trên nhánh `main` mà hãy tạo nhánh riêng theo mục đích công việc:
* Thêm tính năng mới: `feat/<ten-tinh-nang>` *(Ví dụ: `feat/cv-bilingual-extract`)*
* Sửa lỗi (Bug fix): `fix/<ten-loi>` *(Ví dụ: `fix/logout-profile-storage`)*
* Cập nhật tài liệu: `docs/<noi-dung>` *(Ví dụ: `docs/update-install-guide`)*

```bash
git checkout -b feat/ten-tinh-nang-moi
```

---

## 2. Quy chuẩn Mã nguồn & Giấy phép (Coding Standards & SPDX)

1. **Bắt buộc gắn nhãn `SPDX-License-Identifier: MIT` ở dòng đầu tiên của mọi tệp mã nguồn mới**:
   * Với tệp Python (`.py`):
     ```python
     # SPDX-License-Identifier: MIT
     ```
   * Với tệp JavaScript (`.js`):
     ```javascript
     // SPDX-License-Identifier: MIT
     ```
   * Bạn có thể chạy tự động lệnh sau để quét và bổ sung header cho toàn bộ dự án:
     ```bash
     bash scripts/add_spdx_headers.sh
     ```
2. **Dấu xuống dòng chuẩn Unix (`LF`)**:
   * Dự án sử dụng tệp `.gitattributes` với cấu hình `eol=lf`. Không commit các tệp chứa ký tự xuống dòng kiểu Windows (`CRLF`).
3. **Không đưa tệp nặng hoặc thông tin nhạy cảm vào Git**:
   * Không commit tệp `.env`, dữ liệu cơ sở dữ liệu (`pgdata/`) hoặc tệp trọng số mô hình AI (> 100MB).

---

## 3. Kiểm thử bằng Docker trước khi tạo Pull Request

Mọi thay đổi đối với Backend (`back_end/`) hoặc Frontend (`front_end/`) đều phải được biên dịch và kiểm thử trên Docker Compose:

```bash
# 1. Biên dịch lại Docker images và khởi chạy hệ thống
docker compose up --build -d

# 2. Kiểm tra trạng thái 4 containers đều Running / Healthy
docker compose ps

# 3. Kiểm tra nhật ký Backend & AI không phát sinh lỗi
docker compose logs --tail=50 backend
```

---

## 4. Quy chuẩn Commit & Tạo Pull Request (PR)

### 4.1. Định dạng thông điệp Commit (Conventional Commits)
Sử dụng tiền tố rõ ràng khi viết `git commit`:
* `feat: ...` — Thêm tính năng mới
* `fix: ...` — Sửa lỗi logic hoặc giao diện
* `docs: ...` — Cập nhật tài liệu (`README.md`, `INSTALL.md`, `docs/`...)
* `chore: ...` — Cập nhật cấu hình Docker, `Makefile`, giấy phép

```bash
git add -A
git commit -m "feat: mô tả ngắn gọn thay đổi của bạn"
git push origin feat/ten-tinh-nang-moi
```

### 4.2. Gửi Pull Request (PR)
1. Mở trang [GitHub Pull Requests](https://github.com/tql-team/ai-career-coach/pulls) và nhấn **New Pull Request**.
2. Mô tả rõ:
   * Vấn đề hoặc tính năng được giải quyết (liên kết tới mã Issue nếu có, ví dụ `Closes #12`).
   * Các bước kiểm thử đã thực hiện trên Docker.
   * Ảnh chụp màn hình hoặc log kết quả (nếu thay đổi giao diện hoặc đầu ra AI).
