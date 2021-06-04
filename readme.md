# Offline installation *[Tested]*

### Or, for example

1. Install websocket packake:

```bash
pip install ./requirements/websocket-0.2.1.tar.gz
```



2. Install websocket_server package:

```bash
pip install ./requirements/websocket_server-0.4.tar.gz
```




3. etc,.（Install all the other packages the way shown above.）





<p align="right">by Alexander Ezharjan</p>

<p align="right">3rd,June,2021</p>













### *other refs below*

# 离线安装Python依赖

1. 离线下载安装包
   下载单个离线包 - pip download -d your_offline_packages <package_name>
   批量下载离线包 - pip download -d your_offline_packages -r requirements.txt
2. 离线安装
   安装单个离线包 - pip install --no-index --find-links=/your_offline_packages/ package_name
   批量安装离线包 - pip install --no-index --find-links=/your_offline_packages/ -r requirements.txt

