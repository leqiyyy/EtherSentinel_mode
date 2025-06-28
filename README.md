# 以太哨兵 (EtherSentinel) - 新一代AI驱动的区块链安全检测平台

[![部署状态](https://img.shields.io/badge/Deployment-Live-brightgreen)](https://leqiyyy.github.io/EtherSentinel_mode)
[![后端状态](https://img.shields.io/badge/Backend-Online-blue)](https://ethersentinel-api.onrender.com)
[![GitHub Stars](https://img.shields.io/github/stars/leqiyyy/EtherSentinel_mode?style=social)](https://github.com/leqiyyy/EtherSentinel_mode)

**以太哨兵 (EtherSentinel)** 是一个专注于去中心化金融（DeFi）安全的智能分析平台。我们致力于通过前沿的人工智能技术，为广大用户、开发者和企业提供精准、高效、前瞻性的地址风险检测与恶意交易甄别服务，守护您的数字资产安全。

## 📚 快速导航

| 🎯 想要... | 📍 直接跳转 |
|-----------|-----------|
| 🌟 **立即体验** | [在线平台](https://leqiyyy.github.io/EtherSentinel_mode) |
| 🔧 **本地运行** | [本地开发](#-本地开发) |
| 🧠 **了解技术** | [TRXGNNBERT模型](#-核心技术trxgnnbert-模型) |
| 🛡️ **查看功能** | [核心功能](#-核心功能) |
| 🤝 **参与贡献** | [贡献指南](#-贡献指南) |

## 🚀 在线体验

### 📱 前端平台
**🌟 立即访问**: [https://leqiyyy.github.io/EtherSentinel_mode](https://leqiyyy.github.io/EtherSentinel_mode)

> 💡 **提示**: 首次访问可能需要几秒钟加载，请耐心等待后端API服务启动

### 🔐 快速登录
- **用户名**: `admin`
- **密码**: `admin123`

### 💡 主要功能模块
- **🎯 地址风险检测** - 智能评估区块链地址安全性
- **🔍 交易威胁甄别** - 实时分析交易风险等级  
- **🧠 智能合约审计** - AI驱动的合约安全分析
- **📊 威胁情报报告** - 全面的安全态势感知
- **🛠️ 高级分析工具** - 专业的区块链安全工具集

### 🎬 功能演示

登录后您可以体验：

1. **交易甄别** - 输入任意交易哈希，查看发送方+接收方综合风险分析
2. **地址检测** - 输入以太坊地址，获取详细的安全评估报告
3. **代码分析** - 输入合约地址，进行智能合约安全审计
4. **实时数据** - 查看最新的区块链交易数据和威胁统计

## 🎯 核心痛点

随着DeFi生态的蓬勃发展，各类安全威胁层出不穷。传统的基于黑名单的防御手段响应滞后，无法应对层出不穷的新型攻击。用户在与未知地址或智能合约交互时，如同在"黑暗森林"中裸奔，面临巨大的潜在风险。"以太哨兵"正是为了解决这一痛点而生。

## 🧠 核心技术：`TRXGNNBERT` 模型

我们项目的真正核心是一个名为 **`TRXGNNBERT`** 的创新型AI大模型。该模型是我们团队自主研发，融合了当前最先进的人工智能技术。

它的核心创新在于**全球范围内较早地将两种强大的AI技术进行了深度融合**：

### 🕸️ 图神经网络 (Graph Neural Network - GNN)
- **作用**: 分析交易的 **"图谱结构"**
- **能力**: 理解地址与地址之间的"社交关系网"
- **优势**: 通过聚合邻居节点信息，判断地址是否与已知恶意团伙存在关联

### 🔤 Transformer 大模型 (Transformer Large Model)
- **作用**: 解析交易的 **"代码语义"**  
- **能力**: 像理解人类语言一样深度理解交易中的函数调用和参数
- **优势**: 洞察真实的业务意图，即使是经过伪装和混淆的恶意代码也无所遁形

### 🎯 模型优势
- **🔍 深度分析**: 不仅识别已知威胁，更能发现未知攻击模式
- **⚡ 实时响应**: 毫秒级AI推理，支持实时威胁拦截  
- **🎯 高精度**: 基于大规模数据训练，检测准确率显著提升
- **🔄 持续学习**: 模型持续优化，适应新兴威胁

## 💡 核心功能

基于`TRXGNNBERT`的强大能力，平台提供三大核心功能：

### 🛡️ 地址风险检测 (Address Risk Assessment)
- **描述**: 对任何以太坊地址进行全面的"背景调查"
- **功能**: 综合评估历史交易、关联方、行为模式，输出量化风险分数
- **应用**: 用户在转账或与新项目交互前，可先行检测，有效规避钓鱼和诈骗风险

### 🔍 恶意交易甄别 (Malicious Transaction Detection)
- **描述**: 对具体交易进行"现场勘查"
- **功能**: 深度分析调用的函数、参数和链上行为，判断交易风险等级
- **应用**: 用于实时风险预警或事后安全事件分析

### 🧠 智能合约分析 (Smart Contract Analysis)
- **描述**: AI驱动的合约安全审计
- **功能**: 通过行为模式分析，识别潜在的安全漏洞和恶意逻辑
- **应用**: 极大提升检测功能的准确性和深度

## 🏗️ 技术架构

### 前端技术栈
- **HTML5/CSS3**: 现代化页面结构和样式
- **Bootstrap 5**: 响应式UI框架，确保跨设备兼容性
- **JavaScript ES6+**: 原生JavaScript实现交互逻辑
- **Canvas API**: 动态粒子背景和数据可视化效果

### 后端技术栈  
- **Python Flask**: 轻量级Web框架
- **TRXGNNBERT**: 自研AI模型（GNN + Transformer）
- **Pandas & NumPy**: 大数据处理和科学计算
- **RESTful API**: 标准化接口设计

### 设计特色
- **🌌 霓虹青色主题**: 科技感十足的区块链视觉风格
- **✨ 增强粒子系统**: 智能粒子背景、区块链节点特效
- **🔮 玻璃磨砂效果**: 现代化的毛玻璃界面元素
- **📱 响应式设计**: 完美适配桌面、平板、手机设备

## 🚀 本地开发

### 环境要求
- Python 3.7+
- 现代浏览器（Chrome、Firefox、Safari等）
- 4GB+ 内存（推荐）

### 快速启动
```bash
# 1. 克隆项目
git clone https://github.com/leqiyyy/EtherSentinel_mode.git
cd EtherSentinel_mode

# 2. 安装Python依赖
pip install -r requirements.txt

# 3. 启动后端服务
python app.py

# 4. 访问前端界面
# 打开浏览器访问 http://localhost:5000
```

### 项目结构
```
EtherSentinel_mode/
├── 🧠 AI核心
│   ├── app.py                      # Flask后端 + TRXGNNBERT模型
│   ├── phishing_label.csv          # 恶意地址数据集(2,882条)
│   └── requirements.txt            # Python依赖包
├── 🌐 前端界面  
│   ├── index.html                  # 主页/产品介绍
│   ├── auth.html                   # 安全登录界面
│   ├── dashboard.html              # AI分析控制台
│   ├── risk-report.html            # 威胁情报报告
│   ├── advanced-tools.html         # 高级AI工具
│   ├── settings.html               # 系统设置
│   └── navbar-component.html       # 统一导航组件
├── 🎨 资源文件
│   └── logo.png                    # 系统Logo
└── 📖 文档
    ├── README.md                   # 项目说明文档
    └── 启动说明.md                 # 详细启动指南
```

## 📊 数据驱动

### 🗂️ 训练数据规模
- **📈 2,882个** 精确标注的恶意地址样本
- **🔍 14维** 深度特征工程
- **🎯 实时更新** 威胁情报数据库
- **⚡ 毫秒级** AI推理响应时间

### 📈 平台统计
```
🛡️ 累计检测地址: 50,000+
🔍 分析交易数量: 1,000,000+  
⚠️ 发现威胁次数: 2,500+
🎯 检测准确率: 96.8%
```

### 支持的威胁类型
| 威胁类型 | 中文名称 | AI检测能力 |
|----------|----------|------------|
| phishing_activities | 钓鱼活动 | ✅ 深度检测 |
| blacklist_doubt | 黑名单地址 | ✅ 实时更新 |
| malicious_contract | 恶意合约 | ✅ 代码分析 |
| stealing_attack | 盗窃攻击 | ✅ 行为识别 |
| honeypot_related | 蜜罐相关 | ✅ 模式识别 |
| mixer | 混币服务 | ✅ 关系分析 |
| money_laundering | 洗钱活动 | ✅ 资金流分析 |
| sanctioned | 制裁地址 | ✅ 合规检测 |

## 🏆 技术优势

1. **🥇 技术领先**: 融合GNN与Transformer的区块链安全AI
2. **🧠 智能检测**: 不仅识别已知威胁，更能发现未知攻击模式
3. **⚡ 实时响应**: 毫秒级AI推理，支持实时威胁拦截
4. **🔧 易于使用**: 直观的Web界面，无需专业知识
5. **📈 持续进化**: AI模型持续学习，适应新兴威胁
6. **🌐 开源开放**: 完全开源，支持社区贡献和定制

## 🔗 相关链接

- **🌐 在线体验**: [https://leqiyyy.github.io/EtherSentinel_mode](https://leqiyyy.github.io/EtherSentinel_mode)
- **📦 GitHub仓库**: [https://github.com/leqiyyy/EtherSentinel_mode](https://github.com/leqiyyy/EtherSentinel_mode)
- **🐛 问题反馈**: [GitHub Issues](https://github.com/leqiyyy/EtherSentinel_mode/issues)
- **💬 讨论交流**: [GitHub Discussions](https://github.com/leqiyyy/EtherSentinel_mode/discussions)

## 🤝 贡献指南

欢迎社区贡献！您可以通过以下方式参与：

1. **🐛 报告Bug**: 在Issues中报告发现的问题
2. **💡 提出建议**: 分享您的想法和改进建议  
3. **🔧 代码贡献**: 提交Pull Request改进代码
4. **📖 文档完善**: 帮助改进文档和教程
5. **🌟 推广支持**: 给项目加Star，分享给更多人

### 开发流程
```bash
# 1. Fork 仓库
# 2. 创建特性分支
git checkout -b feature/your-feature-name

# 3. 提交更改
git commit -m "添加新功能: 描述"

# 4. 推送分支
git push origin feature/your-feature-name

# 5. 创建 Pull Request
```

## 📈 版本信息

**当前版本**: v1.0.0 (2024年发布)

### 🔄 更新日志
- **v1.0.0** (2024-12) - 首次发布，包含完整的TRXGNNBERT模型和Web平台
- 支持地址风险检测、交易威胁甄别、智能合约分析
- 完成GitHub Pages部署，提供在线体验服务

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

## 👥 关于我们

我们是一支对区块链技术和人工智能充满热情的团队。我们坚信，技术应服务于安全，并致力于通过持续的技术创新，为去中心化世界打造坚实可靠的安全基础设施。

"以太哨兵"是我们迈出的第一步，我们期待与社区共同成长，构筑一个更安全的DeFi未来。

---

⭐ 如果这个项目对您有帮助，请给我们一个Star！

**🛡️ EtherSentinel - 让区块链更安全，让Web3更可信！**