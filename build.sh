ver='0.0.1'
image_name='masuku'
docker_username='glitchyi'

sudo docker build -t $docker_username/$image_name:$ver .
sudo docker tag $docker_username/$image_name:$ver $docker_username/$image_name:latest
sudo docker push $docker_username/$image_name:$ver
