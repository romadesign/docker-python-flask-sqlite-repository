# Backend

## configure from terminal
## Project setup docker and docker composer install

```
cmd=${@:-/bin/bash}
cd "${0%/*}"
echo $PWD
docker run --rm \
    --user "$(id -u):$(id -g)" \
    -p 5000:5000 \
    -v "$PWD":/opt/app \
    -it $(docker build -q .) \
    $cmd
```

* change nick I have no name!@f44e0d76e16d:/opt/app$ || Every time you start with docker the name of the container will change


### Compiles and hot-reloads for development
```
python main.py
```


### install sqlite browser
```
sudo apt install sqlitebrowser
```

### To run test
enter the container to start the test
```
docker exec -it nombre_del_contenedor /bin/bash
```

### Install docker and docker composer
https://www.youtube.com/watch?v=65zv8s499hE

docker, docker-compose Permission denied
https://thxxyj.tistory.com/42


