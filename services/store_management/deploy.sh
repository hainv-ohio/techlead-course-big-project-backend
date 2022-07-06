NAME=store_managament
HOST=0.0.0.0:6996
VERSION=1.0.0


#docker build -t store_managament:1.0.0 -f Dockerfile ...

docker build -t $NAME:$VERSION -f Dockerfile ...

#docker tag $NAME:$VERSION $HOST/$NAME:$VERSION
#
#docker push $HOST/$NAME:$VERSION

docker run -p 6996:6996 $NAME:$VERSION