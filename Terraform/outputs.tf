# output.tf

output "postgresql-endpoint" {
  description = "Public DNS name and port separated by a colon"
  value       = aws_db_instance.postgresql.endpoint
}

output "service-endpoint" {
  description = "Public IP for the service"
  value       = aws_ecs_service.main.public_ip
}
