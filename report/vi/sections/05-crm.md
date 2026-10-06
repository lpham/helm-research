# CRM và vận hành chăm sóc khách hàng

## Tóm tắt khuyến nghị

**Trong 30 ngày đầu, nên sử dụng một helpdesk SaaS chuyên dụng thay vì một bộ giải pháp CRM.** Ở giai đoạn này, vận hành chăm sóc khách hàng chủ yếu là xử lý ticket: các câu hỏi về Khoản nạp (Deposit) và rút tiền, vướng mắc khi xác minh danh tính, tranh chấp Hoa hồng (Commission), truy cập tài khoản và bảo mật. Helpdesk đóng vai trò hộp thư tiếp nhận; back office quản trị do Cyclone xây dựng là nơi nhân viên hỗ trợ tra cứu thông tin và thực hiện các thao tác vận hành. Hai hệ thống được liên kết bằng deep link và một thanh bên chỉ đọc, truy xuất theo Member ID.

Salesforce và Odoo, hai giải pháp AlphaWave đã từng thảo luận, được đánh giá theo cùng tiêu chí. Cả hai đều phù hợp với một giai đoạn CRM về sau hơn là với helpdesk trong 30 ngày đầu.

## So sánh các phương án

| | Zendesk Suite Professional | Freshdesk Omni Enterprise | Intercom Expert | Salesforce Service Cloud | Odoo (Enterprise apps) |
|---|---|---|---|---|---|
| Giá niêm yết, mỗi nhân viên hỗ trợ mỗi tháng (thanh toán năm) | $115 | $119 | $132 | $195 (Core), $395 (Advanced) | Tùy theo quốc gia thanh toán; theo báo giá |
| Đối tượng tùy chỉnh (liên kết với Member ID, ví, trạng thái KYC) | Tối đa 30 | Có | 15 trên mọi gói (theo tuyên bố) | Có, rất phong phú | Có (Studio) |
| SLA và quy trình chuyển cấp | Có | Có | Gói Expert | Có (entitlements) | Có |
| Phê duyệt | Phê duyệt ticket | Có | Hạn chế | Có | Ứng dụng Approvals |
| Nhật ký kiểm toán | Gói Enterprise (theo báo giá) | Đã bao gồm | Cần xác nhận theo gói | Có; Shield cho lịch sử trường dữ liệu | Có |
| SSO | Có | Có | Gói Expert | Có | Có |
| Telegram | Qua tích hợp | Ứng dụng trên Marketplace | **Tích hợp sẵn** (theo tuyên bố) | Phải tự xây dựng | Mô-đun bên thứ ba (cần Odoo.sh hoặc tự lưu trữ) |
| Nơi lưu trữ dữ liệu | Tiện ích bổ sung miễn phí về vị trí dữ liệu (US, EEA, UK, JP, AU) | Trung tâm dữ liệu theo khu vực | Lưu trữ theo khu vực | Các khu vực Hyperforce | Tùy chọn nơi lưu trữ |
| Công sức triển khai (ước tính) | 0.75–2.5 người-tháng | 0.75–2.5 | 0.75–2.5 | 3–5 | 2–3 |
| Mức độ phù hợp với mốc 30 ngày | **Tốt** | **Tốt** | Tốt nếu lấy chat làm kênh chính | Kém (công sức) | Trung bình (công sức, API chỉ có ở gói Custom) |

Nguồn (giá ghi nhận ngày 6 tháng 10 năm 2026, đã xác minh trên trang của nhà cung cấp): [Zendesk pricing](https://www.zendesk.com/pricing/), [Freshdesk Omni pricing](https://www.freshworks.com/freshdesk/omni/pricing/), [Intercom pricing](https://www.intercom.com/pricing), [Salesforce Service Cloud pricing](https://www.salesforce.com/service/pricing/), [Odoo editions](https://www.odoo.com/page/editions), [Odoo pricing](https://www.odoo.com/pricing).

Ghi chú bổ sung:

- **Odoo:** Helpdesk, Knowledge, Approvals và Studio chỉ có ở phiên bản Enterprise, và API bên ngoài yêu cầu gói Custom (đã xác minh). Giá USD phụ thuộc vào quốc gia thanh toán: mức $13.40–$16.40 mỗi người dùng được hiển thị cho địa điểm thực hiện nghiên cứu, còn một bên thứ ba ghi nhận mức $49–$61 tại Hoa Kỳ (chưa xác minh). Odoo cũng tính giấy phép cho mọi người dùng nội bộ, kể cả nhân sự back office, trong khi các helpdesk SaaS chỉ tính giấy phép cho nhân viên hỗ trợ. Không thu thập được bằng chứng về ISO 27001 và SOC 2.
- **Salesforce:** năng lực quản lý hồ sơ yêu cầu, các tùy chọn kiểm toán và lưu trữ dữ liệu theo khu vực mạnh nhất, đi kèm chi phí giấy phép và quản trị cao nhất. Financial Services Cloud ($325–$700 mỗi người dùng) chưa có cơ sở để sử dụng ở giai đoạn này.
- **Intercom:** phương án duy nhất tích hợp sẵn Telegram, phù hợp với mô hình hỗ trợ MLM dựa vào cộng đồng. AI agent của Intercom có giá $0.99 cho mỗi kết quả được giải quyết, cộng thêm vào phí theo số ghế.

## Ranh giới hệ thống: CRM, helpdesk, back office và sổ cái

Không CRM hay helpdesk nào nắm giữ dữ liệu tài chính có giá trị gốc.

| Hệ thống | Nguồn dữ liệu gốc cho | Không được sở hữu hoặc thực hiện | Quyền truy cập của nhân viên hỗ trợ |
|---|---|---|---|
| Sổ cái tài chính | Số dư, Khoản nạp, rút tiền, chi trả hoa hồng, trạng thái đối soát | Hội thoại; chỉnh sửa thủ công | Không truy cập trực tiếp; chỉ thông qua các lệnh của back office |
| Nền tảng MLM | Cây bảo trợ (Sponsor Tree), phiên bản kế hoạch, tính toán và giải trình Hoa hồng | Thực hiện chi trả; ticket | Chế độ xem chỉ đọc qua back office |
| Nhà cung cấp dịch vụ xác minh | Trạng thái KYC, hồ sơ bằng chứng, kết quả sàng lọc danh sách trừng phạt | Bị sao chép vào helpdesk | Chỉ trạng thái; hồ sơ bằng chứng dành cho vai trò tuân thủ |
| Back office quản trị (Cyclone) | Thao tác vận hành: tạm giữ, phê duyệt và thử lại lệnh rút tiền; đóng băng tài khoản; xem xét thay đổi địa chỉ; yêu cầu điều chỉnh Hoa hồng; nhật ký kiểm toán quản trị | Nhắn tin; theo dõi SLA | Theo phạm vi vai trò; mọi thao tác tài chính cần người phê duyệt thứ hai |
| Helpdesk | Hội thoại, ticket, bộ đếm thời gian SLA, cơ sở tri thức, macro | Số dư, bí mật ví, tài liệu KYC, phê duyệt dịch chuyển tiền, thay đổi Cây bảo trợ | Tất cả nhân viên hỗ trợ; hồ sơ yêu cầu chỉ lưu mã tham chiếu |
| CRM (giai đoạn sau) | Bối cảnh quan hệ: trưởng nhóm, pipeline, phân khúc, chiến dịch | Số dư hoặc số liệu Hoa hồng có giá trị gốc | Nhân sự phụ trách thành công của Thành viên |

Nguyên tắc thiết kế:

1. Helpdesk lưu **mã tham chiếu, không lưu giá trị**. Trạng thái Thành viên được truy xuất trực tiếp từ back office theo thời gian thực.
2. Phê duyệt trong helpdesk chỉ dành cho các quyết định phi tài chính. Mọi dịch chuyển tiền đều được phê duyệt trong back office theo cơ chế maker-checker.
3. Nhân viên hỗ trợ không bao giờ yêu cầu khóa riêng tư hay cụm từ khôi phục (seed phrase); macro, cơ sở tri thức và bộ lọc thư đến thực thi quy tắc này.
4. Hồ sơ yêu cầu được tạo tự động từ back office (lệnh rút tiền bị treo, từ chối KYC, tranh chấp Hoa hồng) kèm mã tham chiếu back office.

## Cấu hình tối thiểu khả thi cho 30 ngày

- **Công cụ:** một helpdesk được chọn sau một tuần dùng thử theo kịch bản giữa Zendesk Suite Professional và Freshdesk Omni Enterprise, hoặc Intercom nếu chat và Telegram sẽ là kênh chủ đạo.
- **Nhân sự:** ba đến năm nhân viên hỗ trợ cho giai đoạn thí điểm có kiểm soát, một trưởng nhóm hỗ trợ và một phần tư thời gian của một quản trị viên helpdesk. Người phê duyệt tài chính và tuân thủ làm việc trong back office.
- **Kênh:** email và chat trong ứng dụng. Telegram và WhatsApp chỉ triển khai sau khi có tài khoản đã xác minh và rà soát bảo mật.
- **Loại hồ sơ yêu cầu:** Khoản nạp, rút tiền, KYC, tranh chấp Hoa hồng, Cây bảo trợ hoặc giới thiệu, truy cập tài khoản, bảo mật hoặc lừa đảo phishing.
- **Hàng đợi và SLA:** hồ sơ bảo mật và rút tiền ở mức ưu tiên cao nhất; hàng đợi riêng cho tiền, xác minh và Hoa hồng.
- **Cơ sở tri thức:** 20–40 bài viết được bộ phận tuân thủ rà soát, bao gồm Khoản nạp sai mạng, phí mạng, các bước xác minh, cách thức và thời điểm chi trả Hoa hồng, và các cảnh báo bảo mật. Không đưa ra tư vấn tài chính.
- **AI agent:** tắt, hoặc giới hạn trong phạm vi tri thức đã được phê duyệt, bắt buộc chuyển cấp đối với các chủ đề về tiền và xác minh.
- **Công sức:** khoảng 1.5 người-tháng (dao động 0.75–2.5) và hai đến ba tuần thực hiện sau khi hoàn tất mua sắm.

| Chi phí giấy phép hằng tháng (ước tính từ giá niêm yết) | 5 nhân viên hỗ trợ | 15 nhân viên hỗ trợ |
|---|--:|--:|
| Thấp (Freshdesk Omni Growth hoặc Zendesk Suite Team) | $145–$275 | $435–$825 |
| Cơ sở (Zendesk Suite Professional hoặc Freshdesk Omni Enterprise) | $575–$595 | $1,725–$1,785 |
| Cao (Zendesk Enterprise, hoặc Salesforce Service Core kèm nhắn tin) | khoảng $1,350+ | khoảng $4,050+ |

Phí AI và phí nhắn tin tính theo mức sử dụng được tính thêm.

## Lộ trình mở rộng

- **Tháng 2–4: củng cố helpdesk.** Bổ sung Telegram và WhatsApp, nâng cấp lên gói có nhật ký kiểm toán và vai trò tùy chỉnh nếu chưa mua từ đầu, bổ sung chấm điểm chất lượng (QA) và nội dung đa ngôn ngữ, và kích hoạt AI agent giới hạn trong phạm vi tri thức.
- **Tháng 4–9: bổ sung lớp CRM nếu có cơ sở kinh doanh**, phục vụ quản lý quan hệ với trưởng nhóm, pipeline gia nhập thị trường mới và phân khúc chiến dịch. Các phương án: CRM của chính nhà cung cấp helpdesk (đơn giản nhất); Odoo nếu AlphaWave đồng thời cần chức năng ERP (ước tính 3–6 người-tháng); hoặc Salesforce nếu quy mô và cổng thông tin đối tác biện minh cho lựa chọn này (ước tính 4–8 người-tháng cộng 0.5–1 FTE quản trị viên).
- **Giai đoạn sau: hợp nhất.** Nếu Salesforce hoặc Odoo trở thành CRM, cần quyết định có chuyển mảng hỗ trợ sang hệ thống đó hay không; dự trù 2–4 người-tháng.
