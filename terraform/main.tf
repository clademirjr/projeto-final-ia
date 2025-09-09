terraform {
  required_version = ">= 1.6.0"
}

provider "local" {}

resource "local_file" "hello" {
  content  = "Infraestrutura do projeto-final-ia pronta!"
  filename = "${path.module}/hello.txt"
}
