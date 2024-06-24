include .env
export

# Makefile
.PHONY: build push tag login

# Docker image tag
IMAGE_TAG ?= $(IMAGE_TAG)

# AWS region
AWS_REGION ?= $(AWS_REGION)
AWS_ACCOUNT_ID ?= $(AWS_ACCOUNT_ID)

# ECS Repository
ECS_REPOSITORY_NAME ?= $(ECS_REPOSITORY_NAME)
ECS_REPOSITORY_URL = ${AWS_ACCOUNT_ID}.dkr.ecr.$(AWS_REGION).amazonaws.com

login:
	AWS_PROFILE=$(AWS_PROFILE) aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(ECS_REPOSITORY_URL)

build:
	cd django && docker build --platform linux/amd64 -t $(ECS_REPOSITORY_NAME) -f Dockerfile .

tag:
	cd django && docker tag $(IMAGE_TAG) $(ECS_REPOSITORY_URL)/$(IMAGE_TAG)

push:
	cd django && docker push $(ECS_REPOSITORY_URL)/$(IMAGE_TAG)


