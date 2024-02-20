# Select base image (can be ubuntu, python, shiny etc)
FROM rocker/tidyverse:4.3.2

# Create user name and home directory variables. 
# The variables are later used as $USER and $HOME. 
ENV USER=username
ENV HOME=/home/$USER

# Add user to system
RUN useradd -m -u 1000 $USER

# Set working directory (this is where the code should go)
WORKDIR $HOME/app

# Update system and install dependencies.
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    software-properties-common

# Copy code and start script (this will place the files in home/username/)
COPY requirements.txt $HOME/app/requirements.txt
COPY app.rmd $HOME/app/app.rmd
COPY start-script.sh $HOME/app/start-script.sh

RUN chmod +x start-script.sh \
    && chown -R $USER:$USER $HOME \
    && rm -rf /var/lib/apt/lists/*

USER $USER
EXPOSE 8501

ENTRYPOINT ["./start-script.sh"]