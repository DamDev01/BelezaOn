# BelezaOn
Sistema Web para gerenciamento de Salão de Beleza
Visão Geral
Este projeto é um sistema de gestão de salão de beleza desenvolvido com Django e integrado com AdminLTE 3 para a interface do usuário. O sistema permite agendamento de serviços, gerenciamento de clientes, visualização de agendamentos pendentes e concluídos, e redefinição de senha.

Funcionalidades
Agendamento de Serviços: Permite aos usuários agendar serviços de beleza.
Gerenciamento de Clientes: Cadastro e atualização de informações dos clientes.
Visualização de Agendamentos: Listagem de agendamentos pendentes e concluídos.
Redefinição de Senha: Funcionalidade para que os usuários possam redefinir suas senhas em caso de esquecimento.
Dashboard: Interface administrativa integrada com AdminLTE 3.
Tecnologias Utilizadas
Django: Framework web utilizado para o backend.
AdminLTE 3: Template de dashboard utilizado para a interface administrativa.
Bootstrap: Framework CSS utilizado para estilização.
Font Awesome: Biblioteca de ícones.
HTML/CSS/JavaScript: Linguagens para estruturação e comportamento das páginas web.

# Estrutura de Pastas

projeto_salao/
│
├── manage.py
├── requirements.txt
├── README.md
├── salon/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── adminlte/
│   │   └── ...
│   ├── static/
│   │   ├── adminlte3/
│   │   └── ...
│   └── migrations/
│       └── ...
├── templates/
│   ├── base.html
│   ├── index.html
│   └── ...
└── static/
    ├── css/
    ├── js/
    └── images/


# Instalação e Configuração
Pré-requisitos
Python 3.9+
Django 4.2.13

Página de Login
Acesse a página de login em http://127.0.0.1:8000/login/ e entre com suas credenciais.

Dashboard
Após fazer login, você será redirecionado para o dashboard, onde poderá visualizar e gerenciar agendamentos e clientes.

Redefinição de Senha
Na página de login, clique em "Esqueceu a senha?" para redefinir sua senha. Você será redirecionado para uma página onde poderá inserir seu email e receber instruções para redefinir sua senha.

# Contribuição
Contribuições são bem-vindas! Para contribuir:

Faça um fork do repositório.
Crie uma branch para sua feature/bugfix (git checkout -b feature/nova-feature).
Faça commit das suas alterações (git commit -m 'Adiciona nova feature').
Envie para o repositório remoto (git push origin feature/nova-feature).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


