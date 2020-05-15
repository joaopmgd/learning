resource "aws_s3_bucket" "project" {
  bucket = "${var.project_name}-bucket"
  acl    = "private"

  tags = local.default_tags
}

resource "aws_s3_bucket_object" "binary" {
  bucket = "aws_s3_bucket.${var.project_name}.id"
  acl    = "private"
  key    = "binary/"
}

resource "aws_s3_bucket_object" "config" {
  bucket = "aws_s3_bucket.${var.project_name}.id"
  acl    = "private"
  key    = "config/"
}
