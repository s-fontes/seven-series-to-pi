# Pi Series Calculator

> **Estudo computacional da convergência de séries infinitas para π**
>
> Implementação completa de sete métodos clássicos para calcular π,
com comparação de precisão entre `float` e `double` e parada automática
quando a tolerância desejada é atingida.

---

## 🎯 Objetivo

O projeto investiga como diferentes **séries infinitas** convergem para π
utilizando implementações em C para alta performance e uma interface
Python para visualização. Cada algoritmo executa até que a diferença para
`π` seja inferior a `epsilon`, evitando iterações desnecessárias.

### Principais escolhas de implementação

- **C para velocidade**: as séries são calculadas em C e exportadas como
  biblioteca compartilhada.
- **Dual precision**: todas as rotinas suportam `float` e `double`.
- **Cálculo do erro em C**: garante máxima precisão e facilita o early
  stopping.
- **Integração com Python**: geração de CSV e gráficos usando `matplotlib`.

---

## 📊 Séries Implementadas

| Método | Fórmula resumida | Observações |
|--------|-----------------|-------------|
| **Leibniz** | $\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}$ | Convergência lenta, útil como exemplo didático. |
| **Nilakantha** | $\pi = 3 + \sum_{k=1}^{\infty} \frac{4}{(2k)(2k+1)(2k+2)}$ | Convergência moderada, alternando sinais. |
| **Euler** | $\pi = \sqrt{6 \sum_{k=1}^{\infty} \frac{1}{k^2}}$ | Conhecida como série de Basel; cresce lentamente. |
| **Machin** | $\frac{\pi}{4} = 4\arctan(1/5) - \arctan(1/239)$ | Usa arctangentes para obter poucas iterações. |
| **Ramanujan** | $\frac{1}{\pi} = \frac{2\sqrt{2}}{9801} \sum_{k=0}^{\infty} \frac{(4k)!(1103+26390k)}{(k!)^4 396^{4k}}$ | Série extremamente rápida, explorando fatoriais. |
| **Chudnovsky** | $\frac{1}{\pi} = 12 \sum_{k=0}^{\infty} \frac{(-1)^k(6k)!(545140134k + 13591409)}{(3k)!(k!)^3(640320)^{3k+3/2}}$ | Método moderno com altíssima precisão. |
| **BBP** | $\pi = \sum_{k=0}^{\infty} \frac{1}{16^k}\Bigl(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6}\Bigr)$ | Permite calcular dígitos isolados em base 16. |

Cada função retorna um vetor de `PiResult` contendo o valor aproximado e
o número de iterações. O critério de parada é |π_calc − π| < epsilon.

---

## 🏗️ Estrutura do Projeto

```
seven-series-to-pi/
├── csrc/           # Implementações em C
├── py/             # Interface Python e testes
├── out/            # Resultados gerados (CSV e gráficos)
├── build/          # Biblioteca compilada
├── Makefile        # Automação de build e testes
└── requirements.txt
```

---

## 🚀 Como Usar

### Execução rápida
```bash
# Clonar o repositório
git clone <repo-url>
cd seven-series-to-pi

# Compilar e executar todas as séries
make run EPS=1e-5

# Executar testes
make test
```

### Comandos úteis
```bash
make build      # Compila a biblioteca C
make run        # Calcula π e gera gráficos
make analysis   # Gera CSV de convergência
make test       # Executa testes rápidos
make test-all   # Executa a suíte completa
make test-coverage  # Gera relatório de cobertura
make clean      # Remove build e objetos
make clean-out  # Remove dados em out
make distclean  # Limpeza completa
make lint       # Formata o código
make verify     # Lint + testes
```

Os resultados são salvos em `out/data/*.csv`, `out/graphs/*.png` e
`out/analysis/convergence.csv`.

### Usando GitHub Codespaces

Para quem nunca utilizou o **Codespaces**, é possível executar o projeto
diretamente no navegador sem precisar instalar nada localmente. Siga os
passos abaixo:

1. Abra o repositório no GitHub e clique em **Code → Codespaces → Create codespace**.
2. Aguarde a finalização da criação do ambiente. O GitHub utilizará o arquivo
   `.devcontainer` para configurar tudo automaticamente.
3. Assim que o VS Code Web carregar, abra um terminal dentro do Codespace.
4. No terminal, rode `make build` para compilar a biblioteca C.
5. Em seguida, execute `make run EPS=1e-5` para gerar os resultados e gráficos.
6. (Opcional) Execute `make test` para rodar a suíte de testes.


---

## 📈 Resultados de Performance

Para `epsilon = 1e-3`, observou-se que Ramanujan e Chudnovsky convergem
em 1–2 iterações, Machin e BBP em cerca de 3, Nilakantha em torno de 6 e
Euler/Leibniz precisam de centenas ou milhares de passos.

Usar `double` costuma reduzir o número de iterações e aumentar a
estabilidade numérica em comparação com `float`.

---

## 📝 Licença

Este projeto é open source. Consulte [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Abra issues ou pull requests para
sugerir melhorias.
