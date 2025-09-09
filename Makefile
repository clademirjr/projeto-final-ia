# Makefile para facilitar comandos locais
.PHONY: setup run test docker-build docker-run tf-init tf-plan tf-apply

setup:
	pip install -r requirements.txt

run:
	streamlit run main.py

test:
	pytest -q

docker-build:
	docker build -t projeto-final-ia:latest .

docker-run:
	docker run --env-file .env -p 8501:8501 projeto-final-ia:latest

tf-init:
	cd terraform && terraform init

tf-plan:
	cd terraform && terraform plan -out=tfplan

tf-apply:
	cd terraform && terraform apply -auto-approve tfplan
