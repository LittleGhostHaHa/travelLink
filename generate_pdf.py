#!/usr/bin/env python3
"""
生成行程规划PDF文件
使用selenium和chrome driver将网页转换为PDF
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def generate_pdf():
    """生成PDF文件"""
    
    # 设置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无头模式
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    
    # 设置打印选项
    print_options = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True,
        'paperWidth': 8.27,  # A4宽度
        'paperHeight': 11.69,  # A4高度
        'marginTop': 0.4,
        'marginBottom': 0.4,
        'marginLeft': 0.4,
        'marginRight': 0.4
    }
    
    try:
        # 初始化Chrome驱动
        print("正在初始化Chrome驱动...")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 打开本地网页
        print("正在加载网页...")
        driver.get('http://localhost:8080')
        
        # 等待页面完全加载
        time.sleep(3)
        
        # 生成PDF
        print("正在生成PDF...")
        pdf_data = driver.execute_cdp_cmd('Page.printToPDF', print_options)
        
        # 保存PDF文件
        with open('厦门集美精选游玩攻略.pdf', 'wb') as f:
            import base64
            f.write(base64.b64decode(pdf_data['data']))
        
        print("PDF文件已生成：厦门集美精选游玩攻略.pdf")
        
        # 关闭浏览器
        driver.quit()
        
        return True
        
    except Exception as e:
        print(f"生成PDF时出错：{e}")
        return False

if __name__ == "__main__":
    print("开始生成行程规划PDF文件...")
    if generate_pdf():
        print("PDF生成成功！")
    else:
        print("PDF生成失败！")