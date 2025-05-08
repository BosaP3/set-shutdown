# 💻 Set Shutdown

Interface gráfica em Python para agendar o desligamento automático do computador, seja por horário específico ou por contagem regressiva. Projeto construído com `Tkinter` e arquitetura modular para facilitar a manutenção e extensão.

## 🧩 Funcionalidades

- ⏰ Agendamento de desligamento por data e hora exata
- ⏳ Agendamento por contagem regressiva (timer)
- 🧼 Interface desenvolvida com `Tkinter`
- 🔁 Cancelamento de desligamento agendado

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/BosaP3/set-shutdown.git
cd set-shutdown
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências
```bash 
pip install -r requirements.txt
```


### 4. Execute a aplicação
```bash 
python main.py
```

## ⚙️ Requisitos

Python 3.8+

Sistemas operacionais suportados

- Windows (comando shutdown nativo)

## 🛠️ Geração de Executável (OPCIONAL)

```bash 
pyinstaller --onefile --windowed --noconsole --icon=icons/blue_shutdown.ico main.py
```

## 📝 TODO
1. 🔐 Adicionar autenticação ou senha para restringir o agendamento de desligamentos
2. 📋 Log de atividades para rastrear os agendamentos realizados
3. ⏳ Limites de tempo configuráveis (ex: não permitir agendamento abaixo/acima de X minutos)
4. 🔗 Integração com política de grupo/local
