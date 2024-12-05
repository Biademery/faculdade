# Study App

O **Study App** é uma aplicação mobile desenvolvida em **React Native** com o objetivo de ajudar estudantes a organizarem suas tarefas e metas de estudo por meio de cartões personalizados. A aplicação permite criar, editar e excluir cartões, além de categorizá-los por status. Utiliza o **Firebase** para autenticação de usuários e armazenamento de dados.

---

## Funcionalidades Principais

1. **Autenticação de Usuários**
   - Registro e login utilizando **Firebase Authentication**.
   - Gerenciamento de sessão com **React Context API**.

2. **Gerenciamento de Cartões**
   - Criação, edição e exclusão de cartões de estudo.
   - Organização dos cartões por status:
     - **Backlog**: Cartões que ainda não foram iniciados.
     - **Em Progresso**: Cartões em andamento.
     - **Concluído**: Cartões finalizados.
   - Exibição de cartões que estão próximos ao vencimento (dentro de 15 dias).

3. **Banco de Dados Firebase Firestore**
   - Armazena os cartões de estudo de forma segura e associada a cada usuário autenticado.

---

## Estrutura do Projeto

Abaixo está a arquitetura geral do projeto e o propósito de cada pasta/arquivo.

### Diretórios e Arquivos

- **`assets/`**:
  Contém os recursos estáticos, como imagens e ícones usados na interface do aplicativo.
  - `adaptive-icon.png`: Ícone adaptativo usado para dispositivos móveis.
  - `favicon.png`: Ícone padrão do aplicativo.
  - `icon.png`: Ícone principal do aplicativo.
  - `logo.png`: Logo exibido na tela de login.
  - `splash-icon.png`: Ícone exibido durante o carregamento inicial.

- **`src/`**:
  Diretório principal que contém o código-fonte do aplicativo.
  - **`config/`**:
    - `firebaseConfig.js`: Arquivo de configuração para integração com o Firebase. Contém as chaves e inicialização dos serviços de autenticação e banco de dados.
  - **`contexts/`**:
    - `AuthContext.js`: Gerencia o estado de autenticação do usuário utilizando o Firebase e React Context API.
    - `CartoesEstudoContext.js`: Gerencia os cartões de estudo (criação, leitura, edição e exclusão) e o estado compartilhado entre os componentes.
  - **`screens/`**:
    Contém as telas principais do aplicativo:
    - `ListaCartaoScreen.js`: Tela principal para exibir os cartões organizados por status (Backlog, Em Progresso e Concluído).
    - `EdicaoCartaoScreen.js`: Tela utilizada para criar ou editar cartões de estudo.
    - `LoginScreen.js`: Tela de login para autenticação de usuários.
    - `RegistroScreen.js`: Tela para registro de novos usuários.
    - `TarefasVencimentoProximoScreen.js`: Tela que exibe cartões com vencimento nos próximos 15 dias.
  - **`App.js`**:
    Arquivo principal da aplicação:
    - Configura os provedores de contexto.
    - Gerencia as rotas de navegação (públicas e privadas).
   
    
```
├── assets/                 # Recursos estáticos como imagens e ícones
├── src/
│   ├── config/            # Arquivos de configuração
│   │   └── firebaseConfig.js  # Inicialização e config do Firebase
│   ├── contexts/          # Provedores de Context do React
│   │   ├── AuthContext.js     # Gerenciamento do estado de autenticação
│   │   └── CartoesEstudoContext.js  # Gerenciamento dos cartões de estudo
│   └── screens/           # Telas da aplicação
│       ├── EdicaoCartaoScreen.js    # Tela de edição de cartões
│       ├── ListaCartaoScreen.js     # Tela principal de listagem
│       ├── LoginScreen.js           # Tela de autenticação
│       ├── RegistroScreen.js        # Tela de Registro
│       └── TarefasVencimentoProximoScreen.js  # Tela de tarefas próximas
├── App.js                 # Componente Pai
├── app.json             
├── babel.config.js       # Configuração do Babel
└── package.json          # Dependências do projeto
```

---

## Dependências do Projeto

Abaixo estão as dependências utilizadas no projeto:

### Dependências Principais

- **React Native**: Framework principal para desenvolvimento mobile.
- **Expo**: Ferramenta para simplificar o desenvolvimento, teste e execução do app.
- **Firebase**:
  - **Authentication**: Para registro e login de usuários.
  - **Firestore**: Para armazenamento dos dados dos cartões de estudo.
- **React Navigation**:
  - **@react-navigation/native**: Para navegação principal.
  - **@react-navigation/stack** e **@react-navigation/native-stack**: Para navegação baseada em pilha.
- **React Context API**: Para gerenciamento de estado global.
- **React Native Async Storage**: Para armazenamento local.
- **React Native Picker**: Componente para seleção de opções (dropdown).
- **React Native Modal DateTime Picker**: Componente para seleção de data e hora.
- **React Native Vector Icons**: Para uso de ícones.
- **React Native Safe Area Context**: Para gerenciamento de áreas seguras no dispositivo.
- **Expo Local Authentication**: Para autenticação local (biometria).
- **Expo Status Bar**: Para customização da barra de status.

# Rotas e Navegação

O projeto utiliza o **React Navigation** para gerenciamento das rotas. As rotas estão divididas em:

## Rotas Públicas (acessíveis sem login):

- **LoginScreen**: Tela para autenticação do usuário.
- **RegistroScreen**: Tela para criar uma nova conta.

## Rotas Privadas (protegidas por autenticação):

- **ListaCartaoScreen**: Tela inicial com os cartões organizados por status.
- **EdicaoCartaoScreen**: Tela para criação ou edição de cartões.
- **TarefasVencimentoProximoScreen**: Tela que exibe cartões com vencimento próximo.

---

## Configuração do Ambiente

### Pré-requisitos

- **Node.js** instalado.
- **Conta Firebase** com os serviços de Authentication e Firestore configurados.

---

### Passos para Instalação

1. **Clone o Repositório**

```bash
git clone https://github.com/Biademery/faculdade
cd faculdade/study-app-main
```

2. Instale as Dependências

```bash
npm install
```

3. Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as seguintes informações:

```bash
FIREBASE_API_KEY=<sua-api-key>
FIREBASE_AUTH_DOMAIN=<seu-auth-domain>
FIREBASE_PROJECT_ID=<seu-project-id>
FIREBASE_STORAGE_BUCKET=<seu-storage-bucket>
FIREBASE_MESSAGING_SENDER_ID=<seu-messaging-sender-id>
FIREBASE_APP_ID=<seu-app-id>
```
4. Inicie o Projeto

Para executar o projeto em um emulador ou dispositivo:

```bash
npm start
```
