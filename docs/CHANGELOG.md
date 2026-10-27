# Lịch sử Thay đổi & Phát hành (Changelog)

Mọi thay đổi đáng chú ý của dự án **AI Career Coach** đều được ghi chép đầy đủ tại tệp này.

Định dạng tài liệu tuân thủ chuẩn [Keep a Changelog](https://keepachangelog.com/vi/1.0.0/), và hệ thống đánh số phiên bản tuân thủ nghiêm ngặt quy tắc **Phiên bản ngữ nghĩa tuần tự `Major.Minor.Patch` ([Semantic Versioning](https://semver.org/lang/vi/))**: `v0.1.0` -> `v0.2.0`.

---

## [v0.2.0] - 2026-10-27

### Thêm mới (Added)
- **Trích xuất CV song ngữ tự động (Tiếng Việt & Tiếng Anh)**: Tự động nhận diện ngôn ngữ CV tải lên; nếu CV Tiếng Anh sẽ trả về 100% kỹ năng chuyên môn và kỹ năng mềm bằng Tiếng Anh, nếu CV Tiếng Việt sẽ chuẩn hóa 100% sang Tiếng Việt (giữ nguyên tên công nghệ quốc tế như Python, Laravel, Excel, MISA, HACCP).
- **Hệ thống Log AI toàn diện (`[AI MODEL CALL]`, `[AI CV EXTRACT]`, `[AI JD EXTRACT]`, `[AI SKILL MATCH]`, `[AI STUDY PLAN]`, `[AI INTERVIEW GENERATE]`, `[AI INTERVIEW EVALUATE]`)**: Ghi nhật ký trực tiếp thời gian phản hồi và dữ liệu JSON của mô hình `qwen3.5:4b` phục vụ kiểm tra qua `docker compose logs -f backend`.
- **Cập nhật lịch rảnh giữ nguyên lộ trình (`POST /study-plan/update-schedule`)**: Cho phép học viên đổi khung giờ rảnh và tự động xếp lại các bài chưa hoàn thành mà không làm mất lộ trình hiện tại, chuỗi Streak hay tiến độ Mầm cây.
- **Cơ chế hoàn trả Thẻ Nghỉ Phép thông minh**: Chặn dùng thẻ nghỉ phép nếu trong ngày đã hoàn thành bài học; tự động hoàn trả lại thẻ nghỉ phép tuần (`1/1`) và gỡ trạng thái miễn học (`excused` -> `active`) cho các bài còn lại nếu học viên đổi ý vào học trong ngày nghỉ phép.
- **Chuẩn hóa hồ sơ dự án nguồn mở (Giảm thiểu PoF)**:
  - Bổ sung định danh `SPDX-License-Identifier: MIT` vào đầu toàn bộ tệp mã nguồn (`.py`, `.js`, `.css`, `.sh`) kèm script `add_spdx_headers.sh`.
  - Bổ sung `Makefile` (hỗ trợ `make install`, `make build`, `make up`, `make down`, `make uninstall`, `make logs`, `make check-model`), `INSTALL.md`, `CONTRIBUTING.md`, `LICENSE`, `THIRD_PARTY_LICENSES.md`, `pyproject.toml` và bộ tài liệu `docs/` phục vụ GitHub Pages.

### Sửa lỗi (Fixed)
- **Khắc phục lỗi tải CV lần đầu không hiển thị kỹ năng lên giao diện**: Thiết lập `expire_on_commit=False` trên SQLAlchemy `SessionLocal` và trả về JSON tường minh tại `/profiles/extract-cv/`.
- **Khắc phục lỗi dính dữ liệu phân tích và lộ trình khi chuyển đổi tài khoản (Bug #4 & Mục A1)**: Xóa triệt để các khóa `analysis_done_${profileId}`, `analysis_data_${profileId}`, `has_analyzed_${profileId}` và làm rỗng lộ trình trước khi xóa `current_profile_id` lúc đăng xuất.
- **Khắc phục lỗi chọn phút `00` khi xếp lịch rảnh (Mục A2)**: Sử dụng `Number.isNaN()` thay cho toán tử `||` để giữ nguyên phút `00`.
- **Khắc phục lỗi từ khóa ngắn khớp nhầm vào từ dài (Mục C1)**: Ngăn các từ ngắn như `"C"`, `"Git"`, `"AI"`, `"Java"` khớp chuỗi con vào `"Excel"`, `"Digital"`, `"Email"`, `"JavaScript"`.
- **Khắc phục lỗi kẹt màn hình chờ Skeleton khi phân tích gặp sự cố (Mục A4)**: Tự động ẩn `gapSkeletonLoading` trong khối `catch` của `startAnalysis`.

---

## [v0.1.0] - 2026-10-20

### Thêm mới (Added)
- **Kiến trúc 4 Docker Containers (`docker-compose.yml`)**: Đóng gói hoàn chỉnh PostgreSQL 15 (`career_coach_pg`), Ollama AI (`career_coach_ollama` tự động tải `qwen3.5:4b`), FastAPI Backend (`career_coach_backend`) và Node.js Frontend (`career_coach_frontend`).
- **Thiết kế Cơ sở dữ liệu 7 bảng (`SQLAlchemy ORM`)**: `profiles`, `jobs`, `analyses`, `study_tasks`, `streaks_and_reports`, `feedbacks`, `interviews`.
- **Bảo mật tài khoản người dùng**: Kiểm tra định dạng Email, độ mạnh mật khẩu và băm mật khẩu một chiều bằng thuật toán `SHA-256`; tách biệt dải ID hồ sơ mẫu (`9991`–`9993`).
- **Trích xuất kỹ năng đa ngành (15+ lĩnh vực) & Chống tệp rác**: Bóc tách CV PDF, từ chối tệp không phải CV (`is_cv: false`), đối sánh độ khớp CV - JD và vẽ biểu đồ Radar năng lực.
- **Lộ trình học tập theo múi giờ Việt Nam (`UTC+7`) & Gamification**: Băm nhỏ thời lượng bài học vào lịch rảnh, khóa/mở bài học theo giờ thực tế, tích hợp hệ thống chuỗi ngày học (Streak), Thẻ nghỉ phép (1 lần/tuần) và nuôi trồng Mầm cây tri thức 6 giai đoạn.
- **Phòng phỏng vấn AI đa vòng theo phương pháp STAR**: Hỗ trợ Tiếng Việt & Tiếng Anh với 4 phong cách người phỏng vấn, sinh câu hỏi ngẫu nhiên không trùng lặp (`format='json'`) và chấm điểm kèm đáp án mẫu chuẩn STAR.
