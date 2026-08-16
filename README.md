# Radar de Benefícios

Automação em Python desenvolvida para coletar, raspar e consolidar ofertas e descontos de múltiplos portais de vantagens e programas de parcerias em uma base de dados unificada (CSV / JSON).

---

## Portais e Programas Suportados

- **Clube Hapvida**
- **Mastercard Surpreenda**
- **GitHub Student Developer Pack**

---

## Estrutura do Projeto

```text
├── lib/                     # Módulos de extração de cada portal (scrapers)
│   ├── github.py            # Extração de benefícios do GitHub Student Pack
│   ├── hapvida.py           # Extração e automação do portal Clube Hapvida
│   └── surpreenda.py        # Extração de ofertas do Mastercard Surpreenda
├── main.py                  # Script principal que orquestra a coleta
├── .env                     # Configurações regionais e variáveis de ambiente
└── .gitignore
```

---

## Como Executar o Projeto

### 1. Pré-requisitos
- Python 3.10 ou superior
- Navegador Firefox e Geckodriver instalados no sistema

### 2. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/radar-beneficios.git
cd radar-beneficios
```

### 3. Criar e ativar o ambiente virtual
```bash
# Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
.\venv\Scripts\activate
```

### 4. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 5. Configurar o arquivo .env
Crie um arquivo `.env` na raiz do projeto para configurar a região dos portais com filtro regional:
```env
REGIAO="São Paulo"
```

### 6. Executar o scraper
```bash
python main.py
```

Após a execução, um arquivo consolidado `Ofertas.csv` será gerado na raiz com todas as promoções encontradas.

---

## Estrutura dos Dados Exportados

O arquivo de saída contém as seguintes colunas:

| Coluna | Descrição | Exemplo |
| :--- | :--- | :--- |
| `Nome` | Nome do parceiro / serviço | `1Password`, `Abbraccio`, `Cursos IA` |
| `Beneficio` | Descrição da vantagem / desconto | `1 ano grátis`, `Pague 1 Leve 2`, `20% OFF` |
| `Programa de Beneficios` | Nome do programa de origem | `Hapvida`, `Surpreenda`, `GitHub Student` |

---

## Licença

Este projeto é de código aberto sob a licença [MIT](LICENSE).