# A facial detection API

## How to develop

### Using local settings

Create an environment for python, and install requirements.test.txt, run server
using uvicorn like below:

```bash
fd-api$ uvicorn app:app --port 8080 --reload
```

Test using *tox*. But not implemented yet.

### Using docker settings

Not yet implemented.

## How to use?

Find on `/docs` the documentation for this api.

### Detect

The endpoint `/detect` which gets one argument, an *img* on a base64 string
format. You can transform any image into base64
[here](https://base64.guru/converter/encode/image). The api will return a list
of bounding boxes for each face detected. You can also test it with the curl
bellow:

```bash
fd-api$ curl -X 'POST' \
  'http://localhost:8080/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"img": "paste-base64-img-str-here"}'
```

## Troubleshooting

Nothing here yet!
