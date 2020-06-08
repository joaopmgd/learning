#######################
#    LOAD BALANCER    #
#######################

resource "aws_lb" "lb" {
  name            = local.project_user_1
  subnets         = aws_subnet.main-public.id
  security_groups = [aws_security_group.ecs_tasks.id]
}

#######################
#    TARGET  GROUP    #
#######################

resource "aws_lb_target_group" "target" {
  port        = var.app_port
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"

  health_check {
    healthy_threshold   = "3"
    interval            = "180"
    protocol            = "HTTP"
    matcher             = "401"
    timeout             = "3"
    path                = var.health_check_path
    unhealthy_threshold = "2"
  }
}

#######################
#      LISTENERS      #
#######################

# Redirect all traffic from the ALB to the target group
resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.lb.id
  port              = var.app_port
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_lb_target_group.target.id
    type             = "forward"
  }
}

# Redirect all traffic from the ALB to the target group
resource "aws_alb_listener" "https" {
  load_balancer_arn = aws_lb.lb.id
  port              = "443"
  protocol          = "HTTPS"

  certificate_arn = aws_acm_certificate.cert.arn
  ssl_policy      = "ELBSecurityPolicy-2016-08"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target.id
  }
  
  depends_on = [aws_acm_certificate.cert]
}
