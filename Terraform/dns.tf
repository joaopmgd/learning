#################
##     DNS     ##
#################

data "aws_route53_zone" "dns_zone" {
  name = var.default_dns_name
}

data "aws_route53_zone" "selected" {
  name         = var.default_dns_name
  private_zone = false
}