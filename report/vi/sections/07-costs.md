# Chi phí, nguồn lực và ước tính vận hành 12 tháng

## Cơ sở ước tính

- **Đơn vị tiền tệ và thời điểm:** USD, theo giá ghi nhận ngày 6 tháng 10 năm 2026. Giá chưa bao gồm thuế.
- **Quy mô:** một đợt thí điểm có kiểm soát (controlled pilot) với tối đa 3,000 Thành viên có phát sinh hoa hồng, dưới 10,000 người dùng ví hoạt động hằng tháng, khoảng 1,000 Thành viên mới mỗi tháng và năm nhân viên helpdesk.
- **Phạm vi:** Phương án 2 (mô-đun). Release 1 (bản phát hành đầu tiên) không có on-ramp fiat, không có hợp đồng thông minh tùy biến và chưa vận hành Sản phẩm sinh lợi (Yield Product).
- **Nhân công:** đơn giá ngày công của Cyclone đã được thỏa thuận theo hợp đồng, vì vậy nguồn lực chỉ được thể hiện bằng **người-tháng** (person-month). Các số liệu bằng tiền chỉ bao gồm phần mềm và dịch vụ bên ngoài.
- **Không bao gồm:** phí luật sư tư vấn, hồ sơ xin cấp phép, chi phí ngân hàng, thành lập pháp nhân, tiếp thị và phí mạng do Thành viên tự chi trả.
- **Nhãn bằng chứng:** **X** = giá công khai đã xác minh; **B** = cần báo giá từ nhà cung cấp; **U** = ước tính của tư vấn Cyclone. Trường hợp có giá công khai nhưng các tính năng cần thiết chỉ nằm trong gói phải báo giá, số liệu được đánh dấu U.

## Phần mềm và dịch vụ bên ngoài

| Hạng mục | Thấp | Cơ sở | Cao | Căn cứ |
|---|--:|--:|--:|---|
| Lõi MLM: gói thuê bao MLM Soft (hằng tháng) | $999 | $1,999 | $4,000 | X cho gói Community và Network; kịch bản cao là U cho gói Enterprise (B) |
| Lõi MLM: thiết lập và tùy biến (một lần) | $10,000 | $20,000 | $30,000 | X ("usually varies between $10,000 to $30,000") |
| Ví Thành viên: Privy (hằng tháng) | $499 | $1,500 | $3,000 | U. Các gói công khai ở mức $299–$499/tháng, nhưng công cụ chính sách (policy engine), key quorum và webhook môi trường production thuộc gói Enterprise (B) |
| Công cụ quản lý ví treasury của nhà vận hành (hằng tháng) | $0 | $299 | $999 | X: key quorum của Privy (trong Privy Enterprise), Cobo Starter, Fireblocks Essentials |
| Sàng lọc KYC và AML, kịch bản B (hằng tháng) | $250 | $1,200 | $2,000 | U, dựa trên đơn giá mỗi lượt kiểm tra đã xác minh (X) của Didit, Sumsub, Veriff |
| Sàng lọc ví và giám sát giao dịch (hằng tháng) | $0 | $100 | $1,500 | X đối với oracle miễn phí của Chainalysis và đơn giá mỗi lượt kiểm tra của Didit; KYT thương mại là B |
| Helpdesk, 5 nhân viên (hằng tháng) | $145 | $585 | $1,350 | X theo giá niêm yết; kịch bản cao bao gồm các hạng mục B |
| Hosting, RPC/indexer, giám sát và ghi log (hằng tháng) | $800 | $2,000 | $4,000 | U |
| Tài trợ phí gas cho thao tác ví của Thành viên (hằng tháng) | $200 | $500 | $1,000 | U; chi phí chuyển tiếp, phụ thuộc khối lượng |
| On-ramp fiat (Release 1) | $0 | $0 | $0 | Lùi sang Giai đoạn 2; một nền tảng tổng hợp như Onramper có chi phí $199–$599/tháng (X) |
| Kiểm thử xâm nhập trước khi ra mắt (một lần) | $12,000 | $25,000 | $40,000 | U (không có bảng giá công khai; kiểm thử tự động từ $3,500 là X nhưng tự nó chưa đủ) |
| Rà soát ví và quản lý khóa (một lần) | $10,000 | $20,000 | $30,000 | U |
| Kiểm toán hợp đồng thông minh | $0 | $0 | $0 | Không cần khi Release 1 không triển khai hợp đồng tùy biến; $15,000–$100,000+ nếu có (U) |

Nguồn: [MLM Soft](https://www.mlmsoft.com/cloudplatform/subscription), [Privy](https://www.privy.io/pricing), [Cobo](https://www.cobo.com/pricing), [Fireblocks](https://www.fireblocks.com/pricing), [Sumsub](https://sumsub.com/pricing/), [Zendesk](https://www.zendesk.com/pricing/), [Freshdesk](https://www.freshworks.com/freshdesk/omni/pricing/), [Cobalt](https://www.cobalt.io/pricing).

## Chi phí triển khai một lần (bên ngoài)

| | Thấp | Cơ sở | Cao |
|---|--:|--:|--:|
| Thiết lập và tùy biến MLM | $10,000 | $20,000 | $30,000 |
| Kiểm thử xâm nhập | $12,000 | $25,000 | $40,000 |
| Rà soát ví và quản lý khóa | $10,000 | $20,000 | $30,000 |
| **Tổng chi phí một lần** | **$32,000** | **$65,000** | **$100,000** |

## Chi phí vận hành hằng tháng (bên ngoài)

| | Thấp | Cơ sở | Cao |
|---|--:|--:|--:|
| Gói thuê bao MLM | $999 | $1,999 | $4,000 |
| Hạ tầng ví | $499 | $1,500 | $3,000 |
| Công cụ quản lý treasury | $0 | $299 | $999 |
| Sàng lọc KYC, AML và ví | $250 | $1,300 | $3,500 |
| Helpdesk | $145 | $585 | $1,350 |
| Hosting, RPC, giám sát | $800 | $2,000 | $4,000 |
| Tài trợ phí gas | $200 | $500 | $1,000 |
| **Tổng hằng tháng** | **≈ $2,900** | **≈ $8,200** | **≈ $17,800** |

## Tổng chi phí sở hữu tham khảo trong 12 tháng (bên ngoài)

| | Thấp | Cơ sở | Cao |
|---|--:|--:|--:|
| Chi phí một lần | $32,000 | $65,000 | $100,000 |
| 12 × chi phí hằng tháng | $34,700 | $98,200 | $214,200 |
| **Tổng tham khảo 12 tháng** | **≈ $67,000** | **≈ $163,000** | **≈ $314,000** |

Các yếu tố có thể làm thay đổi đáng kể nhất các số liệu trên:

- **Quy mô mạng lưới.** Gói Network của MLM Soft áp dụng cho tối đa 3,000 tài khoản có phát sinh hoa hồng; số tài khoản hoạt động lớn hơn sẽ chuyển sang giá Enterprise (B).
- **Khối lượng ví.** Giá trả theo mức sử dụng của Privy khi vượt 10,000 người dùng hoạt động hằng tháng là $2,000 cộng $0.05 cho mỗi người dùng (X); giá Enterprise được đàm phán riêng.
- **Nhà cung cấp ví.** Phương án thay thế Turnkey kết hợp Alchemy được tính giá theo từng chữ ký và từng đơn vị tính toán (Turnkey $0.05 mỗi chữ ký ở gói Pro, X), nên chi phí tăng theo khối lượng giao dịch thay vì theo số người dùng hoạt động hằng tháng; ở quy mô thí điểm, chi phí dự kiến nằm trong khoảng giá của Privy nêu trên (U).
- **Kịch bản KYC.** Kịch bản A làm tăng chi phí xác minh; kịch bản C làm giảm chi phí này nhưng đóng lại kênh fiat và làm tăng các rủi ro khác.
- **Giám sát giao dịch thương mại.** Chainalysis, TRM và Elliptic không công bố giá; các nguồn bên thứ ba cho thấy hợp đồng hằng năm ở mức năm chữ số (chưa xác minh).
- **Vận hành Sản phẩm sinh lợi** đòi hỏi thêm việc rà soát kiểm toán đối với các vault được chọn và mọi lớp bọc thu phí (fee wrapper), và có thể cả kiểm toán hợp đồng thông minh.

## Nguồn lực theo hạng mục công việc (người-tháng)

Nguồn lực kỹ thuật không đồng nghĩa với thời gian thực hiện. Việc mua sắm từ nhà cung cấp, phê duyệt của nhà cung cấp dịch vụ và rà soát pháp lý diễn ra song song và không thể rút ngắn bằng cách bổ sung nhân sự.

| Hạng mục công việc | Mốc 30 ngày | Lũy kế đến thí điểm có kiểm soát |
|---|--:|--:|
| Quản lý triển khai và kiến trúc giải pháp | 1.0 | 2.5 |
| Tích hợp lõi MLM và cấu hình kế hoạch trả thưởng | 1.0 | 2.5 |
| Tích hợp ví và treasury (Privy, chính sách, quorum) | 0.75 | 1.5 |
| Sổ cái, phát hiện Khoản nạp và đối soát | 1.0 | 3.0 |
| Ứng dụng web cho Thành viên | 1.5 | 3.5 |
| Back office quản trị (vai trò, phê duyệt, kiểm toán, liên kết hồ sơ xử lý) | 1.0 | 2.5 |
| Tích hợp KYC và sàng lọc | 0.5 | 1.0 |
| Cấu hình và tích hợp helpdesk | 0.5 | 1.25 |
| QA, bộ kiểm thử Hoa hồng và tự động hóa kiểm thử | 1.0 | 2.5 |
| DevOps, kỹ thuật bảo mật và giám sát | 0.75 | 2.0 |
| **Tổng** | **9.0** | **22.25** |

Tất cả số liệu là ước tính của tư vấn (U). Số liệu mốc 30 ngày giả định Khách hàng đưa ra các quyết định tại mục 11 ngay trong tuần 1; nếu không, công việc cấu hình kế hoạch trả thưởng sẽ bị chậm lại.

## Đội ngũ triển khai tối thiểu

| Vai trò | FTE | Trách nhiệm |
|---|--:|---|
| Trưởng nhóm triển khai | 1.0 | Kế hoạch, điều phối nhà cung cấp, nhật ký quyết định, đánh giá mức độ sẵn sàng |
| Kiến trúc sư giải pháp kiêm trưởng nhóm blockchain | 1.0 | Kiến trúc, thiết kế ví và treasury, kiểm soát lưu ký |
| Kỹ sư backend | 2.0 | Sổ cái, đối soát, tích hợp MLM và KYC |
| Kỹ sư ví và blockchain | 1.0 | Tích hợp Privy, chính sách, indexer, tài trợ phí gas |
| Kỹ sư frontend | 2.0 | Ứng dụng web cho Thành viên và back office quản trị |
| Kỹ sư QA | 1.0 | Bộ kiểm thử Hoa hồng, kiểm thử đầu-cuối và kiểm thử tình huống bất lợi |
| Kỹ sư DevOps và bảo mật | 0.75 | Môi trường, quản lý bí mật, giám sát, công cụ xử lý sự cố |
| **Tổng phía Cyclone** | **≈ 8.75** | |
| Khách hàng: chủ sở hữu sản phẩm | 0.5 | Cơ chế sản phẩm, điều khoản Thành viên, quyết định về kế hoạch trả thưởng |
| Khách hàng: phụ trách tuân thủ | 0.5 | Kịch bản KYC, chính sách, đầu mối làm việc với luật sư tư vấn |
| Khách hàng: trưởng bộ phận vận hành và hỗ trợ | 0.5–1.0 | Quy trình hỗ trợ, rà soát cơ sở tri thức, phê duyệt tài chính |
| Bên ngoài: luật sư tư vấn | Theo hợp đồng thuê | Các câu hỏi tại mục 10 |

## Các phụ thuộc và đường găng

Đường găng dẫn tới việc tiếp nhận tiền thật phụ thuộc vào các quyết định và phê duyệt hơn là vào công việc kỹ thuật:

1. **Quyết định của Khách hàng** (tuần 1): cơ sở tính hoa hồng, thị trường mục tiêu, kịch bản KYC, người phê duyệt treasury.
2. **Đánh giá tính chất pháp lý** của kế hoạch trả thưởng, mô hình lưu ký và các ngưỡng KYC (ước tính bốn đến sáu tuần kể từ khi thuê luật sư; nằm ngoài tầm kiểm soát của Cyclone).
3. **Chấp thuận của nhà cung cấp và ký kết hợp đồng**: văn bản chấp thuận mô hình MLM và điều khoản Enterprise của Privy; hợp đồng và bằng chứng bảo mật của MLM Soft; tiếp nhận của nhà cung cấp KYC (mỗi bên đều tiến hành thẩm định doanh nghiệp riêng).
4. **Đặc tả kế hoạch trả thưởng** với đầy đủ tỷ lệ và cơ sở tính hoa hồng đã được xác nhận, sau đó cấu hình và kiểm thử theo bộ kiểm thử Hoa hồng.
5. **Chứng minh đối soát sổ cái** trên mạng thử nghiệm (testnet), sau đó trong một đợt diễn tập nhỏ bằng tiền thật sử dụng vốn của nhà vận hành.
6. **Kiểm thử xâm nhập và rà soát ví độc lập**, với các phát hiện mức độ nghiêm trọng cao đã được khắc phục.
7. **Đánh giá go/no-go** theo các tiêu chí sẵn sàng tại mục 8.

Các bước 2 và 3 thường quyết định ngày ra mắt. Bộ phận kỹ thuật có thể hoàn thành mốc 30 ngày song song, nhưng việc tiếp nhận tiền thật phải chờ cả hai bước này.
