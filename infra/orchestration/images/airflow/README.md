# Docker Airflow Image

### Build Image

~~~sh
docker build . -t lake-apache-airflow:2.8.1 --platform linux/amd64
docker tag lake-apache-airflow:2.8.1 matbragan/lake-apache-airflow:2.8.1
docker push matbragan/lake-apache-airflow:2.8.1
~~~