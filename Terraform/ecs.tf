# ecs.tf
locals {
  project_user_name = "${var.project_name}-${var.user}"
}

resource "aws_ecs_cluster" "main-cluster" {
  name               = "${var.project_name}-cluster"
  capacity_providers = ["FARGATE", "FARGATE_SPOT"]
}

data "template_file" "project_app" {
  template = file("${path.module}/${local.project_user_name}-definitions.json")

  vars = {
    aws_region       = var.aws_region
    app_name         = var.project_name
    log_name         = aws_cloudwatch_log_group.project_log_group.name
    app_image        = "${aws_ecr_repository.project.repository_url}:latest"
    databaseURL      = aws_db_instance.postgresql.endpoint
    databaseName     = var.project_name
    databasePassword = var.database_password
    databaseUser     = var.database_user
  }
}

resource "aws_ecs_task_definition" "project-app" {
  family                   = "${local.project_user_name}-app-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  tags                     = local.default_tags
  container_definitions    = data.template_file.project_app.rendered
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
}

resource "aws_ecs_service" "main" {
  name            = "${local.project_user_name}-service"
  cluster         = aws_ecs_cluster.main-cluster.id
  task_definition = aws_ecs_task_definition.project-app.arn
  desired_count   = var.app_count
  launch_type     = "FARGATE"

  network_configuration {
    security_groups  = [aws_security_group.ecs_tasks.id]
    subnets          = [aws_subnet.main-public.id]
    assign_public_ip = true
  }

  depends_on = [aws_db_instance.postgresql, aws_iam_role_policy_attachment.ecs_task_execution_role, aws_ecr_repository.project]
}
