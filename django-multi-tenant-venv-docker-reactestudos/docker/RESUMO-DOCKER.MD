# Docker

**Container:** caixa isolada com o suficiente para rodar a aplicação, usando os recursos do PC diretamente (sem dividir hardware, como faria uma VM).

## Componentes principais

- **Docker Engine:** motor que cria e gerencia os containers.
- **Docker Hub:** repositório online de imagens Docker.
- **Dockerfile:** receita de UMA imagem — define base, dependências, arquivos e comando de start.
- **Docker Compose:** orquestra VÁRIOS containers juntos (app + banco + cache, etc), cuidando de rede, volumes, variáveis de ambiente e dependências entre serviços.
## Dockerfile vs Compose

| | Dockerfile | Compose |
|---|---|---|
| Empacota | Seu código/app | Vários containers juntos |
| Define | Como construir UMA imagem | Como esses containers se conectam e rodam |
| Comando | `docker build -t nome .` | `docker compose up` |

**Fluxo real:** você escreve um Dockerfile pro seu app → escreve um `docker-compose.yml` que builda esse Dockerfile (`build: .`) e sobe outros serviços prontos (ex: MySQL) → roda `docker compose up` e tudo sobe conectado.

### Exemplo de Dockerfile
```dockerfile
FROM node:20
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
CMD ["node", "server.js"]
```

<figure style="max-width:800px;margin:0.5rem auto;">
  <img src="./imagens/camadas-imagem-docker.png" alt="Camadas da imagem Docker" style="max-width:800px;width:100%;height:auto;
  display:block;" />
  <figcaption style="text-align:center;font-size:0.9em;color:#555;">Camadas da imagem</figcaption>
</figure>

### Exemplo de docker-compose.yml
```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: senha
```

## Comandos úteis

```powershell
docker ps -a                    # listar todos os containers
docker system prune -a          # deletar containers, imagens, volumes e redes não usados
docker exec -it <container> /bin/bash  # acessar shell de um container
docker compose up --build       # buildar e subir os serviços
docker compose up               # apenas subir os serviços
```