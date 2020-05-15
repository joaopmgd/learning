# log.tf

resource "aws_cloudwatch_log_group" "project_log_group" {
  name              = "${var.project_name}_log_group"
  retention_in_days = 7
  tags              = local.default_tags
}

resource "aws_cloudwatch_log_stream" "project_log_stream" {
  name           = "${var.project_name}-log-stream"
  log_group_name = aws_cloudwatch_log_group.project_log_group.name
}
