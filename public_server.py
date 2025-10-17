import http.server
import socketserver
import webbrowser
import os
import socket
import subprocess
import platform
import time

# 设置端口
PORT = 8000

# 获取当前目录
Handler = http.server.SimpleHTTPRequestHandler

# 获取本机IP地址
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# 显示分享选项
def show_sharing_options(local_ip):
    print(f"\n📱 分享选项:")
    print(f"1. 使用ngrok (推荐)")
    print(f"2. 使用localtunnel")
    print(f"3. 使用cloudflared tunnel")
    print(f"4. 仅使用本地网络分享 ({local_ip})")
    print(f"\n💡 建议使用ngrok获取稳定的外网链接")
    print(f"   下载地址: https://ngrok.com/download")
    print(f"   安装后重新运行此脚本即可自动创建外网链接")
    print(f"\n📋 提示: 您也可以使用以下命令手动创建外网链接:")
    print(f"   - ngrok: 'ngrok http {PORT}'")
    print(f"   - localtunnel: 'npx localtunnel --port {PORT}'")
    print(f"   - cloudflared: 'cloudflared tunnel --url http://localhost:{PORT}'")

# 创建一个简单的HTML文件，包含网页链接信息
def create_sharing_page(local_ip):
    sharing_html = f'''
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>厦门集美行程分享</title>
        <style>
            body {{
                font-family: 'Microsoft YaHei', Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
            }}
            h1 {{
                color: #333;
                text-align: center;
            }}
            .link-container {{
                background: #f8f9fa;
                border-radius: 8px;
                padding: 20px;
                margin: 20px 0;
            }}
            .link-item {{
                margin-bottom: 15px;
            }}
            .link-title {{
                font-weight: bold;
                color: #555;
            }}
            .link {{
                display: block;
                padding: 10px;
                background: white;
                border-radius: 5px;
                margin-top: 5px;
                word-break: break-all;
            }}
            .copy-button {{
                margin-left: 10px;
                padding: 3px 8px;
                background: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }}
            .copy-button:hover {{
                background: #45a049;
            }}
            .instructions {{
                background: #e3f2fd;
                border-left: 4px solid #2196F3;
                padding: 15px;
                margin: 20px 0;
            }}
            .qrcode {{
                text-align: center;
                margin: 20px 0;
            }}
        </style>
        <script>
            function copyToClipboard(text, button) {{
                navigator.clipboard.writeText(text).then(function() {{
                    button.textContent = '已复制!';
                    setTimeout(function() {{
                        button.textContent = '复制';
                    }}, 2000);
                }});
            }}
        </script>
    </head>
    <body>
        <h1>厦门集美行程规划分享</h1>
        
        <div class="link-container">
            <h2>本地访问链接</h2>
            <div class="link-item">
                <div class="link-title">主页:</div>
                <span class="link" id="index-link">http://{local_ip}:{PORT}/index.html</span>
                <button class="copy-button" onclick="copyToClipboard(document.getElementById('index-link').textContent, this)">复制</button>
            </div>
            <div class="link-item">
                <div class="link-title">打印版:</div>
                <span class="link" id="print-link">http://{local_ip}:{PORT}/print.html</span>
                <button class="copy-button" onclick="copyToClipboard(document.getElementById('print-link').textContent, this)">复制</button>
            </div>
            <div class="link-item">
                <div class="link-title">路线图:</div>
                <span class="link" id="map-link">http://{local_ip}:{PORT}/route_map.html</span>
                <button class="copy-button" onclick="copyToClipboard(document.getElementById('map-link').textContent, this)">复制</button>
            </div>
        </div>
        
        <div class="instructions">
            <h2>如何获取外网可访问链接?</h2>
            <ol>
                <li><strong>方法一: 使用ngrok (推荐)</strong>
                    <ul>
                        <li>从 <a href="https://ngrok.com/download" target="_blank">ngrok.com</a> 下载并安装ngrok</li>
                        <li>打开新的命令行窗口</li>
                        <li>运行命令: <code>ngrok http {PORT}</code></li>
                        <li>在ngrok输出中找到 "Forwarding" 地址 (以 https:// 开头)</li>
                    </ul>
                </li>
                <li><strong>方法二: 使用localtunnel</strong>
                    <ul>
                        <li>确保已安装Node.js</li>
                        <li>打开新的命令行窗口</li>
                        <li>运行命令: <code>npx localtunnel --port {PORT}</code></li>
                    </ul>
                </li>
                <li><strong>方法三: 部署到免费托管服务</strong>
                    <ul>
                        <li>将所有HTML文件上传到GitHub Pages、Netlify、Vercel等免费托管服务</li>
                    </ul>
                </li>
            </ol>
        </div>
        
        <p><strong>注意:</strong> 本地服务器仅在运行期间有效，关闭服务器后链接将失效。</p>
    </body>
    </html>
    '''
    
    with open('sharing_info.html', 'w', encoding='utf-8') as f:
        f.write(sharing_html)
    
    print(f"\n✅ 分享信息页面已创建: http://localhost:{PORT}/sharing_info.html")
    return os.path.abspath('sharing_info.html')

# 主函数
def main():
    local_ip = get_local_ip()
    
    print(f"🚀 旅行行程网页服务器")
    print(f"🔧 本地访问链接:")
    print(f"   http://localhost:{PORT}")
    print(f"   http://{local_ip}:{PORT}")
    print(f"\n📄 可访问的主要页面:")
    print(f"   主页: http://localhost:{PORT}/index.html")
    print(f"   打印版: http://localhost:{PORT}/print.html")
    print(f"   路线图: http://localhost:{PORT}/route_map.html")
    
    # 创建分享信息页面
    sharing_page_path = create_sharing_page(local_ip)
    
    # 显示分享选项
    show_sharing_options(local_ip)
    
    # 尝试自动打开浏览器
    try:
        webbrowser.open(f"http://localhost:{PORT}/sharing_info.html")
    except Exception as e:
        print(f"无法自动打开浏览器: {e}")
    
    # 创建服务器
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\n🛑 按 Ctrl+C 停止服务器")
        try:
            # 启动服务器
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 服务器正在关闭...")
        finally:
            # 清理临时文件
            try:
                if os.path.exists('sharing_info.html'):
                    os.remove('sharing_info.html')
                    print("✅ 临时文件已清理")
            except:
                pass
            print("✅ 服务器已关闭")

if __name__ == "__main__":
    main()