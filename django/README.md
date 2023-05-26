## Docker镜像创建方法

* 根据Dockerfile构建镜像，镜像名称为sjtuer_django
    
    ` docker build -t sjtuer_django . `

## Docker镜像使用方法

* 根据sjtuer_django镜像构建容器（sjtuer_backend）并运行，并且将宿主机的端口8000与容器的8000端口建立映射
    
    ` docker run -it -d --name sjtuer_backend -p 8000:8000 sjtuer_django `