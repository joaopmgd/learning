locals {
  rds_allocated_storage = 20
  rds_storage_type      = "gp2"
  rds_engine            = "postgres"
  rds_engine_version    = "11.5"
  rds_instance_class    = "db.t2.micro"
}

resource "aws_db_instance" "postgresql" {
  allocated_storage      = local.rds_allocated_storage
  storage_type           = local.rds_storage_type
  engine                 = local.rds_engine
  engine_version         = local.rds_engine_version
  instance_class         = local.rds_instance_class
  name                   = var.project_name
  username               = var.database_user
  password               = var.database_password
  vpc_security_group_ids = [aws_security_group.allow_any_ingress.id]
  publicly_accessible    = true
  skip_final_snapshot    = true
}
