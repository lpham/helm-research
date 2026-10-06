# So sánh nền tảng MLM, danh sách rút gọn và các trường hợp loại trừ

## Phương pháp tiếp cận

Mười lăm nhà cung cấp đã được xem xét, bao gồm các nền tảng white-label được quảng bá cho MLM crypto, các nền tảng bán hàng trực tiếp cấp doanh nghiệp đã có chỗ đứng, và các công cụ tính hoa hồng theo mô hình headless hoặc API-first. Các đơn vị phát triển theo yêu cầu và các công cụ tự xây dựng được chủ động loại khỏi phạm vi. Các nhà cung cấp chỉ được đánh giá dựa trên nguồn công khai; chưa có sản phẩm nào được trình diễn hay kiểm thử.

Do Cây bảo trợ (Sponsor Tree) là cây duy nhất trong kế hoạch của AlphaWave, các cây xếp vị trí dạng binary và matrix là không cần thiết. Các năng lực quan trọng gồm: logic unilevel, theo thế hệ (generation), thưởng đối ứng (matching) và cấp bậc; nén tầng (compression) và mức trần (cap); quản lý phiên bản kế hoạch có ngày hiệu lực; mô phỏng; giải trình Hoa hồng (Commission); thu hồi hoa hồng (clawback); và tách biệt hoàn toàn giữa việc tính Hoa hồng và thực hiện chi trả. **Không nhà cung cấp nào công bố tài liệu công khai đáp ứng đầy đủ tất cả các năng lực này.**

## Điều kiện đủ

Một nhà cung cấp phải đáp ứng cả bốn điều kiện trước khi được chấm điểm. Giá thấp không thể bù đắp cho việc không đạt một điều kiện.

1. **Không có lợi suất chỉ để hiển thị.** Mọi mô-đun "staking", "ROI" hay "investment plan" phải có khả năng tắt hoàn toàn; mô-đun này không bao giờ được dùng làm Sản phẩm sinh lợi (Yield Product).
2. **Chi trả có thể tách khỏi việc tính toán**, để các khoản chi trả được thực hiện từ lớp ví của chính AlphaWave và dưới sự kiểm soát của AlphaWave, không phải bên trong phần mềm MLM.
3. **Có giao diện tích hợp được mô tả bằng tài liệu**: hướng dẫn hoặc tài liệu tham chiếu API được công bố, hoặc tài liệu của nhà cung cấp về mô hình sự kiện và dữ liệu.
4. **Là sản phẩm được duy trì bởi một nhà cung cấp xác định được**, không phải một script sao chép (clone script) hay một bản xây dựng tùy chỉnh dùng một lần.

## Các nhà cung cấp đã xem xét

| Nhà cung cấp | Loại hình | Crypto | Lợi suất | Bằng chứng bảo mật | Giá | Kết quả |
|---|---|---|---|---|---|---|
| MLM Soft | Công cụ SaaS headless | Ví token dùng cho ghi sổ; adapter chi trả (theo tuyên bố) | Không có (theo thiết kế) | Không tìm thấy | $499–$1,999/tháng + phí thiết lập $10k–$30k (đã xác minh) | **Danh sách rút gọn (ứng viên hàng đầu)** |
| Exigo | Nền tảng bán hàng trực tiếp cấp doanh nghiệp | Không có | Không có | Tuyên bố đạt SOC 2 và PCI; báo cáo không công khai | Báo giá | **Danh sách rút gọn (phương án thay thế)** |
| Epixel | White-label tích hợp | Chi trả bằng BTC, ETH, USDT và các loại khác; hoa hồng qua "smart contract" (theo tuyên bố) | Chỉ có nội dung tiếp thị "investment plan" | Tuyên bố ISO 27001 không nhất quán (phiên bản 2013 và 2022) | Công bố các gói CA$1,381 và CA$6,914; giá USD theo báo giá | **Danh sách rút gọn (phương án tích hợp)** |
| Cloud MLM | Giấy phép mã nguồn, tự lưu trữ | Nêu tên cổng thanh toán CoinPayments và Bitaps (lưu ký) | Mô-đun tính lợi nhuận (cần tắt) | Không có | Từ $750 một lần + 18% phí bảo trì hằng năm (đã xác minh) | **Danh sách rút gọn (chi phí thấp, khả năng rút lui)** |
| FlawlessMLM | Công cụ tính thưởng, dạng SaaS hoặc gói phần mềm | Chỉ có tuyên bố trong bài viết của bên thứ ba | Không có | Không có | Gói $6,000 hoặc $1,499/tháng (đã xác minh) | Dự phòng |
| Infinite MLM | Giấy phép một lần | Theo tuyên bố (BTC, ETH, USDT, MetaMask) | "Staking & ROI dashboard" (chỉ hiển thị) | ISO 27001:2013 (phiên bản đã hết hiệu lực); tự khẳng định SOC 2 | $699 gói Basic (đã xác minh) | Dự phòng |
| Tapfiliate | Nền tảng affiliate có API đa tầng | Không có | Không có | Không tìm thấy | Báo giá Enterprise cho API | Phương án dự phòng chỉ cho kế hoạch rất đơn giản |
| Post Affiliate Pro | Nền tảng affiliate, tối đa 99 tầng (theo tuyên bố) | Không có | Không có | Không tìm thấy | Từ $139/tháng | Phương án dự phòng chỉ cho kế hoạch rất đơn giản |
| Hybrid MLM | Giấy phép một lần + mã nguồn | Cổng thanh toán chỉ có ở gói cao nhất | Hoa hồng trên "investment" và "ROI" | Không có | $599–$4,549 một lần | Loại trừ |
| ARM MLM | Script | Smart contract "Forsage clone" | Mô hình phí gia nhập | Không có | Từ $799 | Loại trừ |
| ByDesign | Doanh nghiệp | Không có | Không có | Huy hiệu SOC 2 và ISO | Báo giá | Loại trừ (trùng lặp với Exigo nhưng ít tài liệu hơn) |
| InfoTrax | Doanh nghiệp, lấy đơn hàng làm trung tâm | Không có | Không có | Không tìm thấy | Không tìm thấy | Loại trừ |
| DirectScale | API doanh nghiệp | Không có | Không có | Không tìm thấy | Không tìm thấy | Loại trừ (tên miền hiện chuyển hướng sang Exigo; quan hệ giữa hai bên chưa được xác nhận) |
| Trinity (Firestorm) | Back office cho mô hình bán hàng qua tiệc (party-plan) | Không có | Không có | Không tìm thấy | Gói thuê bao | Loại trừ |
| Các đơn vị phát triển (Osiz, Suffescom và các đơn vị khác) | Bản xây dựng tùy chỉnh và bản sao chép | Theo tuyên bố | Ngôn ngữ "Guaranteed ROI" | Không có | Báo giá | Loại trừ (tự xây dựng) |

Nguồn: [MLM Soft pricing](https://www.mlmsoft.com/cloudplatform/subscription), [Exigo platform](https://www.exigo.com/exigo-platform/), [Epixel](https://www.epixelmlmsoftware.com/), [Epixel CAD pricing](https://www.epixelmlmsoftware.com/en-ca/pricing), [Cloud MLM pricing](https://cloudmlmsoftware.com/pricing/), [FlawlessMLM](https://flawlessmlm.com/en/mlm-marketing-software), [Infinite MLM pricing](https://infinitemlmsoftware.com/pricing), [Tapfiliate REST API](https://tapfiliate.com/docs/rest/), [Post Affiliate Pro pricing](https://www.postaffiliatepro.com/pricing/), [Hybrid MLM pricing](https://www.hybridmlm.io/pricing/).

Hai phát hiện áp dụng cho toàn thị trường:

- **Các tuyên bố về "smart contract commission" không có cơ sở.** Epixel, Infinite MLM và Hybrid MLM có quảng bá tính năng này, nhưng không tìm thấy địa chỉ hợp đồng, kho mã nguồn hay báo cáo kiểm toán nào cho bất kỳ nhà cung cấp nào trong số đó.
- **Một số tuyên bố ISO 27001 không thể còn hiệu lực.** Tất cả chứng chỉ ISO/IEC 27001:2013 được công nhận đã hết hạn hoặc bị thu hồi vào ngày 31 tháng 10 năm 2025 ([SGS transition notice](https://www.sgs.com/en/news/2024/05/iso-iec-27001-transition-what-you-should-know)). Mọi chứng nhận trên thị trường này cần được coi là chưa xác minh cho đến khi nhà cung cấp xuất trình chứng chỉ còn hiệu lực hoặc báo cáo SOC 2.

## Bảng chấm điểm có trọng số

Thang điểm từ 1 (yếu hoặc không có bằng chứng) đến 5 (mạnh, có tài liệu). Đây là đánh giá của Cyclone dựa trên bằng chứng công khai và sẽ thay đổi sau các buổi trình diễn.

| Tiêu chí | Trọng số | MLM Soft | Exigo | Cloud MLM | Epixel | FlawlessMLM |
|---|--:|--:|--:|--:|--:|--:|
| Tính năng trả thưởng (kế hoạch, quản lý phiên bản, mô phỏng, thu hồi hoa hồng, giải trình) | 25% | 3 | 4 | 3 | 3 | 4 |
| Tính linh hoạt của cơ sở tính hoa hồng (sự kiện không phải đơn hàng) | 15% | 5 | 2 | 3 | 3 | 2 |
| Tích hợp (API, webhook, headless, tách biệt chi trả) | 20% | 4 | 5 | 2 | 3 | 2 |
| Bằng chứng về bảo mật và kiểm soát | 15% | 1 | 4 | 1 | 2 | 1 |
| Thời gian triển khai | 10% | 4 | 1 | 3 | 3 | 3 |
| Khả năng rút lui, quyền sở hữu dữ liệu và mức độ phụ thuộc | 10% | 3 | 3 | 5 | 2 | 3 |
| Minh bạch thương mại và chi phí | 5% | 5 | 1 | 5 | 3 | 4 |
| **Điểm có trọng số** | | **3.40** | **3.35** | **2.80** | **2.75** | **2.65** |

Hai ứng viên dẫn đầu có điểm sát nhau vì những lý do khác nhau. MLM Soft vượt trội về tính linh hoạt của cơ sở tính hoa hồng, tốc độ và giá; Exigo vượt trội về bằng chứng kiểm soát và mức độ trưởng thành của tích hợp nhưng triển khai chậm hơn và chỉ cung cấp giá theo báo giá. **Yếu tố quyết định đối với MLM Soft là thẩm định (due diligence) bảo mật**: không tìm thấy báo cáo SOC 2, chứng chỉ ISO hay bản tóm tắt kiểm thử xâm nhập nào. Cả hai nhà cung cấp nên được trình diễn song song.

## Danh sách rút gọn

**1. MLM Soft (ứng viên hàng đầu cho kiến trúc mô-đun).**

- REST API (API3) của nhà cung cấp này "covers all the functionality of the platform" (bao quát toàn bộ chức năng của nền tảng), kèm tài liệu Swagger riêng cho từng tenant ([developers API](https://help.mlmsoft.net/hc/en-us/articles/39249636419475-Developers-API), đã xác minh trong tài liệu của nhà cung cấp).
- Các thuộc tính kế hoạch tùy chỉnh có thể được gắn cờ là volume, bonus hoặc rank và "set by API request" (được thiết lập qua yêu cầu API), do đó có thể gửi một khoản doanh thu phí cho từng Thành viên theo từng sự kiện và dùng làm cơ sở tính hoa hồng ([plan properties](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration), đã xác minh trong tài liệu của nhà cung cấp).
- Hoa hồng được ghi vào một ví ghi sổ; việc chi trả được thực hiện riêng qua một adapter thanh toán. Nhà cung cấp tự mô tả là "not a financial institution" (không phải tổ chức tài chính), phù hợp với sổ cái và lớp ví do Cyclone sở hữu.
- Giá công bố: $499, $999 và $1,999 mỗi tháng cho tối đa 300, 1,000 và 3,000 tài khoản có hoạt động thương mại trong ba tháng gần nhất; gói Enterprise theo báo giá; phí thiết lập "usually varies between $10,000 to $30,000" (đã xác minh). Gói thấp nhất chỉ cho phép một ví và một quản trị viên, nên gói Community hoặc Network là điểm khởi đầu thực tế, và một mạng lưới lớn sẽ chạm đến mức giá Enterprise.
- Khoảng trống: không có chứng thực bảo mật; quản lý phiên bản kế hoạch, mô phỏng và thu hồi hoa hồng tự động không được mô tả trong tài liệu; API xác thực bằng tên đăng nhập và mật khẩu thay vì API key có tài liệu.

**2. Exigo (phương án thay thế cấp doanh nghiệp).**

- Hơn 200 API với tài liệu dành cho nhà phát triển được công khai ([developers.exigo.com](https://developers.exigo.com/), đã xác minh). Tuyên bố tuân thủ SOC 2, PCI và GDPR (tuyên bố của nhà cung cấp; cần yêu cầu báo cáo). Các tích hợp chi trả đã trưởng thành (PayQuicker, Worldpay, Hyperwallet, iPayout).
- Không có năng lực crypto, điều này ít quan trọng hơn trong thiết kế mô-đun vì phần crypto nằm ngoài lõi MLM. Các cơ sở tính hoa hồng không dựa trên sản phẩm sẽ được mô hình hóa dưới dạng đơn hàng tổng hợp hoặc volume tùy chỉnh.
- Không có giá công khai; thời gian chờ triển khai cấp doanh nghiệp khiến việc cấu hình trong 30 ngày khó khả thi.

**3. Epixel (phương án white-label tích hợp).**

- Bộ tính năng MLM crypto rộng nhất trong số các nhà cung cấp đã có chỗ đứng, với hướng dẫn tích hợp công khai bao gồm xác thực JWT, webhook và SSO ([api.epixelsoftware.help](https://api.epixelsoftware.help/), đã xác minh sự tồn tại của hướng dẫn).
- Mọi tuyên bố về khả năng thực thi crypto đều cần được trình diễn kỹ thuật. Mô hình lưu ký và quyền sở hữu khóa không được mô tả trong tài liệu. Trang "cryptocurrency investment plan" của nhà cung cấp dùng ngôn ngữ như "investment will double or may triple", vốn tuyệt đối không được tái sử dụng.

**4. Cloud MLM (chi phí thấp, vị thế rút lui mạnh nhất).**

- Toàn bộ mã nguồn Laravel từ $750 một lần, có thể tự lưu trữ, với 21 loại kế hoạch (đã xác minh). Việc nắm giữ mã nguồn loại bỏ sự phụ thuộc vào nhà cung cấp nhưng chuyển trách nhiệm bảo mật sang Cyclone.
- Các cổng thanh toán được nêu tên (CoinPayments, Bitaps) là cổng lưu ký, mâu thuẫn với thiết kế ví do Thành viên sở hữu; chúng sẽ được thay thế bằng tích hợp ví của Cyclone. Các mô-đun đầu tư và "staking rewards" phải được tắt.

**Dự phòng và phương án thay thế.** FlawlessMLM có tài liệu mô tả các tính năng công cụ tính hoa hồng mạnh nhất (mô phỏng what-if, quản lý phiên bản quy tắc, xử lý hàng trả lại) và là công cụ headless dự phòng. Tapfiliate và Post Affiliate Pro có thể hỗ trợ một kế hoạch được chủ ý giữ đơn giản (tỷ lệ phần trăm cố định theo từng tầng trên doanh thu phí) nhưng thiếu cơ chế xét cấp bậc, nén tầng và quản lý phiên bản.

## Các trường hợp loại trừ

| Nhà cung cấp | Lý do |
|---|---|
| Hybrid MLM | Kế hoạch đầu tư của nhà cung cấp này trả Hoa hồng theo tầng dựa trên "investment" và "ROI" của người được tuyển, với lợi nhuận được chi trả từ "company profits" tạo ra bằng chính khoản tiền đầu tư. Đây là một mẫu thiết kế có rủi ro Ponzi ([nguồn](https://www.hybridmlm.io/investment-mlm-plan/)). |
| ARM MLM | Quảng bá smart contract thu phí gia nhập kiểu "Forsage clone". SEC đã khởi tố các nhà sáng lập Forsage vì cáo buộc vận hành mô hình kim tự tháp và Ponzi ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)). |
| Infinite MLM | Bảng điều khiển "Staking & ROI" chỉ để hiển thị; liên kết tài liệu REST API trả về lỗi; tuyên bố ISO dẫn chiếu một phiên bản đã hết hiệu lực. Chỉ được giữ ở diện dự phòng như một phương án tương đương với Cloud MLM. |
| ByDesign, InfoTrax | Các nền tảng doanh nghiệp lấy đơn hàng làm trung tâm, không có bằng chứng về crypto và ít tài liệu công khai hơn Exigo. |
| DirectScale | Tên miền chuyển hướng sang Exigo vào ngày nghiên cứu; tình trạng pháp nhân chưa được xác nhận. Nếu cần, đánh giá thông qua Exigo. |
| Trinity (Firestorm) | Back office cho mô hình party-plan, không có tài liệu API. |
| Các đơn vị phát triển | Các bản xây dựng tùy chỉnh và script sao chép, thường được quảng bá với ngôn ngữ "guaranteed ROI". Thuộc diện loại trừ đối với giải pháp tự xây dựng. |
| CaptivateIQ, Everstage, QuotaPath và các công cụ tương tự | Công cụ tính thưởng bán hàng, định giá theo từng người nhận và được xây dựng quanh hệ thống phân cấp bán hàng, không phải phả hệ Thành viên. |
