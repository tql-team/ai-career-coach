# Thông báo Phát hành Phiên bản (Release Announcements)

Tài liệu này lưu trữ nội dung thông báo phát hành chính thức gửi tới **Nhóm thư công khai (Google Group: `ai-career-coach-tql@googlegroups.com`)** và trang **GitHub Releases**.

---

## Thông báo Phát hành AI Career Coach v0.2.0 (2026-10-27)

**Tiêu đề**: `[RELEASE] AI Career Coach v0.2.0 - Trích xuất CV Song ngữ (VI/EN), Log AI Toàn diện & Đóng gói Chuẩn Docker`

Xin chào cộng đồng người dùng và Hội đồng đánh giá,

Nhóm phát triển trân trọng thông báo phát hành phiên bản **AI Career Coach v0.2.0** (nâng cấp tuần tự từ phiên bản `v0.1.0`).

### Điểm mới nổi bật trong phiên bản v0.2.0:
1. **Đồng bộ hóa ngôn ngữ trích xuất CV 2 chiều (Anh – Việt)**: Tự động nhận diện ngôn ngữ CV tải lên và trả về kỹ năng chuyên môn / kỹ năng mềm theo đúng ngôn ngữ của CV.
2. **Hệ thống Log AI trực quan**: Bổ sung log chi tiết cho toàn bộ các chức năng gọi model `qwen3.5:4b` (`[AI CV EXTRACT]`, `[AI JD EXTRACT]`, `[AI SKILL MATCH]`, `[AI STUDY PLAN]`, `[AI INTERVIEW GENERATE]`, `[AI INTERVIEW EVALUATE]`).
3. **Cơ chế Thẻ Nghỉ Phép & Tách biệt Phiên Tài khoản**: Hoàn trả thẻ nghỉ phép và mở khóa lại các bài học trong ngày khi học viên đổi ý vào học; xóa sạch bộ nhớ tạm theo từng `profile_id` khi đăng xuất.
4. **Chuẩn hóa đóng gói Docker & GNU Make (`Makefile`)**: Hỗ trợ cài đặt nhanh qua `make install` hoặc `docker compose up --build -d`, kèm đầy đủ giấy phép `MIT`, `SPDX-License-Identifier: MIT` và `THIRD_PARTY_LICENSES.md`.

### Liên kết tải về và trao đổi:
* **Kho mã nguồn chính thức**: https://github.com/tql-team/ai-career-coach.git
* **GitHub Release Tag (`v0.2.0`)**: https://github.com/tql-team/ai-career-coach/releases/tag/v0.2.0
* **Website & Tài liệu trực tuyến (GitHub Pages)**: https://tql-team.github.io/ai-career-coach/
* **Báo lỗi (Bug Tracker)**: https://github.com/tql-team/ai-career-coach/issues
* **Nhóm thư thảo luận (Google Group)**: https://groups.google.com/g/ai-career-coach-tql
