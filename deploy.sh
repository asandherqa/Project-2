#!/bin/bash

# Build server
docker build -t pryze_server server

# Build ticket_api
docker build -t pryze_ticker_api ticket_api

# Create network
docker network create pryze_network

# Run containers
docker run -d \
    -p 5000:5000 \
    --name pryze_server \
    --network pryze_network \
    pryze_server

docker run -d \
    --name pryze_ticket_api \
    --network pryze_network \
    pryze_ticket_api