
# 🎵 Yfitops - Music Playlist

<p align="center">
  <img src="assets/banner.png" alt="Banner" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-6f42c1?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Interface-6f42c1?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Flask-API-6f42c1?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/REST-API-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Concluído-black?style=for-the-badge">
</p>

> Aplicação desenvolvida em Python que utiliza **Flask** como API REST e **Streamlit** como interface para exibir uma playlist e reproduzir vídeos do YouTube.

---

# ✨ Funcionalidades

- 🎵 Exibe uma playlist de músicas.
- ▶️ Reproduz vídeos do YouTube diretamente na interface.
- 🌐 Consome uma API REST desenvolvida em Flask.
- 📋 Lista todas as músicas cadastradas.
- 🔎 Busca músicas por ID.
- ➕ Possui endpoint para adicionar novas músicas.
- 🎨 Interface personalizada com CSS.

# 🏗 Arquitetura

```text
Usuário
   │
   ▼
Interface Streamlit
   │ Requests
   ▼
API Flask
   │
Lista de músicas
   │
Links do YouTube
```

# 🛠 Tecnologias

- Python
- Streamlit
- Flask
- Requests
- HTML/CSS
- REST API
- YouTube

# 📂 Estrutura

```text
projeto-fabrica-5/
├── app.py          # Interface Streamlit
├── api.py          # API Flask
├── requirements.txt
├── assets/
│   ├── banner.png
│   └── demo.gif
└── README.md
```

# 🚀 Como executar

```bash
git clone https://github.com/ArroZh/projeto-fabrica-5.git
cd projeto-fabrica-5
pip install -r requirements.txt
```

Inicie a API:

```bash
python api.py
```

Em outro terminal, execute a interface:

```bash
streamlit run app.py
```

- Interface: http://localhost:8501
- API: http://127.0.0.1:5000

# 📡 Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | /musicas | Lista todas as músicas |
| GET | /musicas/{id} | Retorna uma música |
| POST | /musicas | Adiciona uma música |


# 💡 Aprendizados

- Consumo de APIs REST
- Desenvolvimento com Flask
- Interfaces com Streamlit
- Organização cliente-servidor
- Manipulação de JSON
- Requisições HTTP com Requests

# 🔮 Melhorias Futuras

- [ ] Banco de dados SQLite
- [ ] Login de usuários
- [ ] Busca por nome
- [ ] Favoritos
- [ ] Playlist personalizada
- [ ] Reprodução automática
- [ ] Barra de progresso
- [ ] Controle de volume

# 👩‍💻 Autora

**Hannah Yasmin Rodrigues de Lima**

GitHub: https://github.com/ArroZh

---

⭐ Se este projeto foi útil, considere deixar uma estrela no repositório!
