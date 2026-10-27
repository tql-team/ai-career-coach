# Thông báo Phát hành (Release Announcement)

Tài liệu này lưu trữ nội dung thông báo phát hành chính thức gửi tới **Nhóm thư công khai (Google Group: `ai-career-coach-tql@googlegroups.com`)** và trang **GitHub Releases**.

---

## Thông báo Phát hành Đầu tiên — AI Career Coach: Trợ lý định hướng nghề nghiệp và luyện phỏng vấn thông minh

**Tiêu đề**: `[RELEASE] Bản phát hành đầu tiên - AI Career Coach: Trợ lý định hướng nghề nghiệp và luyện phỏng vấn thông minh`

Xin chào cộng đồng người dùng và Hội đồng đánh giá,

Nhóm phát triển trân trọng thông báo ra mắt **Bản phát hành đầu tiên (First Release)** của dự án **AI Career Coach: Trợ lý định hướng nghề nghiệp và luyện phỏng vấn thông minh**.

### Các tính năng cốt lõi trong bản phát hành đầu tiên:
1. **Trích xuất CV song ngữ 2 chiều (Anh – Việt) & Phân tích JD đa ngành**: Tự động nhận diện ngôn ngữ CV PDF tải lên, trả về kỹ năng chuyên môn / kỹ năng mềm tương ứng và phân tích độ khớp với JD của hơn 15 nhóm ngành nghề.
2. **Lộ trình học tập thông minh (Múi giờ `UTC+7`) & Gamification**: Tự động chia nhỏ bài học theo khung giờ rảnh, hỗ trợ cập nhật lịch rảnh giữ nguyên tiến độ, tích hợp chuỗi Streak, Thẻ nghỉ phép thông minh và nuôi trồng Mầm cây tri thức 6 giai đoạn.
3. **Phòng phỏng vấn AI đa vòng theo mô hình STAR**: Hỗ trợ phỏng vấn Tiếng Việt và Tiếng Anh qua 4 vòng với câu hỏi ngẫu nhiên từ mô hình `qwen3.5:4b`, chấm điểm và gợi ý cách trả lời chuẩn STAR, kèm hệ thống ghi log AI trực quan.
4. **Đóng gói chuẩn Docker & GNU Make (`Makefile`)**: Khởi chạy tự động toàn bộ 4 containers (`postgres_db`, `ollama`, `backend`, `frontend`) qua lệnh `make install` hoặc `docker compose up --build -d`, tuân thủ đầy đủ giấy phép nguồn mở `MIT` và định danh `SPDX-License-Identifier: MIT`.

### Liên kết tải về và trao đổi:
* **Kho mã nguồn chính thức**: https://github.com/tql-team/ai-career-coach.git
* **Trang Phát hành (GitHub Releases)**: https://github.com/tql-team/ai-career-coach/releases
* **Báo lỗi (Bug Tracker)**: https://github.com/tql-team/ai-career-coach/issues
* **Nhóm thư thảo luận (Google Group)**: https://groups.google.com/g/ai-career-coach-tql
