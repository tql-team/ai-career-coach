# Đặc tả REST API & Nhật ký Model AI (API & AI Logging Reference)

Khi hệ thống đang chạy, bạn có thể truy cập trực tiếp giao diện Swagger UI tại **[http://localhost:8000/docs](http://localhost:8000/docs)** để thử nghiệm toàn bộ 20 endpoints.

---

## 1. Danh sách 20 REST API Endpoints

### Phân hệ Xác thực & Hồ sơ (`Auth & Profiles`)
* `POST /auth/register`: Đăng ký tài khoản mới (kiểm tra định dạng Email, mật khẩu tối thiểu 6 ký tự, chặn mật khẩu yếu và băm `SHA-256`).
* `POST /auth/login`: Đăng nhập tài khoản và trả về `profile_id`.
* `GET /auth/verify/{profile_id}`: Kiểm tra tính hợp lệ của phiên đăng nhập trong Database.
* `POST /profiles/extract-cv/`: Kiểm tra tính hợp lệ của CV (`is_cv`) và trích xuất kỹ năng chuyên ngành, kỹ năng mềm theo đúng ngôn ngữ của CV (`vi` hoặc `en`).

### Phân hệ Phân tích Độ khớp CV – JD (`Jobs & Skill Gap Analysis`)
* `POST /jobs/extract-advanced/`: Trích xuất kỹ năng kèm trích dẫn bằng chứng từ văn bản JD.
* `POST /analyses/match/{profile_id}/{role_id}`: Đối sánh kỹ năng ứng viên với JD mẫu hoặc JD dán tự do, tính điểm trọng số và tạo báo cáo kết luận chuyên sâu.
* `POST /analyses/feedback`: Ghi nhận phản hồi đánh giá độ chính xác của kết quả phân tích.
* `GET /analyses/history/{profile_id}`: Lấy lịch sử các lần phân tích JD/CV của học viên.

### Phân hệ Lộ trình Học tập & Gamification (`Study Plan & Gamification`)
* `POST /study-plan/generate`: Tạo lộ trình học tập mới nhúng đích danh tên kỹ năng cần cải thiện và băm vào các khung giờ rảnh (`UTC+7`).
* `POST /study-plan/update-schedule`: Cập nhật lịch rảnh mới và xếp lại các bài chưa học nhưng giữ nguyên lộ trình, tiến độ và chuỗi Streak.
* `GET /study-plan/schedules/{profile_id}`: Lấy danh sách khung giờ rảnh đã lưu.
* `GET /study-plan/tasks/{profile_id}`: Lấy danh sách các bài học trong lộ trình.
* `POST /study-plan/complete-task`: Hoàn thành bài học, cộng `+50 XP`, cập nhật Streak (và tự động hoàn trả thẻ nghỉ phép nếu hoàn thành bài trong ngày đã xin nghỉ).
* `GET /gamification/{profile_id}`: Lấy thông số XP, giai đoạn Mầm cây (1–6), Streak, Thẻ nghỉ phép (`leave_pass_remaining`) và chỉ số kỷ luật.
* `POST /gamification/water-plant/{profile_id}`: Tưới cây mỗi ngày một lần (`+25 XP`).
* `POST /gamification/use-leave-pass/{profile_id}`: Sử dụng Thẻ nghỉ phép (tối đa 1 lần/tuần vào ngày có lịch học, chưa học bài nào trong ngày).

### Phân hệ Phỏng vấn AI theo mô hình STAR (`AI Interview`)
* `POST /interview/generate`: Sinh bộ 3 câu hỏi phỏng vấn ngẫu nhiên không trùng lặp theo vị trí, cấp độ, vòng phỏng vấn và ngôn ngữ (`vi` / `en`).
* `POST /interview/submit-and-evaluate/{question_id}`: Chấm điểm câu trả lời phỏng vấn (`1.0 – 10.0`), đưa ra nhận xét và đáp án mẫu chuẩn STAR.
* `GET /interview/history/{profile_id}`: Xem lịch sử các phiên phỏng vấn đã chấm điểm.
* `DELETE /system/reset-database/`: Khởi tạo lại toàn bộ các bảng cơ sở dữ liệu phục vụ kiểm thử.

---

## 2. Các Nhãn Nhật ký Model AI (`docker compose logs -f backend`)

Mọi lời gọi tới mô hình `qwen3.5:4b` đều được ghi log trực tiếp với các nhãn chuẩn hóa:
* `[AI MODEL CALL]`: Thời gian phản hồi và địa chỉ máy chủ Ollama.
* `[AI CV EXTRACT]`: Ngôn ngữ CV phát hiện (`VI`/`EN`), JSON gốc của AI, danh sách kỹ năng chuyên môn và kỹ năng mềm.
* `[AI JD EXTRACT]` & `[AI JD ADVANCED EXTRACT]`: Kết quả bóc tách kỹ năng từ văn bản JD tự do.
* `[AI SKILL MATCH]`: Điểm số tổng hợp, kỹ năng đã đạt và kỹ năng còn thiếu.
* `[AI STUDY PLAN]`: Danh sách bài học được AI thiết kế cho từng kỹ năng hổng.
* `[AI INTERVIEW GENERATE]` & `[AI INTERVIEW EVALUATE]`: Bộ 3 câu hỏi phỏng vấn và kết quả chấm điểm STAR kèm XP thưởng.
