# Các phương án kiến trúc và luồng tiền

Ba cách tiếp cận đã được so sánh theo yêu cầu của bản mô tả nhiệm vụ. Mọi phương án đều tuân theo cùng một nguyên tắc: **sổ cái nền tảng do Cyclone sở hữu là nguồn dữ liệu gốc duy nhất về tài chính.** Phần mềm MLM tính Hoa hồng (Commission), lớp ví thực hiện chuyển tiền, còn helpdesk và CRM (nếu có) chỉ lưu mã tham chiếu.

## Phương án 1: Nền tảng MLM white-label tích hợp

Một nhà cung cấp duy nhất (Epixel hoặc Cloud MLM) cung cấp cổng thông tin Thành viên, công cụ tính hoa hồng, ví điện tử nội bộ, cổng thanh toán crypto và bảng điều khiển quản trị. Cyclone gắn thương hiệu (white-label) và tùy chỉnh giải pháp này.

![Phương án 1: kiến trúc và luồng tiền. Phần mềm của nhà cung cấp nắm giữ số dư và thực hiện chi trả; việc lưu ký nằm ở một cổng thanh toán không có tài liệu mô tả hoặc một cổng thanh toán lưu ký.](figures/vi/opt1-integrated){width=100%}

| Khía cạnh | Đánh giá |
|---|---|
| Ai kiểm soát tài sản | Cổng thanh toán của nhà cung cấp, hoặc một đơn vị xử lý lưu ký như CoinPayments. Không ứng viên nào mô tả bằng tài liệu về thẩm quyền ký. |
| Ai cung cấp sản phẩm tài chính | Mô-đun "ROI/staking" của nhà cung cấp, vốn chỉ tính toán lợi nhuận. **Mô-đun này phải được tắt**, dẫn đến không có Sản phẩm sinh lợi (Yield Product) nào. |
| Ai xử lý lệnh rút tiền | Phần mềm của nhà cung cấp, thông qua cổng thanh toán của họ. |
| Nguồn dữ liệu gốc | Danh tính, phả hệ, số dư, giao dịch và Hoa hồng đều nằm trong cơ sở dữ liệu của nhà cung cấp. |
| Mua, cấu hình, xây dựng | Mua và cấu hình gói phần mềm của nhà cung cấp; tùy chỉnh cổng thông tin; xây dựng rất ít. |
| Lộ trình tới fiat | Thông qua các đối tác cổng thanh toán của nhà cung cấp, vốn chịu cùng các lệnh cấm MLM như nêu tại mục 3.2. |
| Khả năng thay thế | Thấp. Số dư, phả hệ và chi trả bị gắn chặt với một nhà cung cấp. Giấy phép mã nguồn của Cloud MLM giảm nhẹ vấn đề này nhưng chuyển trách nhiệm bảo mật sang Cyclone. |
| Độ phức tạp và tiến độ | Có cổng thông tin hiển thị nhanh nhất (vài tuần), nhưng khoảng trống về kiểm soát không thể khắc phục bằng cấu hình. |
| Rủi ro trọng yếu | Mô hình lưu ký không có tài liệu; các tuyên bố "smart contract" chưa được xác minh; tuyên bố ISO đã hết hiệu lực hoặc không nhất quán; nội dung tiếp thị của nhà cung cấp hứa hẹn lợi nhuận. |
| Điều kiện trước khi dùng tiền thật | Nhà cung cấp chứng minh mô hình lưu ký, cung cấp địa chỉ hợp đồng và báo cáo kiểm toán; có chứng thực bảo mật còn hiệu lực; thay thế cổng thanh toán bằng lớp ví do AlphaWave kiểm soát, và khi đó phương án này trở thành Phương án 2. |

**Đánh giá: không khuyến nghị cho tiền thật.** Phương án này chỉ hữu ích như một nguồn dự phòng cho cổng thông tin Thành viên hoặc công cụ tính hoa hồng trong Phương án 2.

## Phương án 2: Kiến trúc mô-đun (khuyến nghị)

AlphaWave mua một lõi MLM headless, một lớp ví, công cụ xác minh và một helpdesk; Cyclone xây dựng ứng dụng Thành viên, back office quản trị, sổ cái và lớp tích hợp.

![Phương án 2: kiến trúc tổng thể. Cyclone xây dựng lớp ứng dụng và sổ cái; các thành phần chuyên biệt được mua ngoài.](figures/vi/opt2-architecture){width=100%}

![Phương án 2: luồng tiền. Khoản nạp của Thành viên nằm trong ví do Thành viên sở hữu; chi trả hoa hồng được thực hiện từ một ví treasury riêng của nhà vận hành theo cơ chế phê duyệt nhiều người; một Sản phẩm sinh lợi ở giai đoạn sau giữ cổ phần vault trong ví của Thành viên và chỉ trả cho nền tảng một phần lợi suất.](figures/vi/opt2-fundflow){width=100%}

| Khía cạnh | Đánh giá |
|---|---|
| Ai kiểm soát tài sản | **Khoản nạp của Thành viên:** Thành viên, thông qua ví nhúng (embedded wallet) Privy. Nếu bổ sung một signer (khóa ký) của nền tảng với phạm vi hẹp để nạp vào vault, mô hình trở thành kết hợp (hybrid). **Treasury:** nhà vận hành, với cơ chế phê duyệt theo quorum. |
| Ai cung cấp sản phẩm tài chính | Release 1 (bản phát hành đầu tiên): không có sản phẩm nào dùng tiền thật. Giai đoạn sau: một giao thức cho vay (lending) hoặc Staking được nêu tên cụ thể, thông qua yield adapter (ví dụ Privy Earn vào các vault Morpho hoặc Aave). |
| Ai xử lý lệnh rút tiền | Thành viên tự ký lệnh rút tiền từ ví của mình. Chi trả hoa hồng do ví treasury của nhà vận hành thực hiện sau khi được phê duyệt theo cơ chế maker-checker. |
| Nguồn dữ liệu gốc | Trạng thái danh tính: nhà cung cấp dịch vụ xác minh (hồ sơ bằng chứng) và dịch vụ danh tính của nền tảng (hồ sơ quyết định). Phả hệ và tính toán Hoa hồng: lõi MLM. Số dư và giao dịch: sổ cái nền tảng, được đối soát với dữ liệu on-chain. Chi trả hoa hồng: sổ cái. |
| Mua | Lõi MLM (MLM Soft hoặc Exigo); hạ tầng ví (Privy); công cụ treasury (Privy key quorum, Cobo hoặc Fireblocks); KYC và sàng lọc (Sumsub hoặc Didit, Chainalysis oracle); nhà cung cấp chain indexer hoặc RPC; helpdesk. |
| Cấu hình | Kế hoạch trả thưởng (compensation plan); chính sách ví; các cấp KYC; hàng đợi và SLA của helpdesk. |
| Xây dựng | Ứng dụng web cho Thành viên; back office quản trị; sổ cái và đối soát; lớp tích hợp với xử lý sự kiện idempotent, cơ chế thử lại webhook và feature gate; giao diện yield adapter. |
| Lộ trình tới fiat | Một giao diện nạp tiền trung lập với nhà cung cấp cho phép bổ sung on-ramp (cổng chuyển fiat sang crypto) ở Giai đoạn 2, sau khi các nhà cung cấp chấp thuận mô hình bằng văn bản. |
| Khả năng thay thế | Cao. Mỗi thành phần nằm sau một giao diện của Cyclone: công cụ MLM nhận sự kiện và trả về kết quả Hoa hồng; lớp ví thực hiện các lệnh chuyển đã ký; yield adapter trừu tượng hóa các nhà cung cấp. QUANT có thể được bổ sung hoặc gỡ bỏ mà không ảnh hưởng đến lõi. Privy hỗ trợ xuất khóa, tạo lối thoát cho Thành viên. |
| Độ phức tạp và tiến độ | Công sức tích hợp cao nhất trong ba phương án, nhưng mọi thành phần đều là tiêu chuẩn. Khoảng 9 người-tháng để đạt mốc 30 ngày và khoảng 22 người-tháng để đến giai đoạn thí điểm có kiểm soát. |
| Rủi ro trọng yếu | Bằng chứng bảo mật của MLM Soft; việc Privy chấp nhận mô hình MLM và mức giá Enterprise; cách phân loại signer kết hợp; chi phí gas cho ví của từng Thành viên; thu hồi hoa hồng (clawback) không thể cưỡng chế on-chain sau khi đã chi trả. |
| Điều kiện trước khi dùng tiền thật | Xem mục 8.2. |

Các nguyên tắc thiết kế chính của Phương án 2:

- **Tách biệt treasury khỏi ví của Thành viên.** Khóa ký của treasury không bao giờ nằm trên cùng máy chủ với bất kỳ signer nào của nền tảng được dùng cho ví Thành viên.
- **Mọi signer của nền tảng đều bị giới hạn theo chính sách** ở các phương thức vault đã được phê duyệt, kèm mức trần số tiền và thời hạn hiệu lực, và không bao giờ được chuyển tiền tới địa chỉ không thuộc Thành viên. Signer này được lưu giữ trong mô-đun bảo mật phần cứng (HSM) hoặc dịch vụ quản lý khóa (KMS).
- **Khoản nạp được phát hiện hai lần**: qua webhook của nhà cung cấp ví và qua một indexer độc lập, loại trùng theo chuỗi (chain), mã băm giao dịch và chỉ số log, với ngưỡng xác nhận riêng cho từng chuỗi.
- **Việc tính Hoa hồng tách biệt với chi trả.** Lõi MLM phát lệnh chi trả; sổ cái ghi nhận; treasury thực hiện các lô đã được phê duyệt; thu hồi hoa hồng được áp dụng trước khi chi trả, vì vậy nên có thời gian tạm giữ.
- **Không dùng tính năng nào của Privy phụ thuộc vào Stripe hoặc Bridge**: không tài khoản fiat, không ví lưu ký, không chi trả fiat và không on-ramp Stripe.

## Phương án 3: Tích hợp QUANT ở Giai đoạn 2

Công cụ giao dịch của QUANT là tùy chọn và không thuộc bản phát hành đầu tiên. Nếu sau này AlphaWave cung cấp dịch vụ giao dịch thuật toán, việc tích hợp cần giữ công cụ này tách biệt khỏi số dư chính của Thành viên.

![Phương án 3: tích hợp QUANT ở Giai đoạn 2. Thành viên tự nguyện tham gia một tài khoản giao dịch riêng, có giới hạn số tiền; QUANT chỉ nhận một khóa chỉ được phép giao dịch; Cyclone thực thi các hạn mức và công tắc dừng khẩn (kill switch).](figures/vi/opt3-quant){width=100%}

| Khía cạnh | Đánh giá |
|---|---|
| Ai kiểm soát tài sản | Thành viên, thông qua một tài khoản giao dịch riêng mà Thành viên tự nguyện tham gia và nạp một khoản có giới hạn. QUANT không bao giờ có quyền rút tiền. |
| Ai cung cấp sản phẩm tài chính | Chiến lược của QUANT, thực thi trên Hyperliquid. Đây là sản phẩm giao dịch có khả năng mất vốn gốc, không phải Staking. |
| Ai xử lý lệnh rút tiền | Thành viên, từ tài khoản Hyperliquid của chính mình về ví chính. |
| Nguồn dữ liệu gốc | Vị thế và lãi/lỗ (P&L) trên Hyperliquid, được phản ánh vào một sổ cái phụ riêng. |
| Mua, cấu hình, xây dựng | Tích hợp công cụ của QUANT; xây dựng luồng đăng ký tham gia, bộ giám sát rủi ro, hạn mức và công tắc dừng khẩn; cấu hình khóa chỉ giao dịch của Hyperliquid. |
| Lộ trình tới fiat | Như Phương án 2. |
| Khả năng thay thế | Cao nếu QUANT chỉ gửi lệnh thông qua khóa chỉ giao dịch: một nhà cung cấp chiến lược khác có thể thay thế. Hyperliquid có tài liệu mô tả ví agent (API) có thể đặt lệnh nhưng không thể rút tiền; điều này phải được xác nhận trong quá trình thẩm định (due diligence) (chưa được xác minh trong nghiên cứu này). |
| Độ phức tạp và tiến độ | Giai đoạn 2; phụ thuộc vào kết quả thẩm định công cụ, bảo mật và vận hành của QUANT. |
| Rủi ro trọng yếu | Thua lỗ từ chiến lược; thao túng trên sàn (xem các sự cố HLP); công cụ khớp lệnh của Hyperliquid chưa có báo cáo kiểm toán công bố; các sản phẩm giao dịch do nhà vận hành lựa chọn có mức độ nhạy cảm pháp lý cao. |
| Điều kiện trước khi dùng tiền thật | Thẩm định kỹ thuật độc lập đối với QUANT; hạn mức rủi ro bằng văn bản và kiểm thử công tắc dừng khẩn; xác định tính chất pháp lý của sản phẩm; công bố thông tin cho Thành viên; QUANT không bao giờ nhận signer đối với ví chính của Thành viên. |

**Giới hạn đối với Release 1:** không có khoản tiền nào của Thành viên được đưa vào công cụ của QUANT, và không cấp signer ủy quyền nào cho QUANT.

## Lớp ví: Privy và phương án thay thế độc lập với Stripe

Privy là phương án cơ sở vì kết hợp ví nhúng, smart account (tài khoản thông minh), công cụ chính sách (policy engine) và API lợi suất trong một sản phẩm. Quyền sở hữu là mối lo ngại chính: Stripe đã mua lại Privy vào tháng 6 năm 2025, và cả Stripe lẫn Bridge đều cấm MLM. Chính sách sử dụng chấp nhận được của Privy thì không cấm, và thiết kế đã tránh mọi tính năng của Privy vận hành trên Stripe hoặc Bridge. Tuy vậy, vẫn còn rủi ro điều khoản của Privy về sau sẽ được điều chỉnh cho thống nhất với công ty mẹ. Hai phương án thay thế độc lập đã được đánh giá.

| | Privy (phương án cơ sở) | Turnkey + Alchemy Smart Wallets (phương án thay thế khuyến nghị) | Dynamic (phương án thay thế thứ cấp) |
|---|---|---|---|
| Quyền sở hữu | Stripe (đã xác minh) | Cả hai đều độc lập (Turnkey gọi vốn tháng 5 năm 2026, tuyên bố của nhà cung cấp) | Fireblocks, từ tháng 10 năm 2025 (đã xác minh) |
| Mô hình khóa | Secure enclave kết hợp tách khóa 2-of-2 với thông tin đăng nhập của Thành viên | Turnkey: khóa nằm trong AWS Nitro enclave; ký theo các authenticator được xác định trong chính sách (tuyên bố của nhà cung cấp) | MPC 2-of-2 giữa thiết bị của Thành viên và enclave của nhà cung cấp (tuyên bố của nhà cung cấp) |
| Smart account | ERC-4337 và EIP-7702 (đã xác minh, tài liệu) | Alchemy: mặc định EIP-7702, Modular Account v2 (ERC-6900), được ChainLight và Quantstamp kiểm toán (tuyên bố của nhà cung cấp) | ERC-4337 (tuyên bố của nhà cung cấp); EIP-7702 chưa xác minh |
| Giới hạn đối với thao tác của nền tảng | Công cụ chính sách off-chain trong enclave của Privy (Enterprise) | Chính sách Turnkey về số tiền, người nhận, hợp đồng, chuỗi, ủy quyền 7702 và phê duyệt agent Hyperliquid (đã xác minh, tài liệu); **cùng với session key on-chain** có giới hạn về mức chi, hợp đồng, hàm và thời hạn (đã xác minh, tài liệu) | Phần khóa truy cập ủy quyền cho nền tảng (tuyên bố của nhà cung cấp) |
| Lợi suất tích hợp sẵn | Privy Earn: các vault Morpho và Aave với phí trên lợi suất (đã xác minh) | Không có; tích hợp trực tiếp vault ERC-4626, hoặc dùng Kiln DeFi vault có hỗ trợ phí cho bên tích hợp (đã xác minh) | Không có |
| On-ramp tích hợp sẵn | Stripe (mặc định), MoonPay, Meld | Không có trong lõi | Coinbase, Banxa (cả hai đều cấm MLM) |
| Giá công bố | Miễn phí đến $499/tháng; gói Enterprise cần báo giá (đã xác minh) | Turnkey $0.10 mỗi chữ ký, gói Pro $99/tháng với mức $0.05, Enterprise từ $0.0015 (đã xác minh); Alchemy tính theo mức sử dụng cộng phí gas 8%, giá ví theo báo giá | Miễn phí đến $249/tháng, sau đó $0.05 mỗi người dùng; nằm trong gói Fireblocks Essentials với giá $999/tháng (đã xác minh) |
| SOC 2 | Type I/II (tuyên bố của nhà cung cấp) | Turnkey Type II (tuyên bố của nhà cung cấp); Alchemy chưa xác minh | Type II (tuyên bố của nhà cung cấp) |
| Đánh đổi chính | Tích hợp nhanh nhất; rủi ro chính sách từ công ty mẹ | Nhiều công sức tích hợp hơn; giới hạn được thực thi on-chain, dễ chứng minh hơn với luật sư tư vấn | Chuyển câu hỏi về công ty mẹ sang Fireblocks, mà quan điểm về MLM chưa được xác minh |

Nguồn: [Privy pricing](https://www.privy.io/pricing), [Turnkey policies](https://docs.turnkey.com/concepts/policies/overview), [Turnkey pricing](https://www.turnkey.com/pricing), [Alchemy wallets](https://www.alchemy.com/docs/wallets), [Alchemy session keys](https://www.alchemy.com/docs/reference/wallet-apis-session-keys), [Kiln DeFi FAQ](https://docs.kiln.fi/v1/kiln-products/defi/kiln-defi-faq), [Fireblocks acquisition of Dynamic](https://www.fireblocks.com/blog/fireblocks-acquires-dynamic), [Dynamic pricing](https://www.dynamic.xyz/pricing).

Bốn nhà cung cấp smart account khác cũng đã được đánh giá. Không nhà cung cấp nào thuộc sở hữu của một công ty thanh toán hay một sàn giao dịch, và không nhà cung cấp nào nêu tên MLM trong điều khoản của mình.

| Nhà cung cấp | Bản chất | Điểm mạnh đối với Helm | Hạn chế | Mức độ phù hợp |
|---|---|---|---|---|
| **ZeroDev Kernel** (do Offchain Labs, công ty đứng sau Arbitrum, vận hành) | Smart account (ERC-4337, ERC-7579, EIP-7702), phân quyền on-chain, bundler và paymaster | Session key của nền tảng được giới hạn on-chain theo hợp đồng, hàm, đối số, thời hạn và tần suất; khóa riêng tư không bao giờ rời khỏi nền tảng. Có liệt kê HyperEVM. Earn API (beta) cho Aave, Morpho và ERC-4626. Multisig có trọng số cho treasury. Đã công bố báo cáo kiểm toán Kernel v3.x. Gói $69 và $399/tháng; phụ phí gas 8% | Offchain Labs có thể chấm dứt nếu quan hệ "would cause material harm to the reputation of Offchain" (đã xác minh). Earn là "an experimental product offered in beta" và không có tài liệu về phí trên lợi suất (đã xác minh). Không tìm thấy báo cáo kiểm toán cho Kernel v4 | **Phương án thay thế ngang hàng với Alchemy**, kết hợp với Turnkey |
| **Openfort** | Giải pháp trọn gói: ví nhúng, ví backend, công cụ chính sách, paymaster, session key on-chain | Gần nhất với một phương án thay thế Privy trên các mạng EVM; giá khởi điểm công bố thấp nhất | Không hỗ trợ HyperEVM; quyền ký Hyperliquid theo kiểu được tất cả hoặc không có gì; không có bằng chứng SOC 2; chính sách sử dụng được chấp nhận cấm "Ponzi or pyramid schemes" và "securities" không có giấy phép, là cách diễn đạt gần nhất với việc loại trừ mô hình này | Có thể dùng trên các mạng EVM, sau khi được chấp thuận bằng văn bản |
| **Para** (trước đây là Capsule) | Signer khóa (MPC 2-of-2 với một phần khóa trên thiết bị của Thành viên) | Phần khóa nằm trên thiết bị cung cấp cho Thành viên một yếu tố xác thực độc lập | Không phải smart account và không tài trợ phí gas; cần ZeroDev, Alchemy hoặc Pimlico. Các luồng phía máy chủ do nền tảng kiểm soát. Không liệt kê HyperEVM | Không ưu tiên |
| **Pimlico** | Chỉ là hạ tầng bundler và paymaster | Paymaster thứ hai để dự phòng; có liệt kê HyperEVM | Không hỗ trợ EIP-7702 trên HyperEVM; phụ phí tài trợ 10% | Bổ trợ hạ tầng |

Nguồn: [ZeroDev terms](https://zerodev.app/terms), [ZeroDev Kernel](https://github.com/zerodevapp/kernel), [ZeroDev session keys](https://docs.zerodev.app/smart-accounts/permissions/session-keys), [ZeroDev Earn](https://docs.zerodev.app/onramp/earn), [ZeroDev pricing](https://zerodev.app/pricing), [Openfort acceptable use](https://www.openfort.io/acceptable-use-policy), [Openfort HyperEVM](https://www.openfort.io/docs/recipes/hyperliquid/hyperevm), [Openfort pricing](https://www.openfort.io/pricing), [Para terms](https://www.getpara.com/terms-of-service), [Pimlico pricing](https://www.pimlico.io/pricing). Các trích dẫn được đọc thông qua truy xuất tự động và cần được kiểm tra lại trước khi ký hợp đồng.

**Khuyến nghị:**

- Giữ Privy làm phương án cơ sở, với điều kiện Privy chấp thuận mô hình kinh doanh bằng văn bản.
- Duy trì **Turnkey làm signer kết hợp với Alchemy Smart Wallets hoặc ZeroDev Kernel làm lớp tài khoản** như phương án thay thế độc lập với Stripe. ZeroDev mạnh hơn về HyperEVM, công cụ DeFi và giá công bố; điều khoản riêng của Alchemy chưa được rà soát về các quyền chấm dứt tương tự. Lựa chọn giữa hai bên dựa trên câu trả lời bằng văn bản của các nhà cung cấp.
- Thực hiện **một đợt thử nghiệm kỹ thuật (spike) song song giữa Turnkey với Alchemy Smart Wallets hoặc ZeroDev Kernel trong tuần 1**, bao gồm tạo ví, một session key có phạm vi giới hạn ở một vault và một mức trần, một lệnh rút tiền do Thành viên ký và xuất khóa. Lựa chọn lớp ví dựa trên kết quả thử nghiệm và câu trả lời bằng văn bản của các nhà cung cấp.
- Đặt lớp ví sau giao diện riêng của Cyclone để việc chuyển đổi về sau không ảnh hưởng đến sổ cái, tích hợp MLM hay ứng dụng Thành viên. Tính năng xuất khóa cho Thành viên (Privy và Turnkey cung cấp, theo tuyên bố của nhà cung cấp) tạo lối thoát cho Thành viên nếu một nhà cung cấp rút lui.
- Coinbase Developer Platform (nhiều khả năng cấm MLM), MetaMask Embedded Wallets (tài liệu về chính sách sơ sài hơn) và thirdweb (không có bằng chứng SOC 2) đã được đánh giá và không được khuyến nghị.

## So sánh

| Tiêu chí | Phương án 1: Tích hợp | **Phương án 2: Mô-đun** | Phương án 3: QUANT (Giai đoạn 2) |
|---|---|---|---|
| Mức độ rõ ràng về lưu ký | Kém (không có tài liệu) | **Tốt** (ví do Thành viên sở hữu, treasury riêng) | Tốt nếu sử dụng khóa chỉ giao dịch |
| Lộ trình tới Sản phẩm sinh lợi thực chất | Không có (mô-đun chỉ hiển thị) | **Có** (adapter tới các giao thức được nêu tên) | Lợi nhuận giao dịch, không phải lợi suất |
| Bằng chứng kiểm soát | Yếu | **Không đồng đều** (mạnh với Privy và các nhà cung cấp dịch vụ xác minh; MLM Soft chưa được chứng minh) | Chưa xác minh |
| Khả năng thay thế | Thấp | **Cao** | Trung bình |
| Công sức | Thấp nhất | **Cao nhất** | Bổ sung, ở giai đoạn sau |
| Thời gian tới một đợt thí điểm tiền thật đáng tin cậy | Bị chặn bởi khoảng trống kiểm soát | **10–14 tuần (ước tính)** | Sau khi Phương án 2 đi vào vận hành |
| Khuyến nghị | Không dùng cho tiền thật | **Chính** | Giai đoạn 2, có điều kiện |

## Ưu tiên triển khai trên web

**Triển khai ưu tiên trên web là đủ cho bản phát hành đầu tiên, và ứng dụng di động gốc nên được hoãn lại.** Bản thân PRD đã loại ứng dụng di động độc lập khỏi bản phát hành đầu tiên. Một ứng dụng web responsive hoặc progressive web app tiếp cận Thành viên trên trình duyệt di động, và ví nhúng với đăng nhập bằng passkey hoặc email hoạt động được trong trình duyệt. Ứng dụng gốc phát sinh quy trình kiểm duyệt của kho ứng dụng, vốn áp dụng chính sách riêng đối với ứng dụng crypto và MLM, cùng một quy trình phát hành thứ hai, mà không mang lại lợi ích gì cho giai đoạn thí điểm có kiểm soát. Ứng dụng di động có thể triển khai sau khi sản phẩm và vị thế pháp lý đã ổn định.

## Khuyến nghị: phương án chính và phương án dự phòng

- **Phương án chính: Phương án 2 với MLM Soft, Privy và treasury phê duyệt theo quorum.** Đây là phương án duy nhất mang lại ranh giới lưu ký rõ ràng, lộ trình thực chất tới Sản phẩm sinh lợi, các thành phần có thể thay thế và một sổ cái do AlphaWave kiểm soát.
- **Phương án dự phòng: Phương án 2 với các thành phần thay thế**, được kích hoạt bởi các trường hợp thất bại cụ thể:
  - nếu Privy từ chối mô hình kinh doanh, điều khoản Enterprise không chấp nhận được, hoặc quyền sở hữu của Stripe được đánh giá là rủi ro chính sách quá lớn: dùng bộ giải pháp ví độc lập với Stripe gồm Turnkey với Alchemy Smart Wallets hoặc ZeroDev Kernel (mục 6.4), cùng Fireblocks, Cobo hoặc Safe multisig cho treasury;
  - nếu MLM Soft không đạt yêu cầu trong buổi trình diễn hoặc thẩm định bảo mật: dùng Exigo (bằng chứng kiểm soát mạnh hơn, triển khai chậm hơn) hoặc Epixel (tích hợp, các tính năng crypto cần được chứng minh);
  - nếu luật sư tư vấn hoặc bộ phận kinh doanh ưu tiên mô hình omnibus: dùng Fireblocks, Cobo hoặc một tổ chức lưu ký đủ điều kiện như BitGo, chấp nhận việc nhà vận hành trở thành bên lưu ký tài sản của Thành viên cùng các hệ quả về cấp phép kèm theo.

Đánh đổi ở đây là công sức lấy quyền kiểm soát: Phương án 2 đòi hỏi nhiều công sức tích hợp hơn Phương án 1, đổi lại là sự độc lập về lưu ký, dữ liệu và nhà cung cấp mà Phương án 1 không thể mang lại.
