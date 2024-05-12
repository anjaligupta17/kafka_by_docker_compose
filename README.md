# kafka_by_docker_compose
#producer
#consumer

kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic your_topic_name

----------------------------------
Free Public APIs for Developers & Free Alternatives List


1.https://rapidapi.com › collection › list-of-free-apis
2.Free API - 90+ Public APIs For Testing [No Key]

Apipheny
https://apipheny.io › free-api

------------------------------------
(same for other)
docker build -t pyspark-app .
docker run --network="your_network_name" pyspark-app
Replace your_network_name with the name of the Docker network where Kafka is running.
-------------------------------------
For this part:-'--network="your_network_name"'

1.docker network ls
2.docker network create my-network
3.docker run --network=my-network pyspark-app

----------------------------------------------

zookeeper:
  image: bitnami/zookeeper
  ports:
    - "2181:2181"
  environment:
    - ZOO_ENABLE_AUTHENTICATION=true
    - ZOO_SERVER_USERS=<username>:<password>
  volumes:
    - ./zookeeper/data:/bitnami/zookeeper/data




