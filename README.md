# madgod - Esteira DevSecOps (CI/CD)

## Objetivo
Prova de conceito (PoC) desenvolvida para DevSecOps. O projeto implementa uma esteira CI/CD automatizada com práticas de segurança integradas, visando reduzir erros de implantação e garantir a detecção precoce de vulnerabilidades no código.

## Tecnologias Utilizadas
* **Controle de Versões:** Git e GitHub
* **Automação (CI/CD):** GitHub Actions
* **Linguagem & Framework:** Python e Flask
* **Testes Automatizados:** pytest
* **Security Scan:** Trivy
* **Containerização:** Docker

## Fluxo da Pipeline
1. **Source:** Código armazenado no repositório Git (branch `main`).
2. **Build:** Preparação do ambiente Ubuntu e instalação de dependências via `requirements.txt`.
3. **Teste:** Execução automática do teste unitário (`test_app.py`) para validar o funcionamento base.
4. **Security Scan:** Análise de vulnerabilidades nos pacotes instalados utilizando a ferramenta Aqua Trivy.
5. **Build da Imagem:** Construção da imagem Docker baseada no `Dockerfile` disponibilizado.
6. **Deploy:** Instanciação do contentor e validação da resposta do servidor web na porta 5000.

## Relatório de Análise de Segurança
Durante a execução automatizada da ferramenta Trivy, foram identificadas vulnerabilidades nas dependências do projeto. Abaixo encontra-se o detalhe das falhas reportadas:

**Achado 1:**
* **Vulnerabilidade/Problema:** Redirecionamento de HTTPS para HTTP não remove o cabeçalho de Autorização (CVE-2018-18074), podendo expor credenciais em trânsito.
* **Componente Afetado:** Biblioteca Python `requests` (Versão Instalada: 2.19.0).
* **Nível de Severidade:** ALTA (HIGH).
* **Correção/Mitigação:** Atualizar a versão da biblioteca no ficheiro `requirements.txt` para a versão corrigida (2.20.0).

**Achado 2:**
* **Vulnerabilidade/Problema:** Possibilidade de execução arbitrária de código na máquina de desenvolvimento (CVE-2024-34069).
* **Componente Afetado:** Biblioteca Python `Werkzeug` (Versão Instalada: 3.0.0).
* **Nível de Severidade:** ALTA (HIGH).
* **Correção/Mitigação:** Atualizar a versão da biblioteca no ficheiro `requirements.txt` para a versão corrigida (3.0.3).
