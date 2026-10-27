# Nhật ký Phát triển & Thay đổi (Changelog: 20/10/2026 – 27/10/2026)

Tài liệu này ghi nhận chi tiết quá trình xây dựng, phát triển tính năng, sửa lỗi và hoàn thiện đóng gói của dự án **AI Career Coach: Trợ lý định hướng nghề nghiệp và luyện phỏng vấn thông minh** từ ngày **20/10/2026** đến ngày ra mắt **Bản phát hành đầu tiên (27/10/2026)**.

---

## [27/10/2026] — Hoàn thiện Log AI, Tái cấu trúc Thư mục, Đóng gói Docker & Phát hành Bản đầu tiên

### Thêm mới (Added)
- **Hệ thống ghi nhật ký Model AI toàn diện (Check Logs)**: Bổ sung log trực tiếp kèm thời gian xử lý và dữ liệu đầu ra tại tất cả các hàm gọi `qwen3.5:4b` (`[AI MODEL CALL]`, `[AI CV EXTRACT]`, `[AI JD EXTRACT]`, `[AI JD ADVANCED EXTRACT]`, `[AI SKILL MATCH]`, `[AI STUDY PLAN]`, `[AI INTERVIEW GENERATE]`, `[AI INTERVIEW EVALUATE]`) để theo dõi qua lệnh `docker compose logs -f backend`.
- **Chuẩn hóa hồ sơ dự án nguồn mở & Bản quyền SPDX**:
  - Gắn định danh `SPDX-License-Identifier: MIT` vào dòng đầu tiên của toàn bộ các tệp mã nguồn (`.py`, `.js`, `.css`, `.sh`) kèm công cụ kiểm tra tự động `scripts/add_spdx_headers.sh`.
  - Hoàn thiện bộ tài liệu `LICENSE`, `docs/INSTALL.md`, `docs/ARCHITECTURE.md`, `docs/API.md`, `docs/CONTRIBUTING.md`, `docs/THIRD_PARTY_LICENSES.md`, `docs/RELEASE_ANNOUNCEMENT.md` và `Makefile` chuẩn GNU Make (`make install`, `make build`, `make logs`, `make check-model`, `make uninstall`).
- **Tái cấu trúc cây thư mục dự án**: Phân nhóm toàn bộ tệp vào 5 thư mục chuyên biệt (`.github/`, `back_end/`, `front_end/`, `docs/`, `scripts/`) và chuẩn hóa 100% dấu xuống dòng Unix (`LF`).

### Sửa lỗi (Fixed)
- **Tách biệt triệt để dữ liệu `localStorage` giữa các tài khoản**: Xóa sạch các khóa trạng thái gắn theo ID (`analysis_done_${profileId}`, `analysis_data_${profileId}`, `has_analyzed_${profileId}`) và làm mới lộ trình trên giao diện ngay khi người dùng đăng xuất hoặc chuyển đổi tài khoản.
- **Sửa lỗi kẹt màn hình chờ (Skeleton Loading)**: Tự động ẩn `gapSkeletonLoading` trong khối `catch` khi quá trình phân tích độ khớp gặp sự cố kết nối.

---

## [26/10/2026] — Đồng bộ Song ngữ Anh – Việt (CV & Phỏng vấn) & Khắc phục Lỗi Logic

### Thêm mới (Added)
- **Đồng bộ ngôn ngữ trích xuất CV 2 chiều (Tiếng Việt & Tiếng Anh)**: Tự động nhận diện ngôn ngữ của tệp CV tải lên; khi tải CV Tiếng Anh sẽ trả về 100% kỹ năng chuyên môn và kỹ năng mềm bằng Tiếng Anh, khi tải CV Tiếng Việt sẽ trả về 100% bằng Tiếng Việt (giữ nguyên tên công nghệ và chứng chỉ quốc tế như Python, React, Excel, MISA, HACCP).
- **Cơ chế hoàn trả Thẻ Nghỉ Phép thông minh**: Chặn sử dụng thẻ nghỉ phép nếu trong ngày đã hoàn thành bài học; tự động hoàn trả lại thẻ nghỉ phép tuần (`1/1`) và mở khóa lại các bài học còn lại trong ngày (`excused` -> `active`) nếu học viên đổi ý vào học trong ngày đã xin nghỉ.

### Sửa lỗi (Fixed)
- **Khắc phục lỗi tải CV lần đầu không hiển thị kỹ năng lên giao diện**: Cấu hình `expire_on_commit=False` trên `SessionLocal` của SQLAlchemy và đồng bộ lại biến trạng thái hồ sơ ngay sau khi API `/profiles/extract-cv/` phản hồi.
- **Khắc phục lỗi khớp nhầm từ khóa ngắn vào từ dài**: Chặn việc đối sánh chuỗi con đối với các kỹ năng có độ dài ngắn (`"C"`, `"R"`, `"AI"`, `"BI"`, `"Git"`, `"Java"`, `"Go"`) để không bị nhận diện nhầm vào `"Excel"`, `"Digital"`, `"Email"`, `"JavaScript"`.
- **Khắc phục lỗi chọn phút `00` khi thiết lập lịch rảnh**: Thay thế toán tử `||` bằng `Number.isNaN()` khi đọc giá trị giờ/phút để không bị nhảy từ phút `00` sang phút `30`.

---

## [25/10/2026] — Hệ thống Gamification (Mầm cây Tri thức), Chuỗi Streak & Cập nhật Lịch rảnh

### Thêm mới (Added)
- **Nuôi trồng Mầm cây tri thức 6 giai đoạn (`/gamification/{profile_id}`)**: Thiết kế đồ họa SVG 6 cấp độ phát triển của cây gắn liền với tổng XP mục tiêu của cả lộ trình: `(Tổng số bài học × 50 XP) + (Số ngày của lộ trình × 25 XP tưới cây)`, hỗ trợ tăng nhiều cấp liên tiếp khi nhận lượng lớn XP.
- **Tính năng Tưới cây hàng ngày & Thẻ Nghỉ Phép tuần**:
  - API `/gamification/water-plant/{profile_id}` thưởng +25 XP mỗi ngày một lần.
  - API `/gamification/use-leave-pass/{profile_id}` cho phép sử dụng 1 phiếu nghỉ phép/tuần vào ngày có lịch học để bảo vệ chuỗi Streak và chỉ số kỷ luật.
- **Cập nhật lịch rảnh giữ nguyên lộ trình (`POST /study-plan/update-schedule`)**: Cho phép người học thay đổi khung giờ rảnh hàng tuần và tự động phân bổ lại các bài học chưa hoàn thành mà không làm mất các bài đã học hay chuỗi Streak hiện tại.

---

## [24/10/2026] — Phòng Phỏng vấn Thử AI Đa vòng & Chấm điểm theo Mô hình STAR

### Thêm mới (Added)
- **Sinh câu hỏi phỏng vấn ngẫu nhiên đa vòng (`POST /interview/generate`)**:
  - Hỗ trợ 4 vòng phỏng vấn chuyên biệt: *Vòng Nhân sự (HR)*, *Vòng Chuyên môn (Tech Lead)*, *Vòng Văn hóa (Culture Fit)* và *Vòng Cuối (Hiring Manager)*.
  - Hỗ trợ 2 ngôn ngữ **Tiếng Việt** và **Tiếng Anh** với phong cách xưng hô chuẩn mực doanh nghiệp (*Tôi - bạn*), mỗi lượt sinh ngẫu nhiên 3 câu hỏi mới không trùng lặp.
- **Giám khảo AI chấm điểm & Sửa bài chuẩn STAR (`POST /interview/submit-and-evaluate/{question_id}`)**:
  - Đánh giá câu trả lời trên thang điểm `1.0 – 10.0`, phân tích rõ điểm mạnh, điểm cần cải thiện và viết lại câu trả lời mẫu hoàn chỉnh theo cấu trúc **STAR (Situation - Task - Action - Result)**.
  - Lưu trữ toàn bộ lịch sử phỏng vấn vào bảng `interviews` (`/interview/history/{profile_id}`).
  - Giao diện phòng thi ẩn gợi ý STAR trước khi nộp bài và chỉ mở khóa đáp án mẫu sau khi ứng viên hoàn thành câu trả lời.

---

## [23/10/2026] — Lộ trình Học tập Cá nhân hóa & Thuật toán Băm giờ (Múi giờ `UTC+7`)

### Thêm mới (Added)
- **Sinh lộ trình học tập nhúng đích danh kỹ năng (`POST /study-plan/generate`)**: Kết hợp AI `qwen3.5:4b` và kho học liệu đa ngành để thiết kế danh sách bài học thực chiến có gắn trực tiếp tên từng kỹ năng còn thiếu vào tiêu đề bài học.
- **Thuật toán băm nhỏ thời lượng bài học theo khung giờ rảnh**: Tự động chia các bài học dài thành từng phần (`Phần 1`, `Phần 2`...) khớp vừa vặn với số phút rảnh trong từng ngày của học viên.
- **Khóa/mở bài học theo thời gian thực (`Asia/Ho_Chi_Minh - UTC+7`)**: Kiểm tra chính xác giờ mở khóa (`unlock_time`) tại API `/study-plan/complete-task`, tự động ẩn các khung giờ đã qua khi chọn lịch học cho ngày hôm nay (`isToday`).

---

## [22/10/2026] — Phân tích Độ khớp CV - JD Đa ngành & Biểu đồ Radar Năng lực

### Thêm mới (Added)
- **Trích xuất yêu cầu từ JD tự do (`POST /jobs/extract-advanced/`)**: Hỗ trợ chọn vị trí công việc mẫu hoặc dán trực tiếp bất kỳ Mô tả công việc (JD) thực tế nào để AI trích xuất kỹ năng yêu cầu kèm câu trích dẫn bằng chứng (`evidence`) và lưu vào bảng `jobs`.
- **Phân tích khoảng trống kỹ năng (`POST /analyses/match/{profile_id}/{role_id}`)**:
  - Chấm điểm độ khớp tổng thể theo công thức trọng số: **50% Kỹ năng chuyên môn + 25% Mức độ hứng thú + 25% Kinh nghiệm thực tế**.
  - Vẽ biểu đồ Radar năng lực theo từng nhóm ngành nghề và sinh **Báo cáo Kết luận & Đánh giá chuyên sâu** đa chiều.
  - Lưu trữ lịch sử phân tích vào bảng `analyses` (`/analyses/history/{profile_id}`) và thu thập đánh giá người dùng vào bảng `feedbacks` (`/analyses/feedback`).

---

## [21/10/2026] — Tích hợp Mô hình AI `qwen3.5:4b` (Ollama) & Trích xuất CV PDF Đa ngành

### Thêm mới (Added)
- **Kết nối máy chủ AI Ollama (`qwen3.5:4b`)**: Thiết lập cơ chế tự động dò tìm container Ollama và ép kiểu phản hồi `format='json'` cho toàn bộ các tác vụ xử lý ngôn ngữ tự nhiên.
- **Bóc tách hồ sơ CV PDF & Chống tệp rác (`POST /profiles/extract-cv/`)**:
  - Đọc nội dung văn bản từ tệp `.pdf` tải lên bằng thư viện `pypdf`.
  - Tự động phát hiện và từ chối các tệp PDF không phải là CV xin việc (`is_cv: false` như hóa đơn, đề cương môn học, tài liệu ngẫu nhiên).
  - Trích xuất kỹ năng chuyên môn (`skills`), kỹ năng mềm (`soft_skills`) và số năm kinh nghiệm (`experience_years`) bao phủ hơn 15 nhóm ngành nghề (*CNTT, Dữ liệu/BA, Tài chính - Kế toán, Luật, F&B, Marketing, Nhân sự, Kinh doanh, Logistics, Kỹ thuật, Y dược, Giáo dục, Thiết kế*).

---

## [20/10/2026] — Khởi tạo Dự án, Thiết kế Cơ sở Dữ liệu 7 Bảng & Bảo mật Tài khoản

### Thêm mới (Added)
- **Khởi tạo kiến trúc hệ thống**: Thiết lập dự án với Backend **FastAPI (Python 3.11)**, Cơ sở dữ liệu **PostgreSQL 15 (`SQLAlchemy ORM`)** và Giao diện người dùng **Single Page Application (`HTML/CSS/JS` + `Node.js` static server)**.
- **Thiết kế 7 bảng Cơ sở dữ liệu (`back_end/models.py`)**:
  1. `profiles` (Hồ sơ & tài khoản người dùng)
  2. `jobs` (Vị trí công việc & kỹ năng JD trích xuất)
  3. `analyses` (Lịch sử phân tích độ khớp CV - JD)
  4. `study_tasks` (Danh sách bài học & khung giờ mở khóa)
  5. `streaks_and_reports` (Chuỗi ngày học, điểm XP, giai đoạn cây & thẻ nghỉ phép)
  6. `feedbacks` (Đánh giá phản hồi của người dùng)
  7. `interviews` (Câu hỏi, câu trả lời, điểm số & nhận xét phỏng vấn STAR)
- **Phân hệ Xác thực & Bảo mật (`/auth/register`, `/auth/login`, `/auth/verify/{profile_id}`)**:
  - Kiểm tra chặt chẽ định dạng Email và độ mạnh mật khẩu.
  - Băm mật khẩu một chiều bằng thuật toán **`SHA-256`** trước khi lưu xuống cơ sở dữ liệu.
  - Khởi tạo bộ hồ sơ mẫu (`9991`, `9992`, `9993`) tách biệt hoàn toàn với chuỗi ID tự tăng của tài khoản người dùng thật.
