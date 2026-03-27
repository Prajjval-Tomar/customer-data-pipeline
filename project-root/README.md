# Customer Data Pipeline 

## Overview

A containerized data pipeline using Flask, FastAPI, and PostgreSQL.

## Architecture

Flask (Mock API) → FastAPI (Ingestion Service) → PostgreSQL

## Features

- Pagination handling
- Data ingestion pipeline
- Retry logic for DB readiness
- Upsert using SQLAlchemy
- Dockerized services

## Run Project

```bash
docker compose up --build
Endpoints
Flask: http://localhost:5000/api/customers
FastAPI Docs: http://localhost:8000/docs
