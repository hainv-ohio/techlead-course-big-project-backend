set -e # STOP ON ERROR

# Variables
SERVICE_NAME=$1
NAME=$(echo techlead-$SERVICE_NAME | sed -e "s/_/-/g")
VERSION=$2

if [ -z "$SERVICE_NAME" ]
then
      echo "SERVICE NAME MUST NOT BE EMPTY!"
      exit 1
fi
if [ -z "$VERSION" ]
then
      echo "SERVICE VERSION MUST NOT BE EMPTY!"
      exit 1
fi

# add "insecure-registries":["192.53.115.165:5000"] to /etc/docker/daemon.json 

# Fetch the .env file
if [ -f ./.env ]; then
    source ./.env
fi

echo "Building ${SERVICE_NAME} Docker image with version ${VERSION}. Tag ${NAME}"
# Login to docker registry
# ...

# Build production ready docker
echo "docker build -t $NAME:$VERSION -f services/$SERVICE_NAME/Dockerfile ."