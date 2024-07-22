docker build --platform=linux/amd64 -t docker.io/rasoolsnbis/omicsint_h24:supervisedOMICsIntegration-1.0.0 -f "session_ml/SupervisedOMICsIntegration/Dockerfile" "session_ml/SupervisedOMICsIntegration"

docker run -d -p 8787:8787 --platform=linux/amd64 --name supervisedOMICsIntegration docker.io/rasoolsnbis/omicsint_h24:supervisedOMICsIntegration-1.0.0

docker run -d -p 8787:8787 --platform=linux/amd64 --name unsupervisedOMICsIntegration docker.io/rasoolsnbis/omicsint_h24:unsupervisedOMICsIntegration-1.0.0