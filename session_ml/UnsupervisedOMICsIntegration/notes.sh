docker build --platform=linux/amd64 -t docker.io/rasoolsnbis/test:v9 -f "session_ml/UnsupervisedOMICsIntegration/container/Dockerfile" "session_ml/UnsupervisedOMICsIntegration/container"

docker run -d -p 8787:8787 --platform=linux/amd64 --name my_rstudio_container docker.io/rasoolsnbis/test:v9