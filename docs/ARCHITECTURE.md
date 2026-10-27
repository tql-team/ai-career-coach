# Kiến trúc Hệ thống & Cơ sở dữ liệu (Architecture Guide)

Tài liệu này mô tả kiến trúc kỹ thuật của **AI Career Coach: Trợ lý định hướng nghề nghiệp và luyện phỏng vấn thông minh**, bao gồm sơ đồ điều phối 4 Docker Containers, cấu trúc 7 bảng cơ sở dữ liệu PostgreSQL 15 và luồng xử lý của mô hình AI `qwen3.5:4b`.

---

## 1. Kiến trúc 4 Docker Containers (`docker-compose.yml`)

| Container | Image / Dockerfile | Cổng Host -> Container | Vai trò |
| :--- | :--- | :---: | :--- |
| `career_coach_pg` | `postgres:15` | `5433 -> 5432` | Lưu trữ bền vững 7 bảng dữ liệu qua Docker Volume `pgdata` |
| `career_coach_ollama` | `ollama/ollama:latest` | `11435 -> 11434` | Máy chủ suy luận AI cục bộ, tự động tải và lưu model `qwen3.5:4b` vào volume `ollama_data` |
| `career_coach_backend` | `./back_end/Dockerfile` (`python:3.11-slim`) | `8000 -> 8000` | Máy chủ FastAPI xử lý 20 REST API endpoints, đồng bộ múi giờ `Asia/Ho_Chi_Minh` (`UTC+7`) |
| `career_coach_frontend` | `./front_end/Dockerfile` (`node:20-alpine`) | `5050 -> 5050` | Máy chủ giao diện Web SPA phục vụ người dùng tại `http://localhost:5050` |

---

## 2. Thiết kế 7 Bảng Cơ sở dữ liệu (`back_end/models.py` & `back_end/main.py`)

1. **`profiles`**: Lưu thông tin tài khoản học viên (`id`, `name`, `email`, mật khẩu băm `SHA-256`, `skills_json`, `interests_json`, `experience_text`, `free_time_json`). Hồ sơ mẫu sử dụng dải ID riêng (`9991`–`9993`) tách biệt với chuỗi tự tăng của người dùng thật.
2. **`jobs`**: Lưu tiêu đề, nội dung mô tả công việc (JD) và danh sách kỹ năng yêu cầu (`requirements_json`).
3. **`analyses`**: Lưu lịch sử đối sánh độ khớp CV – JD (`total_score`, `gaps_json`, `reasons_json`).
4. **`study_tasks`**: Lưu từng bài học trong lộ trình cá nhân hóa (`title`, `duration_minutes`, `scheduled_day`, `unlock_time`, `deadline_time`, `status`: `locked` / `active` / `completed` / `excused` / `unscheduled`).
5. **`streaks_and_reports`**: Lưu trạng thái Gamification và báo cáo học tập (`seed_stage`, `current_xp`, `weekly_xp`, `current_streak`, `last_study_date`, `last_watered_date`, `last_leave_date`, `discipline_score`).
6. **`feedbacks`**: Lưu đánh giá của người dùng về độ chính xác của kết quả phân tích (`is_match`).
7. **`interviews`**: Lưu toàn bộ câu hỏi phỏng vấn, câu trả lời của ứng viên và kết quả chấm điểm STAR từ AI (`evaluation_json`).
