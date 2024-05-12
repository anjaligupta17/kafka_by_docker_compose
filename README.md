# kafka_by_docker_compose
#producer
#consumer
--------------------------------------------
Without Code Work ->>>>

topic create:-

kafka-topic.sh --create --zookeeper zookeeper:2181  --replication-factor 1 --partitions 1 --topic work

or

kafka-topics.sh --create --topic mytopic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

produce command:-

kafka-console-producer.sh --topic work --bootstrap-server localhost:9092

consumer command:-

kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic mytopic --from-beginning

That's it! You've now installed Kafka using Docker. You can stop Kafka and Zookeeper by running docker-compose down in the same directory where your docker-compose.yml file is located.

Extra --
2.cd /opt/bitnami/kafka/bin
3.list of topic - /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --list
4.create topic - /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic work --partitions 1 --replication-factor 1
5.describe topic - /opt/bitnami/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic work

----------------------------------------------
With Code Work ->>>>

docker-compose build
docker-compose up -d

For stopping container -
doecker-compose down

All container delete - 
docker rm -f $(docker ps -aq)

All image delete -
docker rmi -f $(docker images -q)
---------------------------------------------------
For authentication for production (learning points)
zookeeper:
  image: bitnami/zookeeper
  ports:
    - "2181:2181"
  environment:
    - ZOO_ENABLE_AUTHENTICATION=true
    - ZOO_SERVER_USERS=<username>:<password>
  volumes:
    - ./zookeeper/data:/bitnami/zookeeper/data




