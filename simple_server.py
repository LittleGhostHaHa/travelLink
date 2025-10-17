import http.server
import socketserver
import webbrowser
import os

# 设置端口
PORT = 8000

# 创建服务器
Handler = http.server.SimpleHTTPRequestHandler

def main():
    print(f"旅行行程网页服务器已启动在端口 {PORT}")
    print(f"\n本地访问链接:")
    print(f"  http://localhost:{PORT}/index.html")
    print(f"  http://localhost:{PORT}/print.html")
    print(f"  http://localhost:{PORT}/route_map.html")
    print(f"  http://localhost:{PORT}/public_access_guide.html")
    print(f"\n如何获取外网可访问链接?")
    print(f"1. 查看 http://localhost:{PORT}/public_access_guide.html 获取详细步骤")
    print(f"2. 推荐使用ngrok工具: https://ngrok.com/download")
    print(f"3. 安装后在新命令行中运行: ngrok http {PORT}")
    print(f"\n按 Ctrl+C 停止服务器")
    
    # 尝试自动打开浏览器
    try:
        webbrowser.open(f"http://localhost:{PORT}/public_access_guide.html")
    except:
        pass
    
    # 启动服务器
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    main()