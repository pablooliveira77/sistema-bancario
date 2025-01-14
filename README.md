# Projeto de Criação de um Sistema Bancário usando Python

Este código implementa um sistema bancário simples em Python, permitindo que o usuário realize operações como depósito, saque, visualização de extrato e saída do sistema. O código utiliza um menu interativo e funciona em loop até que o usuário decida sair. Abaixo está uma explicação detalhada de cada parte do código.

### Menu Interativo

O menu apresenta as opções disponíveis para o usuário:
- **[d]**: Depósito.
- **[s]**: Saque.
- **[e]**: Extrato.
- **[q]**: Sair do sistema.

### Depósito

1. Solicita o valor a ser depositado.
2. Valida se o valor é positivo.
3. Atualiza o saldo e registra a operação no extrato.

### Saque

1. Limita o número de saques a 3 por dia.
2. Verifica se o valor do saque é válido (positivo, menor ou igual ao saldo, e dentro do limite diário de R$ 500).
3. Atualiza o saldo e registra a operação no extrato, se aprovado.

### Extrato

1. Exibe todas as transações realizadas (depósitos e saques).
2. Mostra o saldo atual.

### Sair

Interrompe o loop principal, encerrando o programa.

---

## Funcionalidades do Sistema

- **Controle de saldo**: O sistema mantém um saldo atualizado a cada transação.
- **Limitação de saques**: Apenas 3 saques permitidos por dia, com um limite máximo de R$ 500 por saque.
- **Histórico de transações**: Todas as operações são registradas e podem ser visualizadas no extrato.

---

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código acima em um arquivo chamado `sistema_bancario.py`.
3. Execute o programa usando o comando:

```bash
python sistema_bancario.py
```
