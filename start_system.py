#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EtherSentinel 系统启动脚本
用于启动增强后端API服务和前端界面
"""

import os
import sys
import time
import subprocess
import webbrowser
from pathlib import Path

def check_dependencies():
    """检查系统依赖"""
    try:
        import pandas
        import numpy
        import sklearn
        import flask
        print("✅ 所有依赖包已安装")
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖包: {e}")
        print("请运行: pip install -r requirements_enhanced.txt")
        return False

def start_backend():
    """启动增强后端服务"""
    print("🚀 启动 EtherSentinel 增强后端...")
    
    # 检查钓鱼数据文件
    phishing_file = Path("../phishing_label.csv")
    if phishing_file.exists():
        print(f"✅ 找到钓鱼地址数据文件: {phishing_file}")
    else:
        print("⚠️  未找到钓鱼地址数据文件，将使用示例数据")
    
    # 启动后端服务
    backend_process = subprocess.Popen([
        sys.executable, 'enhanced_backend.py'
    ], cwd=os.getcwd())
    
    return backend_process

def start_frontend():
    """启动前端服务（通过简单HTTP服务器）"""
    print("🌐 启动前端服务...")
    
    # 使用Python内置HTTP服务器
    frontend_process = subprocess.Popen([
        sys.executable, '-m', 'http.server', '8080'
    ], cwd=os.getcwd())
    
    return frontend_process

def main():
    """主启动函数"""
    print("=" * 60)
    print("🛡️  EtherSentinel 区块链安全检测平台启动器")
    print("=" * 60)
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 启动后端
    backend_process = start_backend()
    print("⏳ 等待后端服务启动...")
    time.sleep(3)
    
    # 启动前端
    frontend_process = start_frontend()
    print("⏳ 等待前端服务启动...")
    time.sleep(2)
    
    # 打开浏览器
    print("🌐 打开浏览器...")
    time.sleep(1)
    webbrowser.open('http://localhost:8080/auth.html')
    
    print("\n" + "=" * 60)
    print("✅ 系统启动完成!")
    print("📍 前端界面: http://localhost:8080/auth.html")
    print("🔧 后端API: http://localhost:5008")
    print("👤 登录凭据: admin / admin123")
    print("=" * 60)
    print("\n📊 可用的检测数据:")
    print("   • 2,882个已标记的钓鱼地址")
    print("   • 3.38亿条历史交易记录特征")
    print("   • 14维机器学习特征向量")
    print("   • 实时风险评分和检测")
    print("\n🔍 支持的检测功能:")
    print("   • 地址风险检测 (基于黑名单+ML模型)")
    print("   • 交易安全甄别 (发送方+接收方综合分析)")
    print("   • 智能合约代码分析 (函数去混淆)")
    print("   • 实时威胁监控 (流式数据处理)")
    print("\n按 Ctrl+C 停止服务")
    
    try:
        # 保持服务运行
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹️  正在停止服务...")
        backend_process.terminate()
        frontend_process.terminate()
        print("✅ 服务已停止")

if __name__ == "__main__":
    main() 