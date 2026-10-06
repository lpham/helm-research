# Câu hỏi dành cho nhà cung cấp, QUANT và luật sư tư vấn

## Nhà cung cấp

**Tất cả nhà cung cấp MLM trong danh sách rút gọn (MLM Soft, Exigo, Epixel, Cloud MLM)**

1. Quý công ty có ký hợp đồng với một nền tảng phân phối sản phẩm crypto thông qua mạng lưới MLM, trong đó Hoa hồng được chi trả bằng crypto hay không?
2. Đề nghị cung cấp báo cáo SOC 2 Type II hoặc chứng chỉ ISO/IEC 27001:2022 hiện hành, cùng bản tóm tắt kiểm thử xâm nhập gần nhất kèm tình trạng khắc phục.
3. Đề nghị trình diễn một kế hoạch chỉ dựa trên Cây bảo trợ (Sponsor Tree) với các tầng unilevel, thưởng đối ứng (matching bonus), xét cấp bậc, nén tầng (compression) động, mức trần (cap) cho từng Thành viên, một phiên bản kế hoạch có hiệu lực từ một ngày trong tương lai, mô phỏng phiên bản đó, tính toán lại sau khi một sự kiện bị đảo ngược, và chức năng xuất diễn giải cho từng khoản Hoa hồng.
4. Một sự kiện tính hoa hồng có thể mang giá trị và loại tùy ý không phải là đơn hàng sản phẩm, chẳng hạn một sự kiện doanh thu phí, hay không? Sự kiện này được gửi lên như thế nào (endpoint, khóa idempotency) và được đảo ngược ra sao?
5. Có thể tắt chức năng chi trả để nền tảng chỉ phát ra các lệnh chi trả đã được phê duyệt tới một hệ thống ví bên ngoài hay không?
6. Đề nghị mô tả cơ chế xác thực API, giới hạn tần suất gọi, quản lý phiên bản và ngừng hỗ trợ, ký webhook và cơ chế gửi lại, cũng như tình trạng sẵn có của sandbox.
7. Đề nghị mô tả MFA cho quản trị viên, phê duyệt maker-checker, nhật ký kiểm toán không thể sửa đổi và chức năng xuất log.
8. Những dữ liệu nào có thể xuất ra (phả hệ, sổ cái, lịch sử Hoa hồng), theo định dạng nào và với điều khoản chấm dứt hợp tác ra sao?
9. Khu vực hosting, nơi lưu trữ dữ liệu, SLA, mục tiêu sao lưu và giờ hỗ trợ là gì?
10. Thời gian triển khai thực tế cho kế hoạch nêu trên là bao lâu, và quý công ty có thể cung cấp hai khách hàng tham chiếu có quy mô tương tự hay không?

**Câu hỏi riêng cho từng nhà cung cấp**

11. MLM Soft: cung cấp quyền truy cập tài liệu tham chiếu API3 trước khi ký hợp đồng; mô tả danh mục webhook; xác nhận có hỗ trợ API key thay cho tên đăng nhập và mật khẩu hay không; mô tả khả năng hỗ trợ quản lý phiên bản, mô phỏng và thu hồi hoa hồng (clawback); cung cấp giá Enterprise cho quy mô trên 3,000 tài khoản hoạt động.
12. Exigo: xác nhận khả năng hỗ trợ doanh số tính hoa hồng không dựa trên đơn hàng và chi trả qua hạ tầng crypto bên ngoài; cung cấp giá và thời gian triển khai; làm rõ mối quan hệ với DirectScale.
13. Epixel: cung cấp địa chỉ hợp đồng, kho mã nguồn và báo cáo kiểm toán cho việc xử lý hoa hồng bằng "multi-chain smart contract"; nêu rõ bên nào nắm giữ khóa ký; làm rõ phiên bản ISO 27001; cung cấp giá bằng USD.
14. Cloud MLM: xác nhận các mô-đun đầu tư và "staking rewards" có thể được gỡ bỏ hoàn toàn; nêu rõ mã nguồn đã trải qua những đợt rà soát bảo mật nào và tần suất phát hành bản vá.

**Privy**

15. Privy có tiếp nhận mô hình kinh doanh này hay không, và ví nhúng (embedded wallet), chính sách, key quorum và Earn có yêu cầu tài khoản Stripe hoặc Bridge nào không?
16. Những tính năng nào trong thiết kế của chúng tôi yêu cầu gói Enterprise, và với mức giá nào?
17. Lớp bọc thu phí Earn (Earn fee wrapper) đã được kiểm toán chưa, và do đơn vị nào thực hiện? Các cơ chế kiểm soát nâng cấp và quản trị của lớp này là gì?
18. Cơ chế xuất khóa cho Thành viên hoạt động như thế nào nếu nền tảng ngừng sử dụng Privy?

**Turnkey, Alchemy và ZeroDev (phương án ví thay thế độc lập với Stripe)**

19. Quý công ty có tiếp nhận mô hình kinh doanh này hay không? Turnkey: gói nào bao gồm API key được ủy quyền, chính sách và tài trợ phí gas, và chính sách có thể giới hạn một khóa của nền tảng chỉ được nạp vào các vault ERC-4626 được chỉ định, kèm mức trần về số tiền hay không? Alchemy: xác nhận Turnkey là signer được hỗ trợ cho Smart Wallets, giá của các wallet API và tình trạng SOC 2. ZeroDev (Offchain Labs): xác nhận việc chấp thuận trong bối cảnh có quyền chấm dứt vì lý do tổn hại uy tín, cung cấp báo cáo kiểm toán Kernel v4, và xác nhận phạm vi hỗ trợ paymaster trên HyperEVM.

**Nhà cung cấp treasury (Cobo, Fireblocks)**

20. Quý công ty có tiếp nhận mô hình kinh doanh này hay không? Gói nào bao gồm phê duyệt theo quorum và chi trả theo lô trên các mạng chúng tôi cần?

**Nhà cung cấp dịch vụ xác minh (Sumsub, Didit)**

21. Quý công ty có tiếp nhận mô hình kinh doanh này hay không? Gói nào bao gồm xác minh theo cấp, sàng lọc ví và Travel Rule? Các tùy chọn về nơi lưu trữ và thời hạn lưu giữ dữ liệu là gì?

**Nhà cung cấp helpdesk**

22. Zendesk: giá Enterprise cho nhật ký kiểm toán và vai trò tùy chỉnh. Freshdesk: đối tượng tùy chỉnh (custom objects) có được bao gồm trong gói Pro hay không. Intercom: gói nào bao gồm nhật ký kiểm toán.

**Nhà cung cấp on-ramp (Giai đoạn 2)**

23. Sau khi được công bố đầy đủ về mô hình, quý công ty có phê duyệt nền tảng bằng văn bản hay không? Bên nào là merchant of record (đơn vị bán hàng chịu trách nhiệm pháp lý)? Các nền tảng tổng hợp có chuyển nền tảng qua quy trình thẩm định doanh nghiệp riêng của từng nhà cung cấp hay không?

## QUANT (Giai đoạn 2)

1. MVP hiện nay cụ thể bao gồm những gì, và những phần nào đang chạy trên môi trường production?
2. MVP sử dụng mô hình lưu ký nào, và ai có quyền ký đối với tiền của người dùng?
3. Engine có thể vận hành chỉ thông qua các khóa chỉ được giao dịch trên tài khoản Hyperliquid thuộc sở hữu của Thành viên, không có quyền rút tiền, hay không?
4. Hiện có những hạn mức rủi ro, công tắc dừng khẩn (kill switch) và cơ chế giám sát nào? Ai có quyền ghi đè các cơ chế này?
5. Những đợt đánh giá bảo mật, kiểm thử xâm nhập và kiểm toán nào đã được thực hiện, vào thời điểm nào và với phạm vi ra sao?
6. Hiệu quả lịch sử được đo lường và trình bày như thế nào, và đã được xác minh độc lập hay chưa?
7. Những sự cố nào đã xảy ra, và đã được xử lý như thế nào?
8. Mối quan hệ giữa QUANT với "Quantitative Engine" và "TA Capital Trade Deck" được đề cập trong PRD là gì?

## Luật sư tư vấn

**Phạm vi và cấu trúc**

1. AlphaWave sẽ được thành lập tại những khu vực pháp lý nào, và Thành viên sẽ được tuyển dụng hoặc phục vụ tại những khu vực pháp lý nào? Theo đó, những chế độ pháp lý nào được áp dụng?
2. Pháp nhân nào cung cấp từng dịch vụ (ví, Khoản nạp, Sản phẩm sinh lợi (Yield Product), tính Hoa hồng, chi trả hoa hồng)? Với vai trò đơn vị tích hợp và vận hành lớp ứng dụng, Cyclone có chịu rủi ro bị áp dụng bất kỳ phân loại nào trong số này hay không?

**Lưu ký và cấp phép**

3. Theo mô hình ví đề xuất, dù có hay không có signer của nền tảng được giới hạn bằng chính sách, AlphaWave có "control" (quyền kiểm soát) đối với tài sản của Thành viên hay không?
4. Việc giữ Hoa hồng trong ví treasury của nhà vận hành trước khi chi trả có cấu thành hoạt động bảo quản hoặc chuyển giao tài sản thay mặt Thành viên hay không?
5. Một Sản phẩm sinh lợi chuyển Khoản nạp tới một giao thức của bên thứ ba có khiến AlphaWave trở thành nhà cung cấp dịch vụ tài sản ảo, nhà quản lý đầu tư, hay không thuộc trường hợp nào?

**KYC và AML**

6. Có được phép áp dụng cấp nào không yêu cầu KYC hay không, và nếu có thì đến mức giá trị lũy kế nào và cho những thao tác nào?
7. Cần thu thập những thông tin gì đối với giao dịch rút tiền và chi trả tới ví tự lưu ký? Travel Rule có được áp dụng không?
8. Cần thực hiện sàng lọc danh sách trừng phạt như thế nào đối với địa chỉ ví và Thành viên, theo những danh sách nào và với tần suất ra sao?
9. Những nghĩa vụ nào về lưu giữ hồ sơ, báo cáo giao dịch đáng ngờ và cán bộ tuân thủ được áp dụng?
10. Có cần thông tin định danh cho mục đích kê khai thuế đối với Hoa hồng, độc lập với yêu cầu AML, hay không?

**MLM, chứng khoán và bảo vệ người tiêu dùng**

11. Những cơ sở tính hoa hồng nào là hợp pháp theo luật về mô hình kim tự tháp tại từng khu vực pháp lý mục tiêu: doanh thu phí nền tảng, doanh số Khoản nạp, giá trị lợi suất?
12. Theo từng cơ chế được xem xét (Staking, cho vay (lending), vault giao dịch, do nhà vận hành quản lý), Sản phẩm sinh lợi có phải là chứng khoán, hợp đồng đầu tư, chương trình đầu tư tập thể hoặc hoạt động huy động tiền gửi hay không? SEC và CFTC đã ban hành một văn bản diễn giải chung về tài sản crypto, bao gồm staking giao thức, vào ngày 17 tháng 3 năm 2026 ([SEC 2026-30](https://www.sec.gov/newsroom/press-releases/2026-30-sec-clarifies-application-federal-securities-laws-crypto-assets)); văn bản này và các quy định tương đương tại địa phương được áp dụng như thế nào?
13. Thành viên tuyển dụng và nhận Hoa hồng có cần giấy phép hoặc đăng ký nào không?
14. Cần có những công bố thông tin về thu nhập, cảnh báo rủi ro và biện pháp kiểm soát tiếp thị nào, kể cả đối với nội dung do Thành viên tạo?

**Nhà cung cấp và ngân hàng**

15. AlphaWave có thể dựa vào quy trình KYC của một nhà cung cấp (ví dụ của một on-ramp) để thực hiện nghĩa vụ của chính mình hay không?
16. Có điều khoản nào của nhà cung cấp không tương thích với mô hình kinh doanh theo cấu trúc hiện tại hay không?

Nguồn tham khảo dành cho luật sư tư vấn (chỉ mang tính ví dụ, không phải đánh giá về khả năng áp dụng): [hướng dẫn năm 2021 của FATF về tài sản ảo](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), [EU MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), [EU Transfer of Funds Regulation](https://eur-lex.europa.eu/eli/reg/2023/1113/oj), [FinCEN FIN-2019-G001](https://www.fincen.gov/sites/default/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf), [hướng dẫn của FTC về tiếp thị đa cấp](https://www.ftc.gov/business-guidance/resources/business-guidance-concerning-multi-level-marketing), [FTC Business Opportunity Rule](https://www.ftc.gov/legal-library/browse/rules/business-opportunity-rule), [Investor.gov về mô hình kim tự tháp](https://www.investor.gov/introduction-investing/investing-basics/glossary/pyramid-schemes).
