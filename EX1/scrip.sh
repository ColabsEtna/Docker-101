# Construire l'image Docker
docker build -t debian-colabs .

# Exécuter un conteneur à partir de l'image construite
docker run -it debian-colabs:v1
