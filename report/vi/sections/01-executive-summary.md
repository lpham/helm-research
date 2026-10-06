# Tóm tắt điều hành và định hướng đề xuất

## Mục đích

AlphaWave dự định cung cấp một sản phẩm tài chính dựa trên crypto thông qua mạng lưới tiếp thị đa cấp (MLM) sẵn có của mình. Báo cáo này xác định cách thức nhanh nhất và đáng tin cậy để xây dựng bản phát hành đầu tiên từ các phần mềm hiện có. Báo cáo bao quát các nhà cung cấp (vendor) MLM và CRM, hạ tầng ví và lưu ký (custody), các cổng on-ramp fiat, các phương án Sản phẩm sinh lợi (Yield Product) và công cụ tuân thủ, đồng thời đề xuất một kiến trúc, một khung chi phí và phạm vi công việc cho 30 ngày.

Nghiên cứu được thực hiện dưới dạng nghiên cứu tài liệu vào ngày 6 tháng 10 năm 2026. Không có nhà cung cấp nào được liên hệ và không có tài khoản nào được mở. Mọi nhận định quan trọng đều được gắn nhãn là đã xác minh, tuyên bố của nhà cung cấp, giả định làm việc hoặc chưa xác minh (xem mục 12).

## Định hướng đề xuất

**Phương án chính: kiến trúc mô-đun (Phương án 2).** AlphaWave mua từng năng lực cốt lõi từ một nhà cung cấp chuyên biệt, và Cyclone tích hợp các thành phần này phía sau một trải nghiệm Thành viên (Member) thống nhất và một back office quản trị duy nhất:

- **Lõi MLM:** một công cụ tính hoa hồng (commission engine) dạng headless và Cây bảo trợ (Sponsor Tree). MLM Soft là ứng viên hàng đầu, với Exigo là phương án thay thế để trình diễn song song.
- **Ví của Thành viên:** ví nhúng (embedded wallet) Privy, thuộc sở hữu của Thành viên, không sử dụng bất kỳ tính năng nào của Privy phụ thuộc vào Stripe hoặc Bridge.
- **Ví treasury của nhà vận hành:** một ví riêng biệt, áp dụng phê duyệt nhiều người đối với các khoản chi trả hoa hồng.
- **Sổ cái và back office:** thuộc sở hữu của Cyclone. Sổ cái là nguồn dữ liệu gốc duy nhất về tài chính.
- **Công cụ tuân thủ:** KYC phân tầng (Sumsub hoặc Didit) và sàng lọc danh sách trừng phạt đối với mọi địa chỉ ví ngay từ ngày đầu.
- **Vận hành chăm sóc khách hàng:** một helpdesk SaaS (Zendesk hoặc Freshdesk) liên kết với back office; CRM được hoãn lại.
- **Sản phẩm sinh lợi:** một adapter trung lập với nhà cung cấp, được xây dựng ngay từ bây giờ và kích hoạt sau, trong đó Privy Earn (vault Morpho hoặc Aave) là lộ trình ngắn nhất.

**Phương án dự phòng: cùng thiết kế mô-đun nhưng với các thành phần khác.** Một bộ giải pháp ví độc lập với Stripe, gồm Turnkey kết hợp Alchemy Smart Wallets hoặc ZeroDev Kernel, thay thế Privy cho ví của Thành viên, còn Fireblocks, Cobo hoặc một ví multisig Safe vận hành treasury. Do Privy thuộc sở hữu của Stripe, phương án thay thế này cần được thử nghiệm song song ngay từ tuần 1. Exigo hoặc Epixel sẽ thay thế MLM Soft nếu ứng viên hàng đầu không đạt yêu cầu trong buổi trình diễn hoặc trong quá trình thẩm định (due diligence) bảo mật. Phương án white-label tích hợp (Phương án 1) không được khuyến nghị cho tiền thật, vì không ứng viên nào có tài liệu mô tả về lưu ký, thẩm quyền ký hay một nguồn lợi suất thực sự.

**QUANT (Phương án 3)** được xem là hạng mục tích hợp Giai đoạn 2, chỉ dành cho giao dịch thuật toán. Công cụ giao dịch của QUANT không phải là thành phần phụ thuộc của bản phát hành đầu tiên, và trong bản phát hành đó không có khoản tiền nào của Thành viên chịu rủi ro từ công cụ này.

## Các phát hiện chính

1. **Không nhà cung cấp MLM nào cung cấp một Sản phẩm sinh lợi thực sự.** Mọi tính năng "staking" hay "investment plan" tìm thấy đều chỉ là một tỷ lệ phần trăm do nhà vận hành tự đặt và hiển thị trên bảng điều khiển, không gắn với bất kỳ giao thức cụ thể nào. Do đó, Sản phẩm sinh lợi phải đến từ bên ngoài phần mềm MLM.
2. **Stripe, cùng hầu hết các cổng on-ramp fiat lớn, cấm các doanh nghiệp MLM.** Stripe liệt kê "Multilevel marketing services offering commission or recruitment-based sales" và "Cryptocurrency mining and staking" là các hoạt động bị cấm (cập nhật ngày 22 tháng 9 năm 2026). Coinbase, Transak, Banxa, Ramp và Bridge cũng có các điều khoản cấm tương tự. **Release 1 chỉ nên chấp nhận Khoản nạp bằng crypto**; fiat là hạng mục Giai đoạn 2 có điều kiện.
3. **Privy đáp ứng yêu cầu về ví về mặt kỹ thuật, nhưng không thông qua các tính năng do Stripe hậu thuẫn.** Các tính năng fiat, ví lưu ký và KYC của Privy chạy trên Bridge, một công ty thuộc Stripe có điều khoản cấm MLM. Các tính năng ví lõi, công cụ chính sách (policy engine) và Earn của Privy có thể sử dụng được, với điều kiện Privy chấp thuận mô hình kinh doanh bằng văn bản và đưa ra báo giá Enterprise.
4. **Tính chất lưu ký phụ thuộc vào việc ai kiểm soát quyền ký, chứ không phụ thuộc vào tên gọi.** Ví nhúng có signer (khóa ký) do nền tảng nắm giữ là mô hình kết hợp (hybrid), còn vault do nhà vận hành quản lý là mô hình lưu ký. Các chuẩn mực AML toàn cầu cũng đánh giá quyền kiểm soát theo cách tương tự.
5. **Giả định rằng Khoản nạp bằng crypto không cần KYC là không có cơ sở.** Chính kế hoạch trả thưởng của Khách hàng yêu cầu KYC đối với các cấp bậc lãnh đạo, các cổng on-ramp đều áp dụng KYC, và các khoản chi trả hoa hồng luôn xuất phát từ một ví treasury do nhà vận hành kiểm soát. KYC phân tầng là kịch bản cơ sở để lập kế hoạch, trong khi chờ ý kiến pháp lý.
6. **Cơ sở tính hoa hồng là câu hỏi kinh doanh còn bỏ ngỏ có tác động lớn nhất.** Phần mềm crypto-MLM phổ biến nhất trả Hoa hồng dựa trên Khoản nạp của Thành viên hoặc trên lợi nhuận được tính toán, vốn là những mô thức mà cơ quan quản lý gắn với mô hình Ponzi và mô hình kim tự tháp. Việc trả Hoa hồng từ doanh thu phí của nền tảng, chẳng hạn phí trên lợi suất thực, an toàn hơn về mặt cấu trúc, và tài liệu của MLM Soft cho thấy phần mềm này có thể tính toán dựa trên các khoản như vậy. Kế hoạch dựa trên gói thuê bao (subscription) trước đây đã bị thay thế, và Khách hàng cần xác nhận cơ sở tính mới.

## Có thể chấp nhận tiền thật trong vòng 30 ngày không?

**Không. Các bằng chứng hiện có không ủng hộ việc ra mắt với tiền thật trong vòng 30 ngày.** Các điều kiện tiên quyết nằm ngoài phạm vi kiểm soát của đội ngũ kỹ thuật:

- xác định tính chất pháp lý của kế hoạch trả thưởng, mô hình lưu ký và các ngưỡng KYC;
- sự chấp thuận bằng văn bản đối với mô hình MLM từ các nhà cung cấp ví, MLM và xác minh danh tính;
- một cơ sở tính hoa hồng được xác định rõ và các điều khoản của Sản phẩm sinh lợi;
- một đợt kiểm thử bảo mật độc lập đối với các luồng xử lý tiền.

**Mốc khả thi gần nhất tại ngày 30** là một hệ thống hoàn chỉnh từ đầu đến cuối trên mạng thử nghiệm (testnet) (đăng ký, Cây bảo trợ, ví, Khoản nạp, rút tiền, tính Hoa hồng và chi trả từ treasury, các tầng KYC, phê duyệt quản trị và helpdesk), cùng với việc các hợp đồng với nhà cung cấp và các câu hỏi pháp lý đang được xử lý. Một đợt thí điểm có kiểm soát với tiền thật là khả thi trong khoảng **10–14 tuần** kể từ khi bắt đầu, nếu nhận được trả lời pháp lý trong vòng bốn đến sáu tuần (ước tính của tư vấn).

## Chi phí tham khảo (phần mềm và dịch vụ bên ngoài)

| Hạng mục | Thấp | Cơ sở | Cao |
|---|--:|--:|--:|
| Một lần (thiết lập, kiểm thử bảo mật) | $32,000 | $65,000 | $100,000 |
| Vận hành hằng tháng (quy mô thí điểm) | $2,900 | $8,200 | $17,800 |
| Tổng tham khảo 12 tháng | $67,000 | $163,000 | $314,000 |

Khối lượng triển khai vào khoảng **9 người-tháng** cho mốc 30 ngày và khoảng **22 người-tháng** lũy kế cho đến đợt thí điểm có kiểm soát. Đơn giá của Cyclone đã được quy định trong hợp đồng, vì vậy khối lượng công việc chỉ được thể hiện bằng người-tháng. Mục 7 trình bày chi tiết và tình trạng bằng chứng của từng số liệu.

## Những gì có thể quyết định ngay và những gì cần làm thêm

| Tình trạng | Hạng mục |
|---|---|
| **Quyết định ngay** | Định hướng kiến trúc mô-đun. Chỉ nhận Khoản nạp bằng crypto trong Release 1. Ví treasury riêng của nhà vận hành với phê duyệt nhiều người. Sổ cái do Cyclone sở hữu là nguồn dữ liệu gốc về tài chính. Triển khai helpdesk trước CRM. Ưu tiên nền tảng web. Không có khoản tiền nào của Thành viên chịu rủi ro từ QUANT trong Release 1. Không sử dụng các mô-đun "ROI" chỉ mang tính hiển thị. |
| **Cần nhà cung cấp trình diễn hoặc báo giá** | Buổi demo theo kịch bản của MLM Soft và Exigo dựa trên các tình huống kiểm thử của Helm. Giá gói Enterprise của Privy và văn bản chấp thuận mô hình MLM. Thử nghiệm kỹ thuật nhanh (spike) Turnkey kết hợp Alchemy hoặc ZeroDev làm phương án ví thay thế độc lập với Stripe. Nhà cung cấp treasury (key quorum của Privy, Cobo hoặc Fireblocks). Giá của nhà cung cấp KYC. Dùng thử helpdesk. |
| **Cần thẩm định kỹ thuật** | Bằng chứng bảo mật của MLM Soft (chưa công bố). Cấu hình công cụ chính sách của Privy và tình trạng kiểm toán của lớp bọc thu phí (fee wrapper). Tiêu chí lựa chọn vault cho Sản phẩm sinh lợi trong tương lai. Công cụ giao dịch, lưu ký và cơ chế kiểm soát của QUANT (Giai đoạn 2). |
| **Cần xác nhận pháp lý** | Cơ sở tính hoa hồng. Phân loại lưu ký của mô hình ví kết hợp. Các ngưỡng KYC và Travel Rule. Tính chất pháp lý của Sản phẩm sinh lợi. Các khu vực pháp lý mục tiêu và pháp nhân vận hành. |
