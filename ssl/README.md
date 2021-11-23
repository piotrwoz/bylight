## How to

```bash
mkdir ssl
cd ssl
openssl req -x509 -nodes -new -sha256 -days 1024 -newkey rsa:2048 -keyout RootCA.key -out RootCA.pem -subj "/C=US/CN=Example-Root-CA"
openssl x509 -outform pem -in RootCA.pem -out RootCA.crt
touch domains.ext
nano/vim domains.ext
```

Paste this to `domains.ext`

```bash
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names
[alt_names]
DNS.1 = localhost
DNS.2 = fake1.local
DNS.3 = fake2.local
```
Save and exit.

```bash
openssl req -new -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.csr -subj "/C=US/ST=YourState/L=YourCity/O=Example-Certificates/CN=localhost.local"
openssl x509 -req -sha256 -days 1024 -in localhost.csr -CA RootCA.pem -CAkey RootCA.key -CAcreateserial -extfile domains.ext -out localhost.crt
```

Add `000-default.conf` (and its content, its here in this folder). You can remove `domains.ext`.

Create a `Dockerfile` for prestashop so it can work with our cerificates.

```bash
FROM prestashop/prestashop:1.7.7.8

RUN a2enmod ssl

EXPOSE 80
EXPOSE 443 

RUN service apache2 restart
```

In `docker-compose.yml` add new volume for prestashop `./ssl/:/etc/apache2/sites-available` add new port `443:443`. To avoid pulling docker image from your repo in docker hub use

```bash
build: 
            context: .
            dockerfile: Dockerfile
```

It will build your prestashop image locally. Also turn your `PS_DEV_MODE` to false or 0.

Now go and `docker-compose up` your shop and enable SSL.

# Credits
[cecilemuller](https://gist.github.com/cecilemuller/9492b848eb8fe46d462abeb26656c4f8)