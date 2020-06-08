# variables.tf
variable "user" {
  description = "The User of the platform"
  type        = string
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "aws_region" {
  description = "The AWS region things are created in"
  type        = string
}

variable "app_image" {
  description = "Docker image to run in the ECS cluster"
  type        = string
}

variable "app_port" {
  description = "Port exposed by the docker image to redirect traffic to"
  type        = number
  default     = 80
}

variable "app_count" {
  description = "Number of docker containers to run"
  type        = number
  default     = 1
}

variable "fargate_cpu" {
  description = "Fargate instance CPU units to provision (1 vCPU = 1024 CPU units)"
  type        = string
  default     = "256"
}

variable "fargate_memory" {
  description = "Fargate instance memory to provision (in MiB)"
  type        = string
  default     = "512"
}

variable "ecs_task_execution_role_name" {
  description = "ECS task execution role name"
  type        = string
  default     = "myEcsTaskExecutionRole"
}

variable "az_count" {
  description = "Number of AZs to cover in a given region"
  type        = string
  default     = "2"
}

variable "default_dns_name" {
  description = "Name of the URL"
  type        = string
  default     = "example.com"
}

locals {
  default_prefix = "${var.project_name}-${var.user}"
  default_tags = {
    Name = var.project_name
  }
}
