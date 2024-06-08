# LeiloApp

LeiloApp é um projeto em Python que utiliza o framework FastAPI para criar uma aplicação de leilões online.

## Instruções para executar o projeto localmente

1. Certifique-se de ter o Python instalado em sua máquina. Você pode baixá-lo em https://www.python.org/downloads/.

2. Clone o repositório do LeiloApp em seu ambiente local:
    ```
    git clone https://github.com/seu-usuario/LeiloApp.git
    ```

3. Acesse o diretório do projeto:
    ```
    cd LeiloApp
    ```

4. Crie um ambiente virtual para isolar as dependências do projeto:
    ```
    python -m venv venv
    ```

5. Ative o ambiente virtual:
    - No Windows:
      ```
      venv\Scripts\activate
      ```
    - No macOS/Linux:
      ```
      source venv/bin/activate
      ```

6. Instale as dependências do projeto:
    ```
    pip install -r requirements.txt
    ```

7. Execute o servidor local:
    ```
    uvicorn main:app --reload
    ```

8. Acesse a aplicação em seu navegador através do endereço http://localhost:8000.

Divirta-se utilizando o LeiloApp!