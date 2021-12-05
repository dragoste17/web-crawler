# web-crawler

## How to Test

### Part 1

1. Run the `docker compose up -d` command to get the container running.
2. Attach a shell to the container so that same environment is ensured.
3. From within the container, run the script to download the files.
4. For eg. `./fetch.py https://www.google.com https://autify.com https://www.airbnb.com https://facebook.com`
5. You can see the downloaded files in the `/fetch` director in the container. Can be verified by running the `ls` command. They will be also copied to the `./fetch` directory in the project as docker compose mounts the volume.
6. In case there are errors in downloading, the message will be displayed on the console.

### Part 2

1. After running part 1, the web page of mentioned urls will be fetched and saved.
2. Metadata will only be shown for fetched urls, for all others a message of `not yet fetched` will be shown.
3. In the same shell attached to the container, run the script as in the following example to see the metadata.
4. Eg. `./fetch.py --metadata https://www.google.com https://autify.com https://www.airbnb.com https://facebook.com`
