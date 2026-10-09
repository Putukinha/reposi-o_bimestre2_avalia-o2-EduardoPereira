# Base - Controle De Leituras

Esta é a aplicação-base da avaliação de reposição da turma 2V.

Ela já possui CRUD de leituras com SQLite, Blueprint de autenticação, Blueprint de leituras e uma função de segurança iniciada em `seguranca.py`. A autenticação com `session` e o controle de acesso por usuário ainda precisam ser implementados.

## Executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`.

## Arquivos Principais

- `app.py`: cria a aplicação e registra os Blueprints.
- `auth.py`: rotas de cadastro, login e logout a serem completadas.
- `leituras.py`: rotas do CRUD de leituras.
- `seguranca.py`: função de proteção das rotas privadas.
- `database.py`: funções de banco de dados.
- `templates/`: páginas HTML.

## Observação

Não substitua a aplicação por outro projeto. A tarefa é adaptar esta base para autenticação com `session`, vinculando cada leitura ao usuário logado.

## Justificativa

1- O app.py funciona como o ponto central do sistema: a função dele é só inicializar o Flask, configurar a chave secreta e registrar os Blueprints. Mover a lógica do CRUD e as rotas específicas para leituras.py evita que o arquivo principal fique poluído, deixando a estrutura limpa e bem mais fácil de dar manutenção.
2- A aplicação usa a session do Flask para saber quem está navegando. Assim que o login é validado, o código guarda o usuario_id (e geralmente o nome do usuário) nessa sessão. A partir daí, qualquer rota protegida checa se essa chave existe antes de liberar a visualização. Se o usuário não estiver logado, ele é redirecionado direto para a tela de login.
3- A segurança dos dados funciona em três camadas integradas: o seguranca.py atua como a primeira barreira bloqueando qualquer acesso não autenticado, o leituras.py resgata o usuario_id da sessão ativa e o repassa para as operações do sistema, e o database.py aplica a trava final no banco de dados filtrando todas as consultas, edições e remoções com WHERE usuario_id = ?. Com esse fluxo contínuo, a aplicação garante que apenas as informações do próprio usuário logado sejam acessadas ou alteradas, impedindo completamente que alguém veja, edite ou apague os registros de outra pessoa.
