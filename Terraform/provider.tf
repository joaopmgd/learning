# provider.tf

provider "aws" {
  region  = var.aws_region
  version = "2.56"
  profile = "default"
}
