[![Python application test with GitHub Actions](https://github.com/JTorres258/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/JTorres258/functions-from-zero/actions/workflows/main.yml)

# functions-from-zero

### To call Microservice

Something like this

```bash
curl -X 'POST' \
  'https://fuzzy-space-dollop-7r56q7vq466fr9gx-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsfot",
  "length": 1
}'
```

### Build container

`docker build .`

To know what the image is:

`docker image ls`

Run container

`docker run -p 127.0.0.1:8080:8080 IMAGE_ID`

We can test it using a bash script similar to the microservice, but using the local host `0.0.0.0:8080` and then:

`bash invoke.sh`