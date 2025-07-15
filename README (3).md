
# 🏥 Sistema de Atendimento Hospitalar

Este projeto é uma simulação simples de um sistema de gerenciamento de atendimentos hospitalares, com foco em **priorização de pacientes**. Utiliza estruturas de dados como **heap**, **fila** e **pilha** para gerenciar os atendimentos de forma eficiente.

---

## 📚 Visão Geral

O sistema permite:

- Cadastrar pacientes comuns ou prioritários.
- Atender pacientes seguindo regras de prioridade.
- Desfazer o último atendimento.
- Listar todos os pacientes em espera.

---

## 🏗️ Arquitetura

### Estruturas de Dados:

- **Heap (`heapq`)**: para gerenciar pacientes prioritários com diferentes níveis de urgência.
- **Fila (`list`)**: para pacientes comuns (ordem de chegada).
- **Pilha (`list`)**: para armazenar os atendimentos mais recentes e permitir desfazer.

---

## 📁 Estrutura do Projeto

```
sistema_de_atendimento.py
```

### Classes:

- `Cliente`: representa o paciente, com atributos como nome, CPF e nível de prioridade.
- `SistemaAtendimento`: contém as filas, pilhas e lógica de cadastro, atendimento e listagem.

### Funções principais:

- `cadastrar_cliente()`
- `iniciar_atendimento()`
- `desfazer_atendimento()`
- `listar_fila()`
- `menu()`: interface textual com opções para o usuário.

---

## 🚀 Como Executar

1. Certifique-se de ter o Python 3.6 ou superior instalado.
2. Execute o script:

```bash
python sistema_de_atendimento.py
```

3. Navegue pelo menu interativo.

---

## ✅ Exemplo de Uso

```text
--- MENU ---
[1] Cadastrar Cliente
[2] Iniciar Atendimento
[3] Desfazer Último Atendimento
[4] Listar Fila de Espera
[5] Sair
```

### Cadastro:

```text
Nome: João
CPF: 12345678900
Cliente prioritário? (s/n): s
Nível de prioridade: 1
```

### Atendimento:

```text
Atendendo cliente: João (Prioritário)
```

### Desfazer:

```text
Atendimento desfeito: João (Prioritário)
```

---

## 🧪 Requisitos Técnicos

- Python 3.6+
- Biblioteca padrão: `heapq`

---

## 🔧 Melhorias Futuras

- Persistência em banco de dados (SQLite ou PostgreSQL).
- Interface gráfica com Tkinter ou PyQt.
- Exportação de relatórios.
- Autenticação de usuários (operadores/admins).

---

## 👨‍💻 Autores

**Maria Giuliana, Karlos Marques e Pedro Heleno**  
Analise e desenvolvimento de sistemas • IFPE  
Atividade avalaitiva para Estrutura de Dados | 2025.1

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usar, modificar e distribuir.
