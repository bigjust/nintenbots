./build_docker.sh
docker kill `cat jenkins_container`
./start_docker.sh > jenkins_container

