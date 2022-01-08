#!/bin/bash

CONTAINER="admin-mysql_db.1.jhmt04hxq732lvnr76m7ikzlv"

docker cp ./*.sql $CONTAINER:/tmp/be_180320.sql
docker cp ./constructDB.sh $CONTAINER:/tmp/constructDB.sh
docker exec -it $CONTAINER  chmod 777 /tmp/constructDB.sh
docker exec -it $CONTAINER /bin/sh /tmp/constructDB.sh
docker exec -it $CONTAINER  rm /tmp/be_180320.sql
docker exec -it $CONTAINER  rm /tmp/constructDB.sh 
