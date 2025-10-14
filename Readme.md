# DummyRequestCounter

## Overview
**DummyRequestCounter** is a simple multi-container application built with **FastAPI** and **Redis**.  
It demonstrates how to use Docker and Docker Compose to orchestrate a web service and a database.  
The application counts the number of requests made to the API in real time using Redis.

---

## Features
- Flask API for request counting
- Redis for storing the count
- Multi-container setup using Docker Compose
- Easy to configure environment variables

---

## Prerequisites
Before running the project, make sure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/)



### Persistent Storage
Redis data is stored in a Docker volume named `redis_data` to ensure data persists across container restarts.

### Custom Network
FastAPI and Redis communicate over the custom network called `my_app_network`.
