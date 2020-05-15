# security.tf

# Traffic to the ECS cluster
resource "aws_security_group" "ecs_tasks" {
  name        = "${var.project_name}-ecs-tasks-security-group"
  description = "allow inbound access from the any place"
  vpc_id      = aws_vpc.main.id

  ingress {
    protocol    = "tcp"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    protocol    = "-1"
    from_port   = 0
    to_port     = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Traffic to the RDS database should come from any source
resource "aws_security_group" "allow_any_ingress" {
  name        = "allow_any_ingress"
  description = "Allow any inbound traffic"

  ingress {
    description = "allow_any"
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "any"
  }
}
