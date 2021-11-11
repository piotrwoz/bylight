# Electronic Business
Project implemented for the subject Electronic Business.

[![prestashop 1.7.7.8][shield-prestashop]](https://github.com/PrestaShop/PrestaShop)
[![phpmyadmin latest][shield-phpmyadmin]](https://hub.docker.com/layers/phpmyadmin/library/phpmyadmin/latest/images/sha256-55ff8776ca52dbdf4120821431f580d07f704ac68a3649eabb4a1e915cbd45eb?context=explore)
[![mysql 5.7][shield-mysql]](https://hub.docker.com/layers/mysql/library/mysql/5.7/images/sha256-e5f84e8def65d7bd1e5aaf79d429b748d56c514f6dc4b6247fc67df1f7da7a2c?context=explore)

## Building
In order to build this project use:

```bash
docker-compose up -d
```
## Before you change anything
It's considered a good practice to copy `webprod` folder into your `webbackup` folder. In case you mess sth up you can easili restore the shop.

## Development

To  access PrestaShop as admin go to

```
localhost:80/admin838i5zodk
```

To access PhpMyAdmin go to:

```
localhost:8080
```

## Before commiting

Remember to update `dbdump` with updated database backup which you can download from admin panel going to `Advanced / Data base / Backup / Download backup files`

## Authors

[Kinga Wladzinska](https://github.com/Popularkiya) |
[Marcel Bieniek](https://github.com/marcelbieniek) |
[Piotr Wozniak](https://github.com/piotrwoz) |
[Lukasz Nojman](https://github.com/luckyluk07)

[shield-prestashop]: https://img.shields.io/badge/prestashop-1.7.7.8-pink
[shield-phpmyadmin]: https://img.shields.io/badge/phpmyadmin-latest-pink
[shield-mysql]: https://img.shields.io/badge/mysql-5.7-pink