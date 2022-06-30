NAME=store_managament
HOST=0.0.0.0:6996
VERSION=v1.0.0


docker build -t $NAME:$VERSION -f Dockerfile .

docker tag $NAME:$VERSION $HOST/$NAME:$VERSION

docker push $HOST/$NAME:$VERSION

