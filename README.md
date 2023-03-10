# Throttle Responder
This mini web-server should receive requests containing a delay value (int) and an id (sha1).
It returns a response delayed accordingly, containing the id.

## Build the container
docker build -t throttle-responder .

## Start the container
docker run -p 5000:5000 throttle-responder

## Example usage
curl --location --request POST 'http://localhost:5000/throttle' \
--header 'Content-Type: application/json' \
--data-raw '{
    "throttle": 1000,
    "id": "sample_id"
}'
