# Các phát hiện chính và ràng buộc

## "Staking" bao hàm sáu cơ chế khác nhau

Tài liệu của Khách hàng dùng từ "staking" cho bất kỳ sản phẩm nào trả lợi nhuận trên crypto đã nạp. Các cơ chế đằng sau từ này khác nhau về rủi ro, mô hình lưu ký và đặc điểm pháp lý. Báo cáo này dùng **Sản phẩm sinh lợi (Yield Product)** làm thuật ngữ bao trùm và chỉ dùng **Staking** cho staking gốc (native staking) và liquid staking theo cơ chế proof-of-stake.

| Loại | Ví dụ | Nguồn lợi nhuận | Nền tảng có phải kiểm soát tiền? | Thanh khoản | Rủi ro chính |
|---|---|---|---|---|---|
| Staking gốc | Validator ETH qua Kiln, Figment hoặc Coinbase; ủy thác (delegation) SOL hoặc HYPE | Phần thưởng giao thức cho việc bảo mật mạng lưới | Không, nếu ví của từng Thành viên tự ký | Thời gian hủy staking (unbonding) của từng chuỗi; HYPE có thời gian khóa 1 ngày và hàng chờ 7 ngày | Giá token, slashing, nhà cung cấp bị xâm phạm |
| Liquid staking | Lido stETH, Rocket Pool rETH, Jito JitoSOL | Cùng phần thưởng giao thức đó, thông qua một token biên nhận có thể giao dịch | Không | Bán trên thị trường (giá có thể chênh lệch) hoặc qua hàng chờ của giao thức | Token biên nhận mất neo giá, rủi ro smart contract |
| Cho vay (lending) | Aave; vault Morpho do Steakhouse hoặc Gauntlet quản lý (curate) | Lãi do người vay trả, với tài sản thế chấp bằng crypto | Không, nếu tài sản được cung cấp từ ví của Thành viên | Thường rút được ngay, giới hạn bởi thanh khoản sẵn có | Smart contract, oracle, nợ xấu, sai sót của đơn vị quản lý vault (curator) |
| Vault giao dịch | HLP và các vault người dùng của Hyperliquid | Lãi và lỗ từ giao dịch | Không (người nạp nắm giữ phần sở hữu trong vault) | HLP khóa 4 ngày; vault người dùng 1 ngày | **Mất vốn gốc**, thao túng thị trường |
| Chương trình do nhà vận hành quản lý | Các chương trình "earn" có lưu ký; một chiến lược do QUANT vận hành | Bất kỳ hoạt động nào nhà vận hành thực hiện với nguồn tiền gộp | **Có** | Theo điều khoản của nhà vận hành; có thể bị tạm dừng | Nhà vận hành thất bại, trộn lẫn tài sản, mức độ nhạy cảm pháp lý cao nhất |
| Công cụ tính lợi nhuận | Các gói "staking", "ROI" hoặc "daily return" trong phần mềm MLM | **Không có.** Chỉ là một con số được ghi có trong cơ sở dữ liệu | Nhà vận hành nắm giữ tiền | Phụ thuộc vào Khoản nạp mới | Động lực kiểu Ponzi và kim tự tháp; không phải Sản phẩm sinh lợi |

Nguồn: [Hyperliquid staking](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/staking), [Hyperliquid protocol vaults](https://hyperliquid.gitbook.io/hyperliquid-docs/hypercore/vaults/protocol-vaults), [Aave v3 overview](https://aave.com/docs/aave-v3/overview), [Cloud MLM investment plan](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/).

Các điểm chính đối với AlphaWave:

- **Đối với một sản phẩm tính bằng đô la, cho vay stablecoin có thế chấp vượt mức là cơ chế đáng tin cậy nhất.** Lãi đến từ người vay, và vị thế của Thành viên vẫn nằm trong ví của Thành viên. Morpho cho biết Coinbase, Kraken và Deel tích hợp vault Morpho (tuyên bố của nhà cung cấp).
- **HLP của Hyperliquid là vault giao dịch, không phải Staking.** Báo chí ghi nhận ba sự cố thua lỗ trong năm 2025, lần lượt khoảng 4 triệu USD, 12–13.5 triệu USD (chưa thực hiện) và 4.9 triệu USD (chưa đối chiếu với công bố của Hyperliquid). Các báo cáo kiểm toán Hyperliquid đã công bố chỉ bao gồm cầu nối (bridge) thế hệ cũ, không bao gồm công cụ khớp lệnh hay logic của HLP ([trang kiểm toán](https://hyperliquid.gitbook.io/hyperliquid-docs/audits), đã xác minh).
- **Các nhà cung cấp bên thứ ba mang rủi ro vận hành thực tế.** Vào tháng 9 năm 2025, một API của Kiln bị xâm phạm đã bị lợi dụng để đánh cắp khoảng 41 triệu USD SOL từ chương trình do nhà vận hành quản lý của SwissBorg ([SwissBorg](https://swissborg.com/blog/swissborg-security-update-kiln-breach), đã xác minh). Vào tháng 3 năm 2026, một lỗi cấu hình oracle của Aave đã thanh lý nhầm 34 tài khoản; người dùng được DAO bồi hoàn ([báo cáo sau sự cố](https://governance.aave.com/t/post-mortem-exchange-rate-misallignment-on-wsteth-core-and-prime-instances/24269), đã xác minh). Vào tháng 4 năm 2026, vụ khai thác lỗ hổng cầu nối rsETH của Kelp khiến Aave thiếu hụt một lượng lớn WETH. Một gói bù đắp đã được đề xuất và gây tranh cãi; đến tháng 5, phần lớn lượng rsETH không có tài sản bảo chứng đã được thu hồi thông qua thanh lý, với một liên minh các giao thức cam kết bù đắp phần còn lại ([chuỗi thảo luận về sự cố](https://governance.aave.com/t/rseth-incident-2026-04-18/24481), [Aave Labs May update](https://governance.aave.com/t/al-development-update-may-2026/25013); việc hoàn tất cuối cùng chưa được xác minh).
- **Các mô-đun tính lợi nhuận không thể chấp nhận làm Sản phẩm sinh lợi.** Vụ việc SEC xử lý Forsage liên quan đến chính kiểu thiết kế này ([SEC 2022-134](https://www.sec.gov/newsroom/press-releases/2022-134)).

## Các nhà cung cấp dịch vụ thanh toán cấm MLM

Mối lo ngại của nhóm dự án về Stripe là có cơ sở, và đây là vấn đề chung của toàn ngành chứ không riêng Stripe.

- **Stripe** liệt kê "Pyramid schemes" và "Multilevel marketing services offering commission or recruitment-based sales" là các loại hình kinh doanh **bị cấm**, cùng với "Cryptocurrency mining and staking" (trang được cập nhật ngày 22 tháng 9 năm 2026). Điều khoản dành cho merchant của Crypto Onramp (§5.4) ràng buộc nền tảng tích hợp phải tuân theo danh sách đó, và Stripe có thể tạm ngừng quyền truy cập mà không cần báo trước. Đã xác minh: [Stripe prohibited and restricted businesses](https://stripe.com/legal/restricted-businesses), [Crypto Onramp merchant terms](https://stripe.com/legal/crypto-onramp/merchant-terms).
- **Bridge** (một công ty thuộc Stripe, cung cấp nền tảng cho các tính năng fiat và lưu ký của Privy) liệt kê "multi-level marketing" trong số các hoạt động bị cấm tại §2.1.1 của [Developer Agreement](https://www.bridge.xyz/legal/developer-agreement). Đã xác minh.

| Nhà cung cấp | Nội dung về MLM trong điều khoản | Tình trạng bằng chứng |
|---|---|---|
| Stripe (bao gồm Crypto Onramp) | "Multilevel marketing services offering commission or recruitment-based sales"; "Pyramid schemes" | Đã xác minh |
| Bridge (Stripe) | "multi-level marketing" | Đã xác minh |
| Coinbase Developer Platform | "Multi-level Marketing: Pyramid schemes, network marketing, and referral marketing programs" | Đã xác minh (bản lưu trữ) |
| Transak | "Multi-level marketing" | Đã xác minh |
| Banxa | "Multi-level marketing: pyramid schemes, network marketing, and referral marketing programs" | Đã xác minh (điều khoản tháng 12 năm 2024) |
| Ramp Network | "multi-level marketing" nằm trong các ngành đối tác bị hạn chế | Đã xác minh (nguồn năm 2022; điều khoản hiện hành cần được xác nhận) |
| MoonPay | Điều khoản dành cho người tiêu dùng cấm "certain multi-level marketing programs"; điều khoản dành cho đối tác không công khai | Xác minh một phần |
| Mercuryo | "Ponzi or pyramid schemes" | Đã xác minh |
| Privy | Không có nội dung về MLM; cấm trình bày sai lệch "the nature of the business" | Đã xác minh |
| Onramper (nền tảng tổng hợp) | Không có nội dung về MLM; điều khoản của các nhà cung cấp nền tảng vẫn được áp dụng | Đã xác minh (không có nội dung) |

Không nhà cung cấp nào được rà soát công bố tuyên bố khẳng định rằng họ chấp nhận doanh nghiệp MLM. Mọi sự chấp thuận đều phải được thể hiện bằng văn bản sau khi mô hình được công bố đầy đủ.

**Hệ quả:**

- **Release 1 chỉ chấp nhận Khoản nạp bằng crypto.** Thành viên chuyển crypto từ ví hoặc sàn giao dịch mà họ đang sử dụng. Đối tác on-ramp không thể đóng luồng này. Tuy nhiên, luồng này không loại bỏ các nghĩa vụ KYC hay AML.
- **On-ramp fiat là hạng mục Giai đoạn 2 có điều kiện.** Hạng mục này đòi hỏi luật sư tư vấn xác định tính chất pháp lý của kế hoạch trả thưởng, công bố đầy đủ mô hình MLM trong quá trình nhà cung cấp rà soát, và có văn bản chấp thuận từ ít nhất hai nhà cung cấp hoặc từ một nền tảng tổng hợp cùng hai nhà cung cấp nền tảng.
- **Trực tiếp nhận fiat** (nhận thanh toán bằng thẻ hoặc chuyển khoản ngân hàng rồi quy đổi) kéo theo các vấn đề về giấy phép, bồi hoàn (chargeback), bảo vệ tài sản khách hàng và đối soát ba bên, và thuộc về giai đoạn sau.

## Tính chất lưu ký được xác định bởi quyền kiểm soát, không phải bởi tên gọi

Một mô hình chỉ là phi lưu ký khi không bên nào ngoài Thành viên có thể chuyển tài sản của Thành viên mà không có sự phê duyệt của Thành viên cho từng thao tác. Ví nhúng (embedded wallet), tính toán đa bên (MPC) và smart account là các cơ chế; việc ai nắm giữ thẩm quyền ký mới quyết định cách phân loại.

| Mô hình | Ai có thể ký | Phân loại đối với Thành viên |
|---|---|---|
| Ví nhúng Privy, thuộc sở hữu của Thành viên, không có signer của nền tảng | Thành viên, cùng phần khóa trong enclave của Privy | Phi lưu ký (phụ thuộc vào nhà cung cấp) |
| Ví nhúng Privy có signer của nền tảng bị giới hạn bởi chính sách | Thành viên, hoặc nền tảng trong phạm vi chính sách | **Kết hợp (hybrid)** |
| Signer của nền tảng với quyền hạn rộng | Trên thực tế là nền tảng | Về bản chất là lưu ký |
| Key quorum yêu cầu cả Thành viên và nền tảng | Cả hai | Phi lưu ký đối với dòng tiền ra, nền tảng có quyền phủ quyết |
| Vault MPC của nhà vận hành (Fireblocks, Cobo, BitGo) | Nhà vận hành, được nhà cung cấp đồng ký | **Lưu ký** (nhà vận hành là bên lưu ký) |
| Bên lưu ký thứ ba được cấp phép | Bên lưu ký, theo chỉ thị của nhà vận hành | Lưu ký (bên thứ ba) |

Các nhà cung cấp quảng bá vault MPC là "self-custody" hàm ý tự lưu ký đối với doanh nghiệp, không phải đối với khách hàng của doanh nghiệp đó. **Chi trả hoa hồng đòi hỏi một ví treasury của nhà vận hành trong mọi mô hình, và ví treasury đó luôn mang tính lưu ký.** Lựa chọn thiết kế thực chất là quyết định Khoản nạp của Thành viên được đặt ở đâu.

Các cơ quan quản lý áp dụng cùng một phép thử. FATF coi mọi doanh nghiệp có "control" đối với tài sản ảo là nhà cung cấp dịch vụ tài sản ảo (VASP), bao gồm cả trường hợp kiểm soát chung hoặc kiểm soát đa chữ ký ([FATF 2021 guidance](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Guidance-rba-virtual-assets-2021.html), đoạn 72–76). FinCEN coi một nhà cung cấp là đơn vị chuyển tiền "regardless of the label the person applies to itself" ([FIN-2019-G001](https://www.fincen.gov/sites/default/files/2019-05/FinCEN%20Guidance%20CVC%20FINAL%20508.pdf), §4.2). Định nghĩa về lưu ký trong MiCA của EU bao gồm việc kiểm soát "the means of access" đối với tài sản crypto ([MiCA](https://eur-lex.europa.eu/eli/reg/2023/1114/oj), Art. 3(1)(17)). Đây chỉ là các ví dụ; việc chế định nào được áp dụng do luật sư tư vấn xác định.

## KYC: ba kịch bản

Giả định của Khách hàng rằng Khoản nạp bằng crypto không cần KYC không thể được xác nhận từ phía phần mềm. Đối với VASP, ngưỡng FATF cho các giao dịch không thường xuyên là USD/EUR 1,000 và Travel Rule được áp dụng (hướng dẫn của FATF, đoạn 146). Chẳng hạn, Quy định về Chuyển tiền (Transfer of Funds Regulation) của EU bao gồm cả các giao dịch chuyển đến ví tự lưu ký và không có số tiền tối thiểu đối với crypto ([TFR](https://eur-lex.europa.eu/eli/reg/2023/1113/oj)).

| | A: KYC khi đăng ký | **B: KYC phân tầng (kịch bản cơ sở)** | C: Chỉ crypto, không KYC |
|---|---|---|---|
| Trải nghiệm Thành viên | Kiểm tra giấy tờ và xác thực người thật (liveness) trước bất kỳ Khoản nạp nào | Kiểm tra nhẹ khi đăng ký; kiểm tra đầy đủ được kích hoạt theo các ngưỡng (Khoản nạp, lần rút tiền đầu tiên, Hoa hồng đã nhận, quyền truy cập Sản phẩm sinh lợi) | Chỉ đăng ký bằng ví |
| Công cụ | Xác minh danh tính, sàng lọc AML, sàng lọc ví, quản lý hồ sơ | Như A, cộng thêm công cụ phân tầng và logic ngưỡng trong sổ cái | Chỉ sàng lọc ví |
| On-ramp fiat | Nhà cung cấp vẫn tự thực hiện KYC | Tương tự | Kênh này trên thực tế bị đóng |
| Chi trả hoa hồng | Biết danh tính người nhận | KYC đầy đủ trước khi chi trả vượt ngưỡng | Chi trả cho ví ẩn danh; rủi ro về trừng phạt, tài khoản trùng lặp và thu hồi hoa hồng (clawback) |
| Khả năng tiếp cận nhà cung cấp và ngân hàng | Dễ giải trình nhất | Có thể giải trình với các ngưỡng được luật sư tư vấn phê duyệt | Có thể bị chặn quan hệ lưu ký, ngân hàng và thanh toán |
| Khả năng điều chỉnh | Có thể nới lỏng về sau | Có thể tinh chỉnh ngưỡng | Khó thắt chặt sau khi ra mắt |

**Dù theo kịch bản nào, mọi địa chỉ nguồn của Khoản nạp, địa chỉ rút tiền và địa chỉ nhận chi trả đều cần được sàng lọc danh sách trừng phạt ngay từ ngày đầu.** [Chainalysis sanctions oracle](https://go.chainalysis.com/chainalysis-oracle-docs.html) miễn phí là mức tối thiểu. Các cổng kiểm soát danh tính nên được xây dựng ngay trong Release 1, kể cả trước khi xác định các ngưỡng; việc bổ sung KYC sau khi Thành viên đã nạp tiền khó hơn so với việc kích hoạt một tầng đã có sẵn.

## Cơ sở tính hoa hồng: những gì phần mềm thực sự hỗ trợ

Bản tổng quan kế hoạch trả thưởng trả Hoa hồng dựa trên doanh số gói thuê bao (subscription). Mô hình đó đã bị thay thế và cơ sở tính mới chưa được xác định. Thay vì đề xuất một cơ sở tính từ các nguyên lý ban đầu, nghiên cứu đã xem xét những gì phần mềm MLM thực tế hỗ trợ.

| Cơ sở tính | Bằng chứng từ nhà cung cấp | Tình trạng | Nhận xét |
|---|---|---|---|
| Đơn hàng sản phẩm | Exigo, ByDesign, DirectScale được tổ chức xoay quanh đơn hàng và sản phẩm | Đã xác minh (tài liệu) | Mặc định của các nền tảng doanh nghiệp; cơ sở tính không dựa trên sản phẩm cần đến đơn hàng giả lập |
| Số tiền Khoản nạp ("đầu tư") | Hybrid MLM: "Commissions are earned when a recruit makes an initial investment"; Cloud MLM: "daily percentage returns based on individual member investments" | Đã xác minh (theo mô tả) | **Cơ sở tính phổ biến nhất trong phần mềm crypto-MLM.** Phần thưởng được tài trợ bằng Khoản nạp mới là mô thức cấu trúc đứng sau các lo ngại về Ponzi và kim tự tháp |
| "ROI" được tính toán | Hybrid MLM: "whenever a recruit's investment generates ROI" | Đã xác minh (theo mô tả) | Bản thân "ROI" là một con số do nhà vận hành đặt, không phải lợi suất từ giao thức |
| Phí gia nhập hoặc phí gói | ARM MLM "Forsage clone": "Pay 0.5 ETH to join" | Đã xác minh (theo mô tả) | Mô thức mà SEC cáo buộc trong vụ Forsage |
| Hoạt động giao dịch | Epixel: "new trader registration or ... the first trade" | Tuyên bố của nhà cung cấp | Chỉ phù hợp nếu tích hợp giao dịch ở giai đoạn sau |
| Số tiền tùy ý từ nền tảng, chẳng hạn doanh thu phí | MLM Soft: các thuộc tính kế hoạch được đánh dấu là volume hoặc bonus có thể được "set by API request" | Đã xác minh (tài liệu của nhà cung cấp); cần demo | Lộ trình duy nhất tìm thấy để dùng **doanh thu phí của nền tảng** làm cơ sở tính |

Nguồn: [Hybrid MLM](https://www.hybridmlm.io/investment-mlm-plan/), [Cloud MLM](https://cloudmlmsoftware.com/mlm-plan/investment-mlm-plan/), [ARM MLM](https://www.armmlm.com/tron-smart-contract-mlm-software/), [Epixel](https://www.epixelmlmsoftware.com/cryptocurrency-trading-mlm-software), [MLM Soft plan properties](https://help.mlmsoft.net/hc/en-us/articles/39249705385235-Plan-properties-configuration).

**Có tồn tại một nguồn doanh thu phí phi lưu ký.** Privy Earn đưa tiền của Thành viên vào các vault Morpho hoặc Aave và cho phép nền tảng hưởng tối đa 50% (Morpho) hoặc tối đa 100% (Aave) **chỉ trên phần lợi suất**; Thành viên giữ nguyên vốn gốc và có thể rút bất kỳ lúc nào ([Privy revenue sharing](https://docs.privy.io/wallets/actions/earn/revenue-sharing), đã xác minh). Một kế hoạch trong đó Hoa hồng là một tỷ lệ có mức trần trên doanh thu phí đã thực hiện của nền tảng, và được giữ lại trong một khoảng thời gian trước khi chi trả, là phương án có rủi ro cấu trúc thấp nhất trong số các phương án được tìm thấy. Phương án này vẫn cần luật sư tư vấn xem xét, vì cả việc lựa chọn nguồn lợi suất lẫn việc chi trả Hoa hồng gắn với nguồn đó đều đặt ra các câu hỏi pháp lý tại nhiều khu vực pháp lý (xem vụ việc SEC xử lý "Earn Interest Program" của Celsius, [SEC 2023-133](https://www.sec.gov/newsroom/press-releases/2023-133)).

Khách hàng cần xác nhận cơ sở tính trước khi có thể cấu hình hoặc kiểm thử kế hoạch trả thưởng (mục 11).
