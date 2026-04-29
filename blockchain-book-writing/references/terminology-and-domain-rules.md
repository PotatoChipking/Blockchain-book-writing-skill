# Terminology and Domain Rules

Keep terminology consistent within a chapter and across adjacent chapters.

## Key Distinctions

### 联盟链 vs 许可链

- 联盟链 emphasizes multi-institution governance.
- 许可链 emphasizes access control.
- They may overlap in enterprise financial settings but are not identical.

### 稳定币 vs 代币化存款

- 稳定币 usually refers to an on-chain pegged asset, often issued by a non-bank institution.
- 代币化存款 usually represents a bank liability expressed on-chain.
- They differ in regulatory treatment, issuer, balance-sheet relationship, and settlement logic.

### 支付型 Layer-1 vs 通用 Layer-1

- 支付型 Layer-1 emphasizes low latency, settlement efficiency, stablecoin payment, merchant access, and compliance.
- 通用 Layer-1 emphasizes smart-contract ecosystems, open execution, and developer networks.

### RWA vs 数字资产

- RWA emphasizes on-chain representation of real-world assets.
- 数字资产 is broader and may include native tokens, NFTs, credentials, points, data assets, and other digital objects.

### 隐私 vs 匿名

- 隐私 emphasizes minimal disclosure, data isolation, and controlled visibility.
- 匿名 emphasizes identity non-recognition.
- Financial infrastructure usually needs regulated privacy, not full anonymity.

### 可审计性 vs 公开透明

- 可审计性 means verifiable and traceable under authorized conditions.
- 公开透明 means information is visible to everyone.
- Consortium chains and financial networks often require selective transparency rather than full public visibility.

## Financial Infrastructure Chapters

For stablecoins, payments, RWA, tokenized deposits, institutional financial networks, and cross-border settlement, cover relevant items from this list:

- 资产发行主体
- 资产负债属性
- 结算最终性
- 清算机制
- 合规准入
- KYC / AML / 制裁筛查
- 隐私保护
- 审计机制
- 多机构治理
- 跨链互操作
- 钱包与账户体系
- 链上链下协同
- 监管可见性
- 商户或机构接入成本
- 与传统支付系统、银行系统、RTGS、ACH、SWIFT 等体系的关系

Do not analyze financial infrastructure only from the angle that on-chain transfer is faster.

## Consortium Chain Chapters

For consortium-chain topics, cover relevant items from this list:

- 多机构共同治理
- 节点准入机制
- 权限控制
- 身份认证
- 数据隔离
- 共识机制
- 隐私交易
- 审计追踪
- 监管节点
- 链上链下数据一致性
- 系统可用性
- 运维治理
- 与业务系统集成
- 智能合约生命周期管理
- 性能与可扩展性
- 灾备和容错

Do not simply apply public-chain logic to consortium chains.

## Public Chain Chapters

For public-chain topics, cover relevant items from this list:

- 去中心化程度
- 开放准入
- 共识机制
- 执行环境
- 状态模型
- 费用模型
- MEV
- 开发者生态
- 安全模型
- 治理机制
- 资产发行与流动性
- 跨链桥和互操作
- 性能与去中心化之间的权衡

Do not explain public chains only through consortium-chain governance and access-control logic.

## Data Elements and Trusted Storage Chapters

For data elements, trusted storage, notarization, verifiable data, and privacy computing, cover relevant items from this list:

- 数据确权
- 数据可信采集
- 数据哈希与摘要
- Merkle 证明
- 时间戳
- 存证机制
- 可验证查询
- 隐私保护
- 数据授权
- 数据流通过程中的审计
- 链上链下数据一致性
- 原始数据不宜直接上链的原因
- 可信执行环境、多方安全计算、零知识证明等技术的适用边界

Do not imply that putting data on-chain automatically makes it trustworthy.
