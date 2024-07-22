docker build --platform=linux/amd64 -t docker.io/rasoolsnbis/omicsint_h24:unsupervisedOMICsIntegration-1.0.0 -f "session_ml/UnsupervisedOMICsIntegration/Dockerfile" "session_ml/UnsupervisedOMICsIntegration"

docker run -d -p 8787:8787 --platform=linux/amd64 --name my_rstudio_container docker.io/rasoolsnbis/omicsint_h24:unsupervisedOMICsIntegration-1.0.0

