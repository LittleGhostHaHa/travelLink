import http.server
import socketserver
import webbrowser
import os
import socket

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

# 创建一个简单的HTML文件，包含外网链接创建指南
def create_guide_html():
    html_content = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>厦门集美行程 - 外网访问指南</title>
    <style>
        body {
            font-family: 'Microsoft YaHei', Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        h2 {
            color: #3498db;
            margin-top: 30px;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
        }
        .method {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid #3498db;
        }
        code {
            background: #eee;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: Consolas, Monaco, 'Andale Mono', monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .note {
            background: #fff3cd;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
        }
        .success {
            background: #d4edda;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #28a745;
            margin: 20px 0;
        }
        .warning {
            background: #fff3cd;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #ffc107;
            margin: 20px 0;
        }
        .links {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .link-card {
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            transition: transform 0.2s;
        }
        .link-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .link-card h3 {
            margin-top: 0;
            color: #3498db;
        }
        .link {
            word-break: break-all;
            color: #28a745;
            text-decoration: none;
        }
        .link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>厦门集美行程 - 外网访问指南</h1>
    
    <div class="success">
        <h3>本地服务器已成功启动！</h3>
        <p>您现在可以通过以下本地链接访问您的行程页面：</p>
        <div class="links">
            <div class="link-card">
                <h3>主页</h3>
                <a href="http://localhost:8000/index.html" class="link" target="_blank">http://localhost:8000/index.html</a>
            </div>
            <div class="link-card">
                <h3>打印版</h3>
                <a href="http://localhost:8000/print.html" class="link" target="_blank">http://localhost:8000/print.html</a>
            </div>
            <div class="link-card">
                <h3>路线图</h3>
                <a href="http://localhost:8000/route_map.html" class="link" target="_blank">http://localhost:8000/route_map.html</a>
            </div>
        </div>
    </div>
    
    <h2>如何创建外网可访问的链接？</h2>
    
    <div class="method">
        <h3>方法一：使用 ngrok（推荐）</h3>
        <ol>
            <li>从 <a href="https://ngrok.com/download" target="_blank">ngrok.com</a> 下载适合您操作系统的版本</li>
            <li>解压下载的文件到任意目录</li>
            <li>打开新的命令行窗口（保持当前服务器运行）</li>
            <li>导航到ngrok所在目录</li>
            <li>运行以下命令：<code>./ngrok http 8000</code>（Windows用户直接运行<code>ngrok http 8000</code>）</li>
            <li>ngrok会显示一个公网URL（以 https:// 开头），您可以将此URL分享给他人</li>
        </ol>
        <p>例如：<code>https://abcd-123-45-67-890.ngrok.io</code></p>
        <p>访问此链接的用户将看到您的行程页面！</p>
    </div>
    
    <div class="method">
        <h3>方法二：使用 localtunnel</h3>
        <ol>
            <li>确保您的计算机已安装Node.js</li>
            <li>打开新的命令行窗口（保持当前服务器运行）</li>
            <li>运行以下命令：<code>npx localtunnel --port 8000</code></li>
            <li>localtunnel会生成一个公网URL，您可以将此URL分享给他人</li>
        </ol>
    </div>
    
    <div class="method">
        <h3>方法三：使用 GitHub Pages</h3>
        <ol>
            <li>创建一个新的GitHub仓库</li>
            <li>上传所有HTML文件到仓库</li>
            <li>在仓库设置中启用GitHub Pages</li>
            <li>GitHub会提供一个公网URL，如：<code>https://username.github.io/repository</code></li>
        </ol>
        <p class="note">注意：此方法需要您有GitHub账号，且链接会一直有效（直到您删除仓库）</p>
    </div>
    
    <div class="warning">
        <h3>重要提示：</h3>
        <ul>
            <li>使用ngrok或localtunnel创建的链接仅在服务器运行期间有效</li>
            <li>当您关闭命令行窗口或按下Ctrl+C时，服务器将停止，外网链接将失效</li>
            <li>确保您的防火墙设置允许端口8000的访问</li>
            <li>不要在公共链接中分享敏感信息</li>
        </ul>
    </div>
    
    <div class="note">
        <p>如果您需要更持久的解决方案，可以考虑使用Netlify、Vercel、Render等免费托管服务，它们提供简单的拖放式部署功能。</p>
    </div>
</body>
</html>
'''
    
    with open('public_access_guide.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return 'public_access_guide.html'

# 创建服务器
local_ip = get_local_ip()
guide_file = create_guide_html()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 旅行行程网页服务器已启动")
    print(f"🔧 本地访问链接:")
    print(f"   http://localhost:{PORT}")
    print(f"   http://{local_ip}:{PORT}")
    print(f"\n📄 主要页面:")
    print(f"   主页: http://localhost:{PORT}/index.html")
    print(f"   打印版: http://localhost:{PORT}/print.html")
    print(f"   路线图: http://localhost:{PORT}/route_map.html")
    print(f"   外网访问指南: http://localhost:{PORT}/{guide_file}")
    print(f"\n💡 如何获取外网可访问链接?")
    print(f"   1. 查看外网访问指南页面获取详细步骤")
    print(f"   2. 推荐使用ngrok工具: https://ngrok.com/download")
    print(f"   3. 安装后在新命令行中运行: ngrok http {PORT}")
    print(f"\n🛑 按 Ctrl+C 停止服务器")
    
    # 尝试自动打开外网访问指南
    try:
        webbrowser.open(f"http://localhost:{PORT}/{guide_file}")
    except:
        print("无法自动打开浏览器，请手动访问上述链接")
    
    try:
        # 启动服务器
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 服务器正在关闭...")
    finally:
        # 清理临时文件
        try:
            if os.path.exists(guide_file):
                os.remove(guide_file)
                print("✅ 临时文件已清理")
        except:
            pass
        print("✅ 服务器已关闭")