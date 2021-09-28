### Run App
```bash
python start.py
```

### Use Docker

Build docker image 
```bash
docker build -t my_app .
```

Run docker container
```bash
docker run -d -p 5000:5000 my_app
```

Send POST-request with car's image to http://localhost/5000