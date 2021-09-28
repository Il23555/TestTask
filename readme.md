
### Тестовое задание

Ссылка на модель и ноутбук https://drive.google.com/drive/folders/1u2iPOKSvESacJSdRFa-X-Xbou3P3KT4G?usp=sharing 

### Run App
```bash
python start.py
```

### Use Docker

Build docker image 
```bash
docker build -t <app name> .
```

Run docker container
```bash
docker run -d -p 5000:5000 <app name>
```

Send POST-request with car image to http://localhost/5000
