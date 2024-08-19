<h1 align="center">Missu</h1>
<div align="center">
<p align="center">
  <a href="#">中文</a>｜
  <a href="#">英文</a>
</p>
爬虫通用模板
</div>

## 安装 

```python
pip install requests beautifulsoup4

or

pip3 install requests beautifulsoup4

```

### 使用说明

1. 修改 SimpleSpider 类的 base_url 参数为你需要抓取的网页 URL
2. 根据具体网页的结构，在 extract_data 方法中添加逻辑以提取所需的数据
3. 如果有代理，可以在 proxies 列表中添加代理 IP 地址


### 版本

* 0.0.1 发布
* 0.0.2 排版好看一点
* 0.0.3 添加了 **反爬虫** 机制
