# Entrega2
login de usuário

Instruções de uso:
O usuário deve entrar com dados de login e senha e se este existir será informado que o usuário é o correto e seu nível de permissão.

class_user.py:

A lógica do programa foi criar uma classe usuário (class_user), definindo seus atributos (login, senha e nível de permissões) e seus métodos (checar senha e nível de permissões). Para a senha foi utilizada a biblioteca hashlib, fazendo com que a senha de um usuário salvo seja vinculada a uma hash, a fim de obter melhor segurança e um certo nível de criptografia.

subclass_user_default.py, subclass_user_moderator.py, subclass_user_administrator.py:

A partir desta classe foram criadas subclasses (subclass_user_default, subclass_user_moderator, subclass_user_administrator) com nível de permissão de usuário definido. O que todas têm em comum é que no método para checar a senha (check_password) é comparado se a senha digitada tem hash vinculada e se esta condiz com a da senha digitada.
Além disso, cada subclasse tem dentro do seu método de checar o nível do usuário (check_userlevel) a instrução de printar sua permissão correspondente.
Ademais, o motivo para a escolha de separar em subclasses cada nível de usuário é de que seja possível e mais simples de adicionar métodos/funções personalizados para cada nível de usuário individualmente.

login_main.py:

É utilizado um vetor que armazena os usuários definidos de acordo com seu nível de usuário (objetos definidos nas subclasses). Após isso o programa pede ao usuário um input para o login e entre em um loop de tratamento de erro caso o usuário digite um login que não seja com letras, números e/ou sublinhado. este tratamento de erro é feito com "try" e "except", no try é utilizado um recurso do biblioteca re que faz essa verificação, se caso o usuário digitar corretamente. ele sai do loop no break, se não o programa força um erro com "raise ValueError" e vai para o except que pede para fazer  entrada do login corretamente. Depois é requisitado ao usuário entrar com uma senha e a partir disso o programa entra dentro de um laço for que vai verificar para cada objeto usuário armazenado no vetor inicial, corresponde com o login e a senha digitados.

