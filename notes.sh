docker build --platform=linux/amd64 -t docker.io/rasoolsnbis/omicsint_h24:session_topology-1.0.0 -f "session_topology/Dockerfile" "session_topology/"



Labs:
- In the Supervised omics integration lab I generated the docker with its relevant conda env activated within the docker and hosted the docker on scilifelab serve project, but in line 188 of notebook it returns an error, which I couldn’t initially figure it out what is the source of it.

- Session meta lab is problematic for making the required env.

- Session topology lab is running well, but code chunk 21 is problematic, which I couldn’t figure out what is the source of it. 
