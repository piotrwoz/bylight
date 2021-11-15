# Generate self-signed certificate with custom ca

```bash
mkdir ssl
cd ssl
openssl genrsa -des3 -out rootCA.key 4096
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.crt
openssl genrsa -out localhost.key 2048
openssl req -new -key localhost.key -out localhost.csr
openssl x509 -req -in localhost.csr -CA rootCA.crt -CAkey rootCA.key -CAcreateserial -out localhost.crt -days 500 -sha256
```

## Credits 
Those snippets of code are extracted from [Lorenzo Fontana](https://gist.github.com/fntlnz/cf14feb5a46b2eda428e000157447309) github page