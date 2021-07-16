#!/bin/bash

# Build server
docker build -t pryze_server server

# Build ticket_api
docker build -t pryze_ticket_api ticket_api

# Build class_api
docker build -t pryze_class_api class_api

# Build class_prize
docker build -t pryze_prize_api prize_api

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

docker run -d \
    --name pryze_class_api \
    --network pryze_network \
    pryze_class_api

docker run -d \
    --name pryze_prize_api \
    --network pryze_network \
    pryze_prize_api