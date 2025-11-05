🧮 Programação Linear em Python

Este repositório contém códigos desenvolvidos na disciplina de Programação Linear, com o objetivo de aplicar conceitos de otimização matemática utilizando a linguagem Python e a biblioteca PuLP.

🎯 Objetivo

Os programas aqui apresentados resolvem modelos de maximização e minimização através da formulação de problemas lineares e uso do método solve() da biblioteca PuLP.

Esses modelos são amplamente usados em situações reais, como:

Alocação de recursos;

Planejamento de produção;

Otimização de custos e lucros;

Problemas de transporte e logística.

⚙️ Tecnologias Utilizadas

Python 3

PuLP (biblioteca de otimização linear)

VS Code como ambiente de desenvolvimento

📘 Estrutura dos Códigos

Cada script apresenta:

Definição das variáveis de decisão (ex: quantidade de produtos, horas de trabalho, etc.);

Função objetivo, que pode ser de maximização ou minimização;

Restrições lineares, representando os limites do problema;

Resolução com modelo.solve(), utilizando o solver padrão PULP_CBC_CMD;

Exibição dos resultados, incluindo o status da solução e os valores das variáveis.

🚀 Execução

Para rodar os códigos localmente:

pip install pulp
python nome_do_arquivo.py
