# Rủi ro và yêu cầu thẩm định

## Danh mục rủi ro

Khả năng xảy ra (KN) và mức độ tác động (TĐ) do Cyclone đánh giá ở mức Cao, Trung bình hoặc Thấp đối với Phương án 2 được khuyến nghị.

C = Cao, TB = Trung bình, T = Thấp.

| # | Rủi ro | KN | TĐ | Biện pháp giảm thiểu |
|---|---|:-:|:-:|---|
| R1 | Luật sư tư vấn kết luận kế hoạch trả thưởng (compensation plan) hoặc cơ sở tính hoa hồng là trái pháp luật tại một thị trường mục tiêu | TB | C | Quyết định sớm cơ sở tính hoa hồng; ưu tiên Hoa hồng được tài trợ từ doanh thu phí đã thực hiện, có mức trần và thời gian tạm giữ; không trả Hoa hồng trên Khoản nạp cho đến khi luật sư tư vấn xác nhận |
| R2 | Một nhà cung cấp từ chối hoặc sau đó chấm dứt quan hệ kinh doanh vì mô hình MLM (ví, KYC, thanh toán) | C | C | Công bố đầy đủ trong quá trình tiếp nhận; có văn bản chấp thuận trước khi công việc xây dựng phụ thuộc vào nhà cung cấp đó; các thành phần có thể thay thế đặt sau giao diện của Cyclone; đã xác định nhà cung cấp dự phòng |
| R3 | Mô hình ví kết hợp (hybrid) (có signer của nền tảng) bị phân loại là lưu ký hoặc chuyển tiền | TB | C | Release 1 không có signer của nền tảng trên ví Thành viên; chỉ bổ sung signer có phạm vi giới hạn sau khi có ý kiến của luật sư tư vấn; phương án thay thế là key quorum có chữ ký của Thành viên |
| R4 | Khóa của treasury hoặc signer của nền tảng bị xâm phạm | T | C | Phê duyệt theo quorum; HSM hoặc KMS; chính sách chặt chẽ; tách biệt khóa; hạn mức rút; rà soát ví trước khi ra mắt |
| R5 | MLM Soft không vượt qua thẩm định bảo mật hoặc không hỗ trợ được kế hoạch | TB | TB | Demo song song với Exigo; bộ kiểm thử theo kịch bản; yêu cầu bằng chứng SOC 2, ISO 27001:2022 hoặc kiểm thử xâm nhập trước khi ký hợp đồng |
| R6 | Sai sót hoặc tranh chấp về Hoa hồng (tỷ lệ, nén tầng, đảo ngược) | TB | C | Đặc tả đầy đủ; bộ kiểm thử; diễn giải cho từng Thành viên; thời gian tạm giữ trước khi chi trả; maker-checker đối với các điều chỉnh |
| R7 | Không thể thu hồi hoa hồng (clawback) sau khi đã chi trả on-chain | C | TB | Chi trả sau thời gian tạm giữ; bù trừ các khoản đảo ngược vào Hoa hồng tương lai; nêu rõ điều này trong điều khoản Thành viên |
| R8 | Gian lận thông qua Thành viên giả (tự bảo trợ, tài khoản sybil) | C | TB | KYC theo cấp trước khi chi trả; tín hiệu về thiết bị và hành vi; mức trần; quy tắc về điều kiện hưởng Hoa hồng |
| R9 | Chênh lệch đối soát giữa sổ cái, ví và chuỗi | TB | C | Hai tín hiệu Khoản nạp độc lập; tính lũy đẳng (idempotency) theo mã định danh giao dịch; đối soát hằng ngày, chặn chi trả khi còn chênh lệch chưa xử lý |
| R10 | Tổn thất từ giao thức sinh lợi (hợp đồng thông minh, oracle, curator, thanh khoản) khi Sản phẩm sinh lợi (Yield Product) đi vào vận hành | TB | C | Danh sách vault được phép kèm tiêu chí về curator; mức trần rủi ro; công tắc dừng khẩn (kill switch); công bố thông tin cho Thành viên theo từng nhóm; không hiển thị lợi suất dự kiến |
| R11 | Thành viên hiểu sai về lợi suất hoặc dựa vào các tuyên bố quảng cáo về thu nhập | C | C | Nội dung được bộ phận tuân thủ rà soát; không cam kết lợi suất; công bố thông tin về thu nhập; kiểm soát nội dung tiếp thị do Thành viên tạo |
| R12 | Chi phí gas cho ví của từng Thành viên vượt ngân sách | TB | T | Chọn mạng phí thấp; chi trả theo lô; giới hạn tài trợ phí |
| R13 | Chậm trễ trong rà soát pháp lý hoặc tiếp nhận của nhà cung cấp đẩy đợt thí điểm vượt kế hoạch | C | TB | Khởi động cả hai ngay trong tuần 1; coi đây là đường găng; giữ các mốc kỹ thuật độc lập với hai yếu tố này |
| R14 | Phụ thuộc vào Privy, công ty thuộc sở hữu của Stripe: điều khoản của Privy có thể được điều chỉnh theo lệnh cấm MLM của Stripe | TB | C | Không sử dụng tính năng nào của Stripe hoặc Bridge; xác nhận chấp thuận bằng văn bản; lớp ví đặt sau giao diện của Cyclone; cho phép Thành viên xuất khóa; kiểm thử song song Turnkey kết hợp Alchemy Smart Wallets hoặc ZeroDev Kernel làm phương án thay thế độc lập |
| R15 | Tích hợp QUANT khiến tiền của Thành viên chịu rủi ro thua lỗ giao dịch | T (Release 1) | C | Không cho phép truy cập QUANT trong Release 1; Giai đoạn 2 chỉ thông qua tài khoản chỉ được giao dịch, có mức trần, do Thành viên chủ động đăng ký, sau khi thẩm định |

## Yêu cầu thẩm định

**Nhà cung cấp MLM (trước khi ký hợp đồng):**

- Báo cáo SOC 2 Type II hoặc chứng chỉ ISO/IEC 27001:2022 hiện hành, kèm phạm vi và kỳ đánh giá; bản tóm tắt kiểm thử xâm nhập gần nhất và tình trạng khắc phục.
- Demo theo kịch bản đối với bộ kiểm thử Helm, bao gồm cơ sở tính hoa hồng không dựa trên đơn hàng được gửi qua API, quản lý phiên bản kế hoạch, mô phỏng, đảo ngược và diễn giải cho từng Thành viên.
- Xuất dữ liệu phả hệ, lịch sử kế hoạch và lịch sử Hoa hồng; điều khoản chấm dứt hợp tác.
- Xác thực API, giới hạn tần suất gọi, quản lý phiên bản, ký webhook và cơ chế gửi lại; quyền truy cập sandbox.

**Nhà cung cấp ví và treasury:**

- Văn bản chấp thuận mô hình MLM và xác nhận rằng các tính năng ví cốt lõi không yêu cầu tài khoản Stripe hoặc Bridge (Privy).
- Giá Enterprise; báo cáo SOC 2; năng lực của công cụ chính sách (policy engine); cơ chế xuất khóa và lộ trình chuyển đổi.
- Tình trạng kiểm toán của lớp bọc thu phí Earn (Earn fee wrapper) và mọi hợp đồng mà nền tảng sẽ phụ thuộc vào.

**Nhà cung cấp dịch vụ xác minh:** chấp thuận mô hình; các chứng nhận; nơi lưu trữ dữ liệu; thời hạn lưu giữ hồ sơ; sự cố hệ thống hỗ trợ năm 2024 mà Sumsub đã công bố ([thông báo của Sumsub](https://sumsub.com/newsroom/security-incident-update/)).

**Nhà cung cấp sinh lợi (giai đoạn sau):** lịch sử kiểm toán, lịch sử sự cố và khắc phục, khung quản trị rủi ro của curator, đặc điểm thanh khoản và các tác động về lưu ký của mô hình tích hợp.

**QUANT (Giai đoạn 2):** rà soát kỹ thuật độc lập đối với engine, mô hình lưu ký, các biện pháp kiểm soát bảo mật, mức độ sẵn sàng vận hành, phương pháp đo lường hiệu quả lịch sử và lịch sử sự cố. Các năng lực MVP của QUANT chưa được xác minh trong nghiên cứu này.
