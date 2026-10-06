# Yêu cầu kinh doanh và các giả định làm việc

## Bối cảnh kinh doanh

AlphaWave sở hữu một mạng lưới phân phối MLM đã được thiết lập và mong muốn cung cấp một sản phẩm tài chính thông qua mạng lưới này. Nền tảng dự kiến bao gồm:

- đăng ký Thành viên (Member) và ghi nhận người bảo trợ;
- ví hoặc smart account (tài khoản thông minh);
- Khoản nạp (Deposit) và rút tiền bằng crypto;
- một sản phẩm hiện được gọi là "staking", với cơ chế vận hành chưa được xác định;
- cây phả hệ MLM và các kế hoạch trả thưởng (compensation plan) có thể cấu hình;
- công cụ quản trị và hỗ trợ khách hàng;
- nạp tiền fiat, trong bản phát hành đầu tiên hoặc ở giai đoạn sau.

Một công ty giao dịch liên kết là QUANT đã xây dựng một MVP bao gồm chức năng đăng ký và tạo smart account, và dự định kết nối một công cụ giao dịch với Hyperliquid. Các năng lực của QUANT chưa được xác minh độc lập. Cyclone là công ty triển khai và giữ vai trò dẫn dắt về công nghệ. Cyclone ưu tiên mua phần mềm lõi và tích hợp thay vì tự xây dựng các hệ thống lõi.

Chưa có khu vực pháp lý hoạt động, pháp nhân hay thị trường mục tiêu nào được xác nhận. Do đó, báo cáo này trung lập về khu vực pháp lý. AlphaWave sẽ làm việc với luật sư tư vấn về các nghĩa vụ pháp lý; không có nội dung nào trong báo cáo này là tư vấn pháp lý, và không phần mềm hay chứng nhận nào của nhà cung cấp hợp thức hóa mô hình kinh doanh.

## Các yêu cầu theo cách hiểu của nhóm tư vấn

Tài liệu yêu cầu sản phẩm (PRD) và bản tổng quan kế hoạch trả thưởng của Khách hàng được xem là tuyên bố về ý định kinh doanh, chứ không phải là các đặc tả đã được thẩm định. Phạm vi dưới đây phản ánh các tài liệu đó và các quyết định đã được đưa ra trong quá trình nghiên cứu.

| Lĩnh vực | Bản phát hành đầu tiên | Các giai đoạn sau |
|---|---|---|
| Đăng ký | Đăng ký, ghi nhận người bảo trợ, liên kết giới thiệu, chế độ xem tuyến dưới đảm bảo quyền riêng tư | Chiến dịch, học viện, trò chơi hóa |
| Ví | Ví nhúng (embedded wallet) thuộc sở hữu của Thành viên; ví treasury riêng của nhà vận hành | Bổ sung chuỗi và tài sản |
| Khoản nạp | Chỉ bằng crypto, với các tài sản và mạng lưới do các thành phần được chọn hỗ trợ | On-ramp fiat, tùy thuộc vào sự chấp thuận của nhà cung cấp và rà soát pháp lý |
| Rút tiền | Crypto về địa chỉ ví bên ngoài của chính Thành viên | Off-ramp fiat |
| Sản phẩm sinh lợi (Yield Product) | Không vận hành với tiền thật; adapter trung lập với nhà cung cấp và bản trình diễn chỉ đọc hoặc trên mạng thử nghiệm (testnet) | Vault cho vay (lending) hoặc Staking thông qua một nhà cung cấp cụ thể, sau khi có xác nhận pháp lý |
| MLM | Cây bảo trợ (Sponsor Tree), kế hoạch trả thưởng được cấu hình trong công cụ đã mua, tính Hoa hồng tách biệt với chi trả, được kiểm thử theo các tình huống đã xác định | Kế hoạch đầy đủ, mô phỏng, chiến dịch |
| Vận hành | Back office quản trị với phân quyền, phê duyệt và nhật ký kiểm toán; helpdesk | CRM, phân tích nâng cao |
| Giao dịch | Không có | Tích hợp QUANT qua Hyperliquid, kèm các giới hạn (Phương án 3) |

## Các giả định làm việc

Các giả định sau đây là nền tảng cho các khuyến nghị. Mỗi giả định có khả năng làm thay đổi đáng kể kết quả đều được nêu tại mục 11 như một quyết định dành cho Khách hàng.

1. **Cyclone dẫn dắt về công nghệ** và đóng vai trò đơn vị tích hợp phần mềm lõi được mua. Các công cụ tính hoa hồng tự xây dựng, bao gồm cả công cụ của QUANT, bị loại trừ.
2. **Thiết kế trung lập về khu vực pháp lý.** Các cơ chế kiểm soát được thiết kế để có thể kích hoạt theo chính sách sau khi luật sư tư vấn xác định các nghĩa vụ.
3. **Privy là kịch bản cơ sở cho ví của Thành viên**, không sử dụng bất kỳ tính năng nào do Stripe hoặc Bridge hậu thuẫn.
4. **KYC phân tầng (kịch bản B) là kịch bản cơ sở** cho việc ước tính công cụ và chi phí (xem mục 3.5).
5. **Cơ sở tính hoa hồng còn bỏ ngỏ.** Bản tổng quan kế hoạch trả thưởng trả Hoa hồng dựa trên doanh số gói thuê bao (subscription), nhưng mô hình đó đã bị thay thế. Báo cáo này trình bày các cơ sở tính mà phần mềm thực tế hỗ trợ cùng các rủi ro cấu trúc của chúng; Khách hàng cần xác nhận cơ sở tính.
6. **Ưu tiên nền tảng web.** Chính PRD đã loại ứng dụng di động độc lập khỏi bản phát hành đầu tiên.
7. **Quy mô thí điểm** cho mục đích tính chi phí: tối đa 3,000 Thành viên có phát sinh hoa hồng, dưới 10,000 người dùng ví hoạt động hằng tháng và khoảng 1,000 Thành viên mới mỗi tháng.

## Các mâu thuẫn trong tài liệu tham chiếu

Khi các tài liệu mâu thuẫn với nhau, bản yêu cầu nghiên cứu (research brief) được ưu tiên áp dụng. Các mâu thuẫn và giả định chưa được giải quyết sau đây đã được ghi nhận:

| # | Chủ đề | Nhận xét | Cách xử lý trong báo cáo này |
|---|---|---|---|
| 1 | Tình trạng của PRD | PRD tự gọi mình là "final-programme draft", nhưng vẫn để ngỏ các vấn đề về lưu ký, công thức hoa hồng, tỷ lệ chi trả, ngưỡng KYC, cam kết lợi nhuận và việc lựa chọn nhà cung cấp. | Được xem là ý định không ràng buộc. |
| 2 | Thời điểm triển khai "staking" | Bản yêu cầu nghiên cứu liệt kê staking là một thành phần đề xuất; PRD đặt "Staking or Saving" vào Giai đoạn 2 và nêu rằng hạng mục này "requires a separate definition before build". | Sản phẩm sinh lợi được nghiên cứu đầy đủ nhưng không vận hành trong Release 1. |
| 3 | KYC | Khách hàng giả định rằng Khoản nạp bằng crypto không cần KYC. PRD để ngỏ vấn đề KYC và đặt điều kiện là phải có phê duyệt pháp lý; kế hoạch trả thưởng yêu cầu KYC từ cấp bậc Certified Leader trở lên. | Giả định được xem là chưa xác minh; KYC phân tầng là kịch bản cơ sở. |
| 4 | Cơ sở tính hoa hồng | Kế hoạch trả thưởng chỉ chi trả dựa trên doanh số gói thuê bao. Mô hình đó sau đó đã bị thay thế và cơ sở tính mới chưa được xác định. | Các cơ sở tính được so sánh dựa trên bằng chứng; cần có quyết định (mục 11). |
| 5 | Tình trạng xây dựng | Kế hoạch trả thưởng nêu rằng công cụ tính "fully built into the system" và đang tắt; PRD nêu rằng chưa có công thức nào được phê duyệt. Bản yêu cầu nghiên cứu nêu rằng Cyclone ưu tiên mua. | Loại trừ các công cụ tự xây dựng; khuyến nghị sử dụng công cụ mua sẵn. |
| 6 | Tính toán trong kế hoạch | Thiếu tỷ lệ cho các tầng 2–10, nên không thể đối chiếu tổng mức chi trả với mức trần (cap) 30% trên mỗi giao dịch bán đã nêu. Chưa rõ khoản thưởng tương ứng (leadership match) cho cấp lãnh đạo có được tính vào mức trần hay không. | Được liệt kê thành các câu hỏi dành cho Khách hàng. |
| 7 | QUANT và Hyperliquid | Là trọng tâm của bản yêu cầu nghiên cứu nhưng không xuất hiện trong tài liệu của Khách hàng. | QUANT chỉ được xem là hạng mục tích hợp Giai đoạn 2. |
| 8 | Độ rộng phạm vi | Lộ trình trong PRD bao gồm quyền chọn nhị phân (binary options), B-Book, thẻ ghi nợ và các sản phẩm quỹ. | Không nghiên cứu; được đánh dấu là các hạng mục có độ nhạy cảm cao ở giai đoạn sau. |
| 9 | Điều kiện xét cấp bậc dựa trên tuyển mộ | Cấp bậc phụ thuộc vào số lượng người được giới thiệu đã xác minh và số người đăng ký đang hoạt động, đồng thời các cấp bậc lãnh đạo yêu cầu "plan tier 7 or higher". | Được nêu để rà soát pháp lý dưới dạng một nhận xét, không phải một kết luận. |
