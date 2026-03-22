# Mapa de endpoints da API

Mapa do contrato de dados que precisaremos construir. Isso guiará o Swagger e as telas do aplicativo.

### Autenticação e Perfil (App core)
|Método|Endpoint  |Descrição |
|--|--|--|
| POST | /api/auth/registro/ | Recebe e-mail, senha e nome. Valida o domínio institucional obrigatoriamente. |
| POST | /api/auth/login/ | Recebe credenciais e devolve o Token JWT de acesso. |
| GET | /api/auth/me/ | Retorna os dados do usuário logado (foto, curso, reputação). |

### Módulo de moradias (App moradias)
|Método|Endpoint  |Descrição |
|--|--|--|
| GET | /api/moradias/ | Lista vagas. Aceita _query params_ de filtro (ex: `?tipo=kitnet&genero=feminino`). |
| POST | /api/moradias/ | Cria um novo anúncio de moradia. |
| GET | /api/moradias/[id] | Retorna os detalhes completos, regras e fotos de uma vaga específica. |


### Módulo de mobilidade (App caronas)
|Método|Endpoint  |Descrição |
|--|--|--|
| GET | /api/caronas/ | Lista caronas ativas do dia. Aceita parâmetros de rota. |
| POST | /api/caronas/ | Motorista publica uma rota (Origem, Destino, Vagas, Valor). |
| POST | /api/caronas/[id]/solicitar/ | Passageiro envia um pedido para ocupar um assento naquela viagem. |

Obs: Esse mapa não exclui a necessidade de outros endpoints, é apenas um mapa inicial para desenvolvimento.