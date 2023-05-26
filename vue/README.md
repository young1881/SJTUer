## Docker镜像创建方法

* 根据Dockerfile构建镜像，镜像名称为sjtuer_vue

    ` docker build -t sjtuer_vue . `


## Docker镜像使用方法

* 根据sjtuer_vue镜像构建容器（sjtuer_frontend）并运行，并且将宿主机的端口5173与容器的5173端口建立映射

    ` docker run -it -d --name sjtuer_frontend -p 5173:5173 sjtuer_vue `
