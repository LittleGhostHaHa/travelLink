#!/usr/bin/env python3
"""
生成路线地图图片
使用matplotlib根据坐标绘制行程路线图
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_route_map():
    """创建路线地图图片"""
    
    # 景点坐标（经度，纬度）
    locations = {
        '集美集影视文创园': (118.098497, 24.580102),
        '集美学村': (118.092832, 24.566280),
        '大社': (118.087921, 24.565843)
    }
    
    # 路线顺序
    route_order = ['集美集影视文创园', '集美学村', '大社', '集美集影视文创园']
    
    # 创建图形
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 提取坐标
    lons = [locations[name][0] for name in route_order]
    lats = [locations[name][1] for name in route_order]
    
    # 计算合适的显示范围
    lon_min, lon_max = min(lons) - 0.005, max(lons) + 0.005
    lat_min, lat_max = min(lats) - 0.005, max(lats) + 0.005
    
    # 设置坐标范围
    ax.set_xlim(lon_min, lon_max)
    ax.set_ylim(lat_min, lat_max)
    
    # 绘制路线
    ax.plot(lons, lats, 'r-', linewidth=3, alpha=0.8, label='游览路线')
    
    # 绘制景点标记
    markers = ['o', 's', 'D', 'o']  # 圆形、方形、菱形、圆形
    colors = ['#52c41a', '#1890ff', '#ff4d4f', '#52c41a']  # 绿色、蓝色、红色、绿色
    sizes = [100, 80, 80, 100]
    
    for i, (name, marker, color, size) in enumerate(zip(route_order, markers, colors, sizes)):
        lon, lat = locations[name]
        ax.scatter(lon, lat, s=size, c=color, marker=marker, alpha=0.8, edgecolors='white', linewidth=2)
        
        # 添加景点标签
        ax.annotate(name, (lon, lat), 
                   xytext=(10, 10), textcoords='offset points',
                   fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        # 添加路线编号
        if i < len(route_order) - 1:  # 不在最后一个点（返回点）添加编号
            ax.text(lon, lat, str(i+1), 
                   ha='center', va='center', 
                   fontsize=8, fontweight='bold', color='white')
    
    # 添加起点和终点标记
    ax.text(lons[0], lats[0], '起点', 
           ha='center', va='center', 
           fontsize=9, fontweight='bold', 
           bbox=dict(boxstyle="round,pad=0.3", facecolor='#52c41a', alpha=0.8))
    
    ax.text(lons[-1], lats[-1], '终点', 
           ha='center', va='center', 
           fontsize=9, fontweight='bold',
           bbox=dict(boxstyle="round,pad=0.3", facecolor='#ff4d4f', alpha=0.8))
    
    # 设置标题和标签
    ax.set_title('厦门集美精选游玩路线图', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('经度', fontsize=12)
    ax.set_ylabel('纬度', fontsize=12)
    
    # 添加网格
    ax.grid(True, alpha=0.3)
    
    # 添加图例
    ax.legend(loc='upper right')
    
    # 添加比例尺说明
    ax.text(0.02, 0.98, '比例尺：约1公里', 
           transform=ax.transAxes, fontsize=10,
           bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.7))
    
    # 美化图形
    plt.tight_layout()
    
    # 保存图片
    plt.savefig('route_map.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.savefig('route_map.jpg', dpi=300, bbox_inches='tight', facecolor='white')
    
    print("路线地图已生成：route_map.png, route_map.jpg")
    
    # 显示图片信息
    print("路线总长度：约4公里")
    print("景点顺序：")
    for i, name in enumerate(route_order[:-1]):  # 不显示最后一个返回点
        print(f"{i+1}. {name}")
    print("4. 返回起点")

if __name__ == "__main__":
    print("正在生成路线地图...")
    create_route_map()
    print("路线地图生成完成！")