# provider.tf

provider "aws" {
  region  = var.aws_region
  version = "2.56"
  profile = "default"
}


terraform {
  required_version = ">= 0.12"

  backend "s3" {
    bucket = "crpt-bucket"
    key    = "infra/infrastructure.tfstate"
    region = "ap-northeast-1"
  }
}
