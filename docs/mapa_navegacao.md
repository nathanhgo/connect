# Mapa de Navegação

Esse diagrama é um rascunho, focado em ilustrar o fluxo de telas e navegação do aplicativo mobile (React Native).



```mermaid
graph TD
    %% Estilização Básica
    classDef auth fill:#f9f2f4,stroke:#d9534f,stroke-width:2px;
    classDef main fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef module fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;

    A([Splash Screen]) --> B{Autenticado?}
    
    %% Fluxo de Autenticação (Stack Navigation)
    subgraph Auth [Fluxo de Autenticação]
        B -- Não --> C[Tela de Login]
        C --> D[Criar Conta]
        D --> E[Validação de E-mail Institucional]
        E --> C
    end
    class C,D,E auth;

    %% Fluxo Principal (Tab Navigation)
    B -- Sim --> F[[Menu Principal - Bottom Tabs]]
    
    F --> G[🏠 Dashboard / Resumo]
    F --> H[🚗 Módulo de Caronas]
    F --> I[🛏️ Módulo de Moradias]
    F --> J[👤 Perfil do Usuário]
    class G,H,I,J main;

    %% Subfluxo de Caronas
    subgraph Caronas [Fluxo: Mobilidade]
        H --> H1[Mapa em Tempo Real]
        H --> H2[Oferecer Nova Carona]
        H1 --> H3[Detalhes da Rota / Motorista]
        H3 --> H4((Chat Interno))
    end
    class H1,H2,H3 module;

    %% Subfluxo de Moradias
    subgraph Moradias [Fluxo: Habitação]
        I --> I1[Mural de Vagas]
        I1 --> I2[Filtros Avançados<br/>Tipo, Gênero, Distância]
        I --> I3[Anunciar Nova Moradia]
        I1 --> I4[Detalhes da Vaga / Fotos]
        I4 --> I5((Chat Interno))
    end
    class I1,I2,I3,I4 module;

    %% Subfluxo de Perfil
    subgraph Perfil [Configurações]
        J --> J1[Editar Dados e Curso]
        J --> J2[Histórico de Atividades]
        J --> J3[Sair / Logout]
    end