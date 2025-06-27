from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import json
import time
from datetime import datetime, timezone, timedelta
import random
import hashlib

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # 启用跨域请求支持

# 设置中国时区
CHINA_TZ = timezone(timedelta(hours=8))

def get_current_time():
    """获取当前中国时间"""
    return datetime.now(CHINA_TZ)

# 区块链地址风险评估类
class BlockchainAddressRiskAnalyzer:
    def __init__(self):
        # 定义风险类型映射
        self.risk_mapping = {
            'phishing_activities': '钓鱼活动',
            'blacklist_doubt': '黑名单地址',
            'malicious_contract': '恶意合约',
            'stealing_attack': '盗窃活动',
            'honeypot_related_address': '蜜罐相关地址',
            'fake_kyc': '假冒身份认证',
            'mixer': '混币活动',
            'darkweb_transactions': '暗网交易',
            'money_laundering': '洗钱活动',
            'sanctioned': '被制裁地址',
            'financial_crime': '金融犯罪',
            'cybercrime': '网络犯罪',
            'blackmail_activities': '勒索活动',
            'scam': '诈骗活动',
        }
        
        # 定义风险详情说明
        self.risk_details_mapping = {
            'phishing_activities': {
                'title': '钓鱼活动风险',
                'description': '该地址被检测到与钓鱼网站或钓鱼邮件活动相关。这类攻击通常试图欺骗用户透露敏感信息，如私钥或助记词。',
                'recommendations': [
                    '不要向此地址发送任何资金',
                    '不要与此地址关联的任何智能合约交互',
                    '将此地址加入您的个人黑名单'
                ],
                'severity': '高'
            },
            'blacklist_doubt': {
                'title': '黑名单地址风险',
                'description': '该地址出现在一个或多个知名区块链安全组织的黑名单中，可能与欺诈、盗窃或其他恶意活动有关。',
                'recommendations': [
                    '避免与此地址进行任何交易',
                    '如果您已经与此地址交互，请密切监控您的资金',
                    '考虑将您的资金转移到一个新的、安全的钱包地址'
                ],
                'severity': '高'
            },
            'malicious_contract': {
                'title': '恶意合约风险',
                'description': '该地址部署或与已知的恶意智能合约交互。这类合约可能包含后门、漏洞或其他可利用的安全缺陷。',
                'recommendations': [
                    '不要调用此地址部署的任何智能合约函数',
                    '撤销对此地址或其合约的任何授权',
                    '使用多签名钱包或硬件钱包来增强安全性'
                ],
                'severity': '严重'
            },
            'stealing_attack': {
                'title': '盗窃活动风险',
                'description': '该地址与盗窃用户资金的活动相关。可能通过漏洞利用、钓鱼或其他欺诈手段获取用户资产。',
                'recommendations': [
                    '立即撤销对此地址的任何授权',
                    '确保您的钱包安全，考虑更换新钱包',
                    '向相关执法机构或安全组织报告此地址'
                ],
                'severity': '严重'
            }
        }
        
        # 为其他风险类型添加默认详情
        for risk in self.risk_mapping:
            if risk not in self.risk_details_mapping:
                self.risk_details_mapping[risk] = {
                    'title': f'{self.risk_mapping[risk]}风险',
                    'description': f'该地址被检测到与{self.risk_mapping[risk]}相关的可疑活动。',
                    'recommendations': [
                        '谨慎与此地址交互',
                        '在进行大额交易前进行额外验证',
                        '监控与此地址相关的交易'
                    ],
                    'severity': '中'
                }
        
        # 示例黑名单地址集合
        self.known_malicious_addresses = [
            '0x12345',  # 前缀匹配
            '0xabcde',
            '0x54321',
            '0x1234567890abcdef',
            '0xdeadbeef'
        ]
    
    # 评估地址风险
    def evaluate_risk(self, address):
        # 模拟API调用延迟
        time.sleep(1)
        risks = self._analyze_address(address)
        address_details = self._get_address_details(address)
        
        return {
            'address': address,
            'risks': risks,
            'addressInfo': address_details,
            'riskLevel': self._calculate_risk_level(risks),
            'timestamp': get_current_time().isoformat()
        }
    
    # 模拟地址风险分析
    def _analyze_address(self, address):
        risks = []
        address_hash = self._calculate_address_hash(address)
        
        # 通过哈希值确定风险项，模拟真实API的行为
        # 1. 检查是否在已知黑名单中
        if self._is_in_blacklist(address):
            risks.append('blacklist_doubt')
        
        # 2. 基于地址哈希值随机确定是否有其他风险
        risk_types = list(self.risk_mapping.keys())
        
        # 避免过多风险项，并模拟大部分地址是安全的
        max_risks = 0 if address_hash % 6 == 0 else (address_hash % 3) + 1
        
        if max_risks > 0:
            # 生成不重复的随机风险项
            selected_risks = set()
            
            while len(selected_risks) < max_risks and len(selected_risks) < len(risk_types):
                risk_index = (address_hash * (len(selected_risks) + 1)) % len(risk_types)
                risk_type = risk_types[risk_index]
                
                # 避免重复添加blacklist_doubt
                if risk_type != 'blacklist_doubt' or 'blacklist_doubt' not in risks:
                    selected_risks.add(risk_type)
            
            # 将选定的风险项添加到结果中
            for risk in selected_risks:
                if risk not in risks:
                    risks.append(risk)
        
        return risks
    
    # 计算地址相关信息
    def _get_address_details(self, address):
        address_hash = self._calculate_address_hash(address)
        
        # 模拟地址余额（ETH）
        balance = round((address_hash % 1000) / 100, 4)
        
        # 模拟ETH当前价格
        eth_price = 3892.64
        
        # 计算美元价值
        value = f"${round(balance * eth_price, 2)} (@ ${eth_price}/ETH)"
        
        # 模拟最后一次交易信息
        last_txn_days = 10 + (address_hash % 300)
        last_txn = f"0x{address[2:10]}...{address[-6:]} (from {last_txn_days} days ago)"
        
        # 模拟第一次交易信息
        first_txn_days = last_txn_days + 30 + (address_hash % 400)
        first_txn = f"0x{address[-8:]}...{address[2:6]} (from {first_txn_days} days ago)"
        
        return {
            'balance': str(balance),
            'value': value,
            'lastTxn': last_txn,
            'firstTxn': first_txn
        }
    
    # 检查地址是否在黑名单中
    def _is_in_blacklist(self, address):
        # 简单的前缀匹配
        for bad_address in self.known_malicious_addresses:
            if address.lower().startswith(bad_address.lower()):
                return True
        
        # 基于地址哈希值的随机判断
        address_hash = self._calculate_address_hash(address)
        return address_hash % 10 == 1  # 10%的概率为黑名单地址
    
    # 计算地址的哈希值（用于生成一致的随机结果）
    def _calculate_address_hash(self, address):
        hash_value = 0
        for i, char in enumerate(address):
            hash_value = ((hash_value << 5) - hash_value) + ord(char)
            hash_value = hash_value & 0xffffffff  # 转换为32位整数
        return abs(hash_value)
    
    # 计算综合风险等级
    def _calculate_risk_level(self, risks):
        if len(risks) == 0:
            return '安全'
        elif len(risks) == 1:
            return '低风险'
        elif len(risks) == 2:
            return '中风险'
        elif len(risks) == 3:
            return '高风险'
        else:
            return '严重风险'
    
    # 获取本地化风险描述
    def get_risk_description(self, risk_type):
        return self.risk_mapping.get(risk_type, risk_type)
    
    # 获取风险详情
    def get_risk_details(self, risk_type):
        return self.risk_details_mapping.get(risk_type, {
            'title': f'未知风险: {risk_type}',
            'description': '未能找到此风险类型的详细描述。',
            'recommendations': ['建议谨慎处理'],
            'severity': '未知'
        })

# 交易风险分析类
class TransactionRiskAnalyzer:
    def __init__(self):
        self.risk_patterns = [
            '钓鱼活动',
            '恶意合约调用',
            '可疑转账模式',
            '洗钱行为',
            '高频小额转账',
            '异常Gas费用',
            '智能合约漏洞利用'
        ]
    
    def analyze_transaction(self, tx_hash):
        # 模拟分析延迟
        time.sleep(1.5)
        
        # 基于交易哈希生成一致的分析结果
        hash_value = self._calculate_tx_hash(tx_hash)
        
        # 90%的交易是安全的
        is_safe = hash_value % 10 != 1
        
        risks = []
        if not is_safe:
            # 随机选择1-2个风险模式
            num_risks = (hash_value % 2) + 1
            for i in range(num_risks):
                risk_index = (hash_value + i) % len(self.risk_patterns)
                risks.append(self.risk_patterns[risk_index])
        
        return {
            'txHash': tx_hash,
            'isSafe': is_safe,
            'risks': risks,
            'timestamp': get_current_time().isoformat(),
            'analysisDetails': self._get_transaction_details(tx_hash, hash_value)
        }
    
    def _calculate_tx_hash(self, tx_hash):
        hash_value = 0
        for char in tx_hash:
            hash_value = ((hash_value << 5) - hash_value) + ord(char)
            hash_value = hash_value & 0xffffffff
        return abs(hash_value)
    
    def _get_transaction_details(self, tx_hash, hash_value):
        return {
            'fromAddress': f"0x{hash_value:08x}...{(hash_value * 2) & 0xffffff:06x}",
            'toAddress': f"0x{(hash_value * 3) & 0xffffff:06x}...{(hash_value * 4) & 0xffffff:06x}",
            'value': f"{round((hash_value % 1000) / 100, 4)} ETH",
            'gasUsed': f"{21000 + (hash_value % 50000):,}",
            'blockNumber': 18500000 + (hash_value % 100000)
        }

# 代码生成和智能合约分析类
class CodeAnalyzer:
    def __init__(self):
        self.sample_contract_data = {
            'is_contract': True,
            'goplus': 'stealing attack',
            'code': "{'_dispatcher': 'function _dispatcher', '_fallback': 'function _fallback payable view pure', 'withdraw()': 'function withdraw()', '0x5b1e3b51': 'function 0x5b1e3b51 payable view', '0x5fe2e4d1': 'function 0x5fe2e4d1 payable view', 'withdraw(address,uint256)': 'function withdraw(address,uint256) view'}"
        }
    
    def generate_function_names(self):
        # 模拟代码处理延迟
        time.sleep(1)
        
        # 格式化代码数据
        processed_data = {
            'is_contract': self.sample_contract_data['is_contract'],
            'goplus': self.sample_contract_data['goplus'],
            'code': self._format_code_functions(self.sample_contract_data['code'])
        }
        
        return {
            'original': self.sample_contract_data,
            'processed': processed_data,
            'timestamp': get_current_time().isoformat()
        }
    
    def _format_code_functions(self, code_string):
        # 简单的代码格式化
        try:
            # 解析代码字符串并重新格式化
            formatted = code_string.replace("', '", "',\n    '")
            formatted = formatted.replace("{'", "{\n    '")
            formatted = formatted.replace("'}", "'\n}")
            return formatted
        except:
            return code_string

# 实时数据生成器
class RealTimeDataGenerator:
    def __init__(self):
        self.chars = 'abcdef0123456789'
    
    def generate_transaction_data(self, count=10):
        transactions = []
        
        for i in range(count):
            # 生成随机交易数据
            tx_hash = '0x' + ''.join(random.choice(self.chars) for _ in range(18)) + '...'
            from_addr = '0x' + ''.join(random.choice(self.chars) for _ in range(18)) + '...'
            to_addr = '0x' + ''.join(random.choice(self.chars) for _ in range(18)) + '...'
            
            # 大部分交易是安全的
            is_risk = random.random() < 0.15  # 15%的概率是风险交易
            
            transactions.append({
                'hash': tx_hash,
                'from': from_addr,
                'to': to_addr,
                'isRisk': is_risk,
                'timestamp': get_current_time().isoformat()
            })
        
        return transactions

# 创建分析器实例
address_analyzer = BlockchainAddressRiskAnalyzer()
transaction_analyzer = TransactionRiskAnalyzer()
code_analyzer = CodeAnalyzer()
data_generator = RealTimeDataGenerator()

# 用户认证配置
VALID_CREDENTIALS = {
    'admin': 'admin123'
}

# 路由: 主页 - 重定向到index.html
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# 路由: 静态文件服务
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# API: 用户登录验证
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': '缺少用户名或密码'}), 400
    
    username = data['username']
    password = data['password']
    
    if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
        return jsonify({
            'success': True,
            'message': '登录成功',
            'username': username,
            'timestamp': get_current_time().isoformat()
        })
    else:
        return jsonify({'error': '用户名或密码错误'}), 401

# API: 检查地址风险
@app.route('/api/check_address_risk', methods=['POST'])
def check_address_risk():
    data = request.get_json()
    
    if not data or 'address' not in data:
        return jsonify({'error': '缺少地址参数'}), 400
    
    address = data['address']
    
    # 验证地址格式
    if not address.startswith('0x') or len(address) < 10:
        return jsonify({'error': '无效的以太坊地址格式'}), 400
    
    try:
        # 评估地址风险
        result = address_analyzer.evaluate_risk(address)
        
        # 将风险类型转换为可读文本并获取详情
        readable_risks = []
        risk_details = {}
        
        for risk in result['risks']:
            readable_risk = address_analyzer.get_risk_description(risk)
            readable_risks.append(readable_risk)
            risk_details[readable_risk] = address_analyzer.get_risk_details(risk)
        
        # 构建响应
        response = {
            'address': result['address'],
            'risks': readable_risks,
            'addressInfo': result['addressInfo'],
            'riskLevel': result['riskLevel'],
            'riskDetails': risk_details,
            'timestamp': result['timestamp']
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': f'风险评估失败: {str(e)}'}), 500

# API: 检查交易风险
@app.route('/api/check_transaction_risk', methods=['POST'])
def check_transaction_risk():
    data = request.get_json()
    
    if not data or 'txHash' not in data:
        return jsonify({'error': '缺少交易哈希参数'}), 400
    
    tx_hash = data['txHash']
    
    # 验证交易哈希格式
    if not tx_hash.startswith('0x') or len(tx_hash) < 10:
        return jsonify({'error': '无效的交易哈希格式'}), 400
    
    try:
        # 分析交易风险
        result = transaction_analyzer.analyze_transaction(tx_hash)
        
        return jsonify({
            'txHash': result['txHash'],
            'status': 'success',
            'isSafe': result['isSafe'],
            'risks': result['risks'],
            'analysisDetails': result['analysisDetails'],
            'timestamp': result['timestamp']
        })
    
    except Exception as e:
        return jsonify({'error': f'交易风险评估失败: {str(e)}'}), 500

# API: 代码生成和函数名处理
@app.route('/api/generate_code', methods=['POST'])
def generate_code():
    try:
        # 生成处理后的代码
        result = code_analyzer.generate_function_names()
        
        return jsonify({
            'status': 'success',
            'original': result['original'],
            'processed': result['processed'],
            'timestamp': result['timestamp']
        })
    
    except Exception as e:
        return jsonify({'error': f'代码生成失败: {str(e)}'}), 500

# API: 获取实时交易数据
@app.route('/api/get_realtime_data', methods=['GET'])
def get_realtime_data():
    try:
        # 获取交易数量参数
        count = request.args.get('count', 10, type=int)
        count = min(max(count, 1), 50)  # 限制在1-50之间
        
        # 生成实时交易数据
        transactions = data_generator.generate_transaction_data(count)
        
        return jsonify({
            'status': 'success',
            'data': transactions,
            'count': len(transactions),
            'timestamp': get_current_time().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'获取实时数据失败: {str(e)}'}), 500

# API: 获取系统统计信息
@app.route('/api/get_system_stats', methods=['GET'])
def get_system_stats():
    try:
        # 模拟系统统计数据
        stats = {
            'totalAddressesChecked': 50234,
            'totalTransactionsAnalyzed': 1256789,
            'threatsDetected': 2847,
            'detectionAccuracy': 99.2,
            'systemUptime': '99.8%',
            'lastUpdated': get_current_time().isoformat()
        }
        
        return jsonify({
            'status': 'success',
            'stats': stats,
            'timestamp': get_current_time().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'获取统计数据失败: {str(e)}'}), 500

# API: 获取威胁情报
@app.route('/api/get_threat_intelligence', methods=['GET'])
def get_threat_intelligence():
    try:
        # 模拟威胁情报数据
        now = get_current_time()
        threats = [
            {
                'type': '钓鱼网站',
                'address': '0x742d...a8c2',
                'riskLevel': '高危',
                'detectedTime': (now - timedelta(hours=1)).strftime('%Y-%m-%d %H:%M'),
                'status': '已处理'
            },
            {
                'type': '洗钱活动',
                'address': '0x1a2b...f3e4',
                'riskLevel': '高危',
                'detectedTime': (now - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M'),
                'status': '监控中'
            },
            {
                'type': '可疑转账',
                'address': '0x9c8d...b7a6',
                'riskLevel': '中危',
                'detectedTime': (now - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M'),
                'status': '待分析'
            }
        ]
        
        return jsonify({
            'status': 'success',
            'threats': threats,
            'timestamp': get_current_time().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': f'获取威胁情报失败: {str(e)}'}), 500

# API: 健康检查
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'service': 'EtherSentinel API',
        'version': '2.0.0',
        'timestamp': get_current_time().isoformat()
    })

# 错误处理
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': '接口不存在'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': '服务器内部错误'}), 500

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': '请求格式错误'}), 400

# 启动应用
if __name__ == '__main__':
    print("🚀 EtherSentinel 区块链安全监控系统启动中...")
    print("📡 API服务地址: http://localhost:5000")
    print("🌐 前端访问地址: http://localhost:5000")
    print("🔐 登录凭证: 用户名: admin, 密码: admin123")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000) 