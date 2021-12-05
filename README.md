# web-crawler

## How to Test
1. Run the `docker-compose up` command to get the container running.
2. Attach a shell to the container so that same environment is ensured.
3. From within the container, run the script to download the files.
4. For eg. `./fetch.py https://www.google.com https://autify.com https://www.airbnb.com https://facebook.com`
5. You can see the downloaded files in the `/fetch` director in the container. Can be verified by running the `ls` command. They will be also copied to the `./fetch` directory in the project as docker compose mounts the volume.
