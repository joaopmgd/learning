resource "aws_instance" "project" {
  ami                  = data.aws_ami.aws_linux.id
  instance_type        = "t2.micro"
  security_groups      = ["${aws_security_group.ecs_tasks.name}"]
  key_name             = var.project_name
  user_data            = file("${path.module}/startup_script_${var.ec2_user}.sh")
  depends_on           = [aws_security_group.allow_http_and_ssh, aws_db_instance.postgresql, aws_iam_instance_profile.project_profile]
  iam_instance_profile = aws_iam_instance_profile.project_profile.name

  tags = local.default_tags
}

output "id" {
  description = "ID of the new instance"
  value       = "${aws_instance.project.id}"
}

output "project-ip" {
  description = "IP of the new instance"
  value       = "${aws_instance.project.public_ip}"
}
