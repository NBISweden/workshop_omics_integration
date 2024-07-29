docker build --platform=linux/amd64 -t docker.io/rasoolsnbis/omicsint_h24:session_gsa-1.0.0 -f "session_gsa/Dockerfile" "session_gsa"

docker run -d -p 8787:8787 --platform=linux/amd64 --name session_mofa docker.io/rasoolsnbis/omicsint_h24:session_mofa-1.0.0

docker run -d -p 8787:8787 --platform=linux/amd64 --name supervisedOMICsIntegration docker.io/rasoolsnbis/omicsint_h24:supervisedOMICsIntegration-1.0.0

docker run -d -p 8787:8787 --platform=linux/amd64 --name unsupervisedOMICsIntegration docker.io/rasoolsnbis/omicsint_h24:unsupervisedOMICsIntegration-1.0.0