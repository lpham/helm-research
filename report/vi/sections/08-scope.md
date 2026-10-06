# Phạm vi 30 ngày đề xuất và tiêu chí sẵn sàng

## Định nghĩa mốc

Việc ra mắt với tiền thật trong vòng 30 ngày là không khả thi (mục 1). Do đó, mốc 30 ngày được định nghĩa như sau:

> **Một hệ thống đầu-cuối vận hành trên mạng thử nghiệm (testnet), trong đó mọi luồng tiền, quy trình phê duyệt và quy trình hỗ trợ đều hoạt động, đồng thời hợp đồng với nhà cung cấp và các câu hỏi pháp lý đang được xử lý, để một đợt thí điểm có kiểm soát (controlled pilot) bằng tiền thật có thể bắt đầu ngay khi các điều kiện về pháp lý và nhà cung cấp được đáp ứng.**

Môi trường production chỉ dành cho đăng ký (đăng ký tài khoản, ghi nhận người bảo trợ, liên kết giới thiệu và tạo ví, không có Khoản nạp) có thể được mở vào ngày 30 nếu luật sư tư vấn đồng ý rằng việc đăng ký trước không phát sinh vấn đề tại các thị trường mục tiêu.

## Kế hoạch theo tuần

| Tuần | Kết quả | Phụ trách | Phụ thuộc | Tiêu chí nghiệm thu |
|---|---|---|---|---|
| 1 – Quyết định và mua sắm | Nhật ký quyết định bao gồm cơ sở tính hoa hồng, thị trường, kịch bản KYC và người phê duyệt treasury. Demo theo kịch bản của MLM Soft và Exigo. Thử nghiệm nhanh (spike) song song về ví trên Privy và trên Turnkey kết hợp Alchemy Smart Wallets hoặc ZeroDev Kernel. Gửi văn bản đề nghị chấp thuận mô hình MLM tới Privy, Turnkey, Alchemy, ZeroDev (Offchain Labs), MLM Soft và nhà cung cấp KYC. Thuê luật sư tư vấn kèm danh sách câu hỏi. Thiết lập môi trường và kho mã nguồn. | Chủ sở hữu sản phẩm phía Khách hàng; trưởng nhóm triển khai và kiến trúc sư của Cyclone | Mức độ sẵn sàng của Khách hàng; lịch demo của nhà cung cấp | Các quyết định được phê duyệt; hoàn thành bảng chấm điểm demo và kết quả thử nghiệm ví; đã gửi bảng câu hỏi cho nhà cung cấp; xác nhận đã thuê luật sư tư vấn |
| 2 – Nền tảng | Đăng ký Thành viên, ghi nhận người bảo trợ và liên kết giới thiệu. Tạo ví Privy trên mạng thử nghiệm. Môi trường sandbox của lõi MLM với kế hoạch tạm thời. Lược đồ sổ cái và mô hình sự kiện. Khung vai trò quản trị và nhật ký kiểm toán. Tenant helpdesk và các loại hồ sơ xử lý. | Bộ phận kỹ thuật Cyclone | Quyền truy cập sandbox của MLM và Privy | Một Thành viên thử nghiệm có thể đăng ký dưới một người bảo trợ, nhận ví và xuất hiện trong Cây bảo trợ (Sponsor Tree); mọi thao tác quản trị đều được ghi log |
| 3 – Luồng tiền trên mạng thử nghiệm | Phát hiện Khoản nạp với đối soát độc lập. Rút tiền do Thành viên ký. Tính Hoa hồng từ các sự kiện thử nghiệm. Chi trả từ treasury với phê duyệt theo quorum. Sàng lọc danh sách trừng phạt trên mọi địa chỉ. Các cấp KYC trong sandbox. | Bộ phận kỹ thuật Cyclone; phụ trách tuân thủ phía Khách hàng (ngưỡng theo cấp) | Thống nhất ngưỡng tạm thời; sandbox KYC | Khoản nạp được ghi có đúng một lần, kể cả khi webhook bị trùng lặp hoặc đến chậm; chi trả cần hai người phê duyệt; một địa chỉ thử nghiệm thuộc danh sách trừng phạt bị chặn |
| 4 – Củng cố và rà soát | Bộ kiểm thử Hoa hồng (các tầng unilevel, thưởng đối ứng (matching), xét cấp bậc, nén tầng, mức trần, thay đổi phiên bản kế hoạch, đảo ngược). Quy trình xử lý sự cố và tạm ngừng dịch vụ. Công tắc dừng khẩn (kill switch). Tích hợp helpdesk và bản nháp cơ sở tri thức. Tự đánh giá bảo mật và đặt lịch kiểm thử xâm nhập. Đánh giá mức độ sẵn sàng. | QA và DevOps của Cyclone; trưởng bộ phận vận hành phía Khách hàng | Kế hoạch tạm thời đầy đủ; rà soát cơ sở tri thức | Bộ kiểm thử đạt; các quy trình được diễn tập trong một buổi diễn tập trên bàn (tabletop); phát hành báo cáo mức độ sẵn sàng kèm danh sách các điều kiện còn mở |

## Yêu cầu trước khi tiếp nhận tiền thật

Tất cả các yêu cầu dưới đây đều phải được đáp ứng. Không yêu cầu nào được miễn trừ để kịp tiến độ.

1. **Cơ chế sản phẩm và điều khoản Thành viên được xác định**, bao gồm cơ sở tính hoa hồng và đầy đủ tỷ lệ của kế hoạch, được luật sư tư vấn phê duyệt.
2. **Xác nhận pháp lý** cho các khu vực pháp lý ra mắt, bao gồm phân loại lưu ký, ngưỡng KYC, khả năng áp dụng Travel Rule và kế hoạch trả thưởng.
3. **Văn bản chấp thuận** mô hình MLM từ các nhà cung cấp ví, MLM và xác minh.
4. **Các biện pháp kiểm soát lưu ký và ký giao dịch** đã có hiệu lực: treasury tách biệt với phê duyệt theo quorum; mọi signer (khóa ký) của nền tảng đều bị giới hạn bằng chính sách và được lưu giữ trong HSM hoặc KMS; việc luân chuyển và khôi phục khóa đã được kiểm thử.
5. **Nạp và rút tiền** đã được chứng minh trên mạng thử nghiệm và trong một đợt diễn tập nhỏ bằng tiền thật sử dụng vốn của nhà vận hành.
6. **Sổ cái và đối soát hằng ngày** với số dư on-chain, trong đó các chênh lệch được điều tra trước khi chi trả.
7. **Xác minh và sàng lọc** đã vận hành theo kịch bản đã thống nhất, với sàng lọc danh sách trừng phạt trên mọi địa chỉ.
8. **Việc tính Hoa hồng đã được kiểm thử** theo bộ kiểm thử đã thống nhất, với phần diễn giải có thể xuất ra cho từng Thành viên.
9. **Phân quyền quản trị và khả năng kiểm toán**: kiểm soát truy cập theo vai trò, phê duyệt maker-checker cho mọi giao dịch luân chuyển tiền, nhật ký kiểm toán không thể sửa đổi.
10. **Ứng phó sự cố**: chế độ tạm ngừng dịch vụ và chế độ chỉ cho phép rút, xử lý giao dịch thất bại và bị treo, mẫu thông báo cho Thành viên.
11. **Kiểm thử xâm nhập và rà soát ví độc lập** đã hoàn thành, với các phát hiện mức độ nghiêm trọng cao đã được khắc phục.

## Tính năng của đợt thí điểm có kiểm soát

- Khoản nạp crypto đối với các tài sản và mạng được các thành phần đã chọn hỗ trợ; rút tiền về địa chỉ của chính Thành viên.
- Cây bảo trợ và tính Hoa hồng trên cơ sở tính hoa hồng đã được xác nhận, chi trả theo đợt sau một thời gian tạm giữ.
- KYC theo cấp và sàng lọc danh sách trừng phạt.
- Back office quản trị có quy trình phê duyệt; helpdesk với các hàng đợi về tiền, xác minh và Hoa hồng.
- Giới hạn mức độ rủi ro: danh sách Thành viên chỉ theo lời mời, mức trần cho từng Thành viên và tổng thể, cùng khả năng tạm ngừng.

## Các giai đoạn sau

- Vận hành Sản phẩm sinh lợi (Yield Product) thông qua adapter, sau khi có xác nhận pháp lý và thẩm định (due diligence) vault.
- On-ramp fiat, sau khi có văn bản phê duyệt của nhà cung cấp dịch vụ.
- Tích hợp giao dịch QUANT (Phương án 3), sau khi thẩm định.
- Lớp CRM, kênh hỗ trợ Telegram và WhatsApp, hỗ trợ bằng AI giới hạn trong phạm vi tri thức đã được phê duyệt.
- Ứng dụng di động gốc.
- Các hạng mục trong lộ trình PRD có độ nhạy cảm cao về mặt quản lý (quyền chọn nhị phân, B-Book, thẻ ghi nợ, sản phẩm quỹ), mỗi hạng mục phải được rà soát pháp lý riêng.

## Đánh giá mức độ sẵn sàng

Tình trạng dự kiến vào ngày 30 nếu các quyết định của tuần 1 được đưa ra đúng hạn:

| Tiêu chí | Tình trạng dự kiến vào ngày 30 | Có chặn việc tiếp nhận tiền thật không? |
|---|---|---|
| Cơ chế sản phẩm và điều khoản Thành viên | Đã quyết định cơ sở tính hoa hồng; điều khoản đã soạn thảo, chưa được phê duyệt | Có, cho đến khi luật sư tư vấn phê duyệt |
| Xác nhận pháp lý | Câu hỏi đã gửi luật sư tư vấn; đang chờ trả lời | **Có** |
| Kiểm soát lưu ký và ký giao dịch | Đã thiết kế và hoạt động trên mạng thử nghiệm | Có, cho đến khi được rà soát |
| Nạp và rút tiền | Hoạt động trên mạng thử nghiệm | Có, cho đến đợt diễn tập bằng tiền thật |
| Sổ cái và đối soát | Hoạt động trên mạng thử nghiệm | Có, cho đến đợt diễn tập bằng tiền thật |
| Xác minh và sàng lọc | Sandbox; ngưỡng tạm thời | Có, cho đến khi ngưỡng được phê duyệt |
| Tính Hoa hồng | Bộ kiểm thử đạt với kế hoạch tạm thời | Có, cho đến khi chạy lại với kế hoạch đã phê duyệt |
| Phân quyền quản trị và khả năng kiểm toán | Đã xây dựng và kiểm thử | Không |
| Ứng phó sự cố và tạm ngừng dịch vụ | Quy trình đã soạn thảo và diễn tập | Không, sau khi đã diễn tập |
| Kiểm thử bảo mật | Đã lên lịch | **Có** |
| Chấp thuận của nhà cung cấp | Đã gửi đề nghị | **Có** |

**Kết luận:** vào ngày 30, hệ thống cần sẵn sàng để trình diễn đầu-cuối. Hệ thống không nên được mô tả là sẵn sàng vận hành production với tiền thật cho đến khi mọi hạng mục có tính chặn nêu trên được xử lý xong.
