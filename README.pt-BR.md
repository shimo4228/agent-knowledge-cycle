Language: [English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | Português (Brasil) | [Español](README.es.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200727.svg)](https://doi.org/10.5281/zenodo.19200727)

Um ciclo de conhecimento para agentes de IA — que cresce junto com as pessoas que o moldam.

## O que é o AKC

O AKC trata o conhecimento do agente como um **ativo vivo**: episódios são registrados de forma imutável, destilados em padrões, promovidos a regras e auditados continuamente. Seis fases compostáveis (Research → Extract → Curate → Promote → Measure → Maintain) mantêm habilidades, regras e documentação alinhadas à realidade. Sem um laço de manutenção, o conhecimento do agente se degrada: habilidades ficam desatualizadas, regras se contradizem e a documentação se afasta do código.

Este não é um laço de otimização unidirecional — o ciclo também muda o humano. Veja [Por que um ciclo?](#por-que-um-ciclo) abaixo.

O AKC é entregue como especificações, schemas, ADRs e uma implementação de referência mínima. Traga seu próprio LLM e seu próprio adaptador.

## O que há neste repositório

```
agent-knowledge-cycle/
├── docs/
│   ├── akc-cycle.md              # Regras de comportamento — o ciclo inteiro como um único arquivo de regras
│   ├── scaffold-dissolution.md   # Habilidades são andaimes; e aqui está como elas se dissolvem
│   ├── inspiration.md            # Trabalho anterior
│   ├── adr/
│   │   ├── 0002-immutable-episode-log.md         # JSONL, append-only, umask 0600
│   │   ├── 0003-three-layer-distillation.md      # Raw → Knowledge → Identity/Rules
│   │   ├── 0004-two-stage-distill-pipeline.md    # Texto livre → formato estruturado
│   │   ├── 0005-human-approval-gate.md           # Sem promoção automática a regras
│   │   ├── 0008-code-and-llm-collaboration.md    # Código detém o fluxo de controle; o LLM detém o significado
│   │   ├── 0009-akc-is-a-cycle-not-a-harness.md  # O ciclo é a única característica definidora
│   │   ├── 0010-human-cognitive-resource-as-central-constraint.md  # signal-first Research; economia cognitiva
│   │   └── 0011-cycle-applies-to-any-knowledge-body.md  # O ciclo é neutro quanto ao gênero do que flui por ele
│   └── skills/                   # Habilidades de padrão de projeto pareadas 1:1 com ADRs
│       ├── when-code-when-llm.md                 # Por tarefa: estrutural vs semântico
│       ├── code-and-llm-collaboration.md         # Por pipeline: quatro padrões de camadas
│       └── signal-first-research.md              # Design do filtro de intake para o ADR-0010
├── schemas/
│   ├── episode-log.schema.json   # Formato de registro da Layer 1
│   └── knowledge.schema.json     # Formato de padrão da Layer 2
└── examples/
    ├── minimal_harness/          # Demo de mecanismo — ciclo sobre padrões comportamentais
    │   ├── episode_log.py        # Layer 1
    │   ├── knowledge_store.py    # Layer 2 + decaimento temporal + validação por substrings proibidas
    │   ├── distill.py            # Pipeline em duas etapas, independente de LLM
    │   └── demo.py               # python3 -m examples.minimal_harness.demo
    └── constitution_amend/       # Referência a um consumidor — ciclo sobre valores constitucionais
        └── README.md             # Mapeia as fases do AKC sobre o fluxo de emenda do contemplative-agent
```

Oito ADRs, oito princípios de design, três habilidades de padrão de projeto, dois JSON schemas, uma implementação de referência executável de cerca de 300 linhas e o arquivo de regras que instala todo o ciclo com um único `cp`. O AKC define três camadas de memória e quatro padrões de camadas entre código e LLM. As seis cycle skills listadas abaixo continuam sendo a implementação opinionada e completa de cada fase.

O AKC entrega **dois tipos de habilidades**:

- **Cycle skills** (repositórios externos) — uma para cada fase do laço de autoaprimoramento: `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — guias longos de «how» pareados 1:1 com ADRs. São transversais e se aplicam a múltiplas fases.

## O ciclo

O AKC é um conjunto de seis habilidades compostáveis que formam um laço fechado de autoaprimoramento:

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

Cada habilidade cuida de uma fase do ciclo de vida do conhecimento:

| Skill | Phase | O que faz |
|-------|-------|-----------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | Pesquisar amplamente, filtrar por sinal — absorver apenas o que mudaria a próxima ação |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | Extrair padrões reutilizáveis de sessões com portas de qualidade |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | Auditar habilidades instaladas quanto a obsolescência, conflitos e redundância |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | Destilar princípios transversais das habilidades em regras |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | Testar se os agentes realmente seguem suas habilidades e regras |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | Auditar documentação quanto a sobreposição de papéis, conteúdo obsoleto e registros de decisão ausentes |

## Rules — instale o ciclo sem as habilidades

Você não precisa das seis habilidades para rodar o ciclo. O arquivo [`docs/akc-cycle.md`](docs/akc-cycle.md) destila as seis fases em princípios comportamentais que qualquer agente de IA pode seguir em conversação natural.

### Instalação rápida

```bash
# Copie para o diretório de regras do seu agente
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

É só isso. O ciclo roda pela conversação — sem habilidades, sem plugins, sem ferramentas CLI.

### O que as regras cobrem

| Phase | Resumo da regra |
|-------|-----------------|
| Research | Pesquisar amplamente, filtrar por sinal — absorver apenas o que mudaria a próxima ação |
| Extract | Capturar padrões reutilizáveis de sessões com avaliação de qualidade |
| Curate | Auditar periodicamente redundância, obsolescência e silêncio |
| Promote | Elevar padrões que se repetem 3+ vezes para a camada de regras |
| Measure | Verificar mudança de comportamento quantitativamente, não subjetivamente |
| Maintain | Manter os papéis da documentação limpos e o conteúdo fresco |

### Skills vs Rules

- **Skills** fornecem fluxos passo a passo e aprofundados para cada fase. Instale-as quando quiser execução guiada.
- **Rules** fornecem princípios e condições de gatilho. Instale-as quando quiser que o ciclo emerja naturalmente da conversação.
- Os dois podem coexistir. Rules garantem que o ciclo rode mesmo quando as habilidades não são acionadas.

## Por que um ciclo

Configuração estática desvia com o tempo. Habilidades são adicionadas mas nunca revisadas. Regras se acumulam mas a conformidade nunca é medida. Documentação envelhece.

O AKC trata o conhecimento do agente como um sistema vivo que exige manutenção contínua — não uma configuração única.

| Problema | Resposta do AKC |
|----------|-----------------|
| Habilidades ficam obsoletas | skill-stocktake audita a qualidade periodicamente |
| Regras não batem com a prática | skill-comply mede a conformidade comportamental real |
| O conhecimento fica espalhado | rules-distill promove padrões recorrentes a princípios |
| A documentação desvia | context-sync detecta sobreposições de papéis e conteúdo obsoleto |
| Rodas são reinventadas | search-first checa se já existe uma solução |
| Aprendizados se perdem | learn-eval extrai padrões com portas de qualidade |

O ciclo também muda o humano. Ao repetir decisões de Curate e Promote, os usuários afiam seu julgamento sobre que conhecimento vale a pena manter. Através de Research, desenvolvem melhor intuição sobre quando adotar soluções existentes versus construir novas. Através de Measure, aprendem o que distingue uma boa regra de uma aspiração vaga. O AKC não é um laço de otimização unidirecional em que o agente melhora isoladamente — é um laço de crescimento bidirecional em que humano e agente se desenvolvem juntos por meio de interação sustentada.

### De quem é o orçamento cognitivo que o ciclo está protegendo?

O do humano. À medida que a capacidade do agente cresce, o recurso escasso deixa de ser computação ou contexto e passa a ser **atenção e julgamento humanos**. As fases do AKC são moldadas em torno dessa escassez: Research é signal-first para que a ingestão não ultrapasse a digestão; Promote converte decisões recorrentes em regras, para que o mesmo julgamento não seja refeito a cada sessão; Measure substitui a reauditoria manual por verificações de conformidade observáveis; e o diálogo pré-implementação é antecipado porque desalinhamento de intenção descoberto na revisão custa mais do que a conversa que o teria evitado. Rodar o ciclo não é de graça — mas é assim que o ciclo protege o único recurso que não escala com o modelo. Veja [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

## Princípios de design

1. **Composable** — Cada habilidade funciona de forma independente. Use uma ou todas as seis.
2. **Observable** — skill-comply produz taxas de conformidade quantitativas, não avaliações subjetivas.
3. **Non-destructive** — Toda habilidade propõe mudanças e espera confirmação. Nada é aplicado automaticamente.
4. **Tool-agnostic in concept** — Projetado para Claude Code, mas a arquitetura se aplica a qualquer agente com configuração persistente.
5. **Evaluation scales with model capability** — Modelos pequenos se beneficiam de pontuação baseada em rubrica; modelos de raciocínio (classe Opus) avaliam com contexto completo e julgamento qualitativo. O AKC não prescreve uma abordagem única — ele ajusta a profundidade da avaliação à capacidade de raciocínio do modelo.
6. **Scaffold dissolution** — Habilidades são andaimes. À medida que usuário e agente interiorizam o ciclo, as habilidades se tornam desnecessárias e apenas as regras sustentam o laço. Veja [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md).
7. **Code-LLM Layering** — O código detém determinismo, auditabilidade e fluxo de controle. O LLM detém o significado. Faça a separação em camadas de forma explícita; nunca deixe o LLM deter estado durável ou condição de término. Veja [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md).
8. **Human cognitive resource is the bottleneck** — À medida que a capacidade do agente cresce, o recurso escasso deixa de ser computação ou contexto e passa a ser a atenção e o julgamento humanos. Toda fase é moldada para proteger esse orçamento: intake signal-first em Research, promoção de regras para que a mesma decisão não seja refeita, medição de conformidade para que o humano não reaudite manualmente, e diálogo antecipado porque implementação desalinhada custa mais do que a conversa que a teria evitado. Veja [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).
9. **Genre neutrality** — O ciclo é um mecanismo, não conteúdo. As mesmas seis fases operam sobre qualquer corpo coerente de conhecimento do agente — padrões comportamentais, expertise de domínio ou valores constitucionais — e o AKC não toma posição sobre qual deles um projeto a jusante prioriza. O que muda por gênero são os critérios de avaliação, os templates de prompt e as consultas de auditoria; as fases permanecem idênticas. Veja [ADR-0011](docs/adr/0011-cycle-applies-to-any-knowledge-body.md).

## Relação com Harness Engineering

O AKC compartilha terreno comum com [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — a prática de engenheirar soluções para que um agente nunca repita o mesmo erro, combinando prompts melhorados (por exemplo, atualizações em AGENTS.md) e ferramentas programáticas (scripts, comandos de verificação). Ambos visam tornar os agentes mais confiáveis, mas o foco é diferente.

| Camada | Pergunta | Endereçada por |
|--------|----------|----------------|
| Harness | «Esta saída está correta?» | Linters, testes e scripts individuais |
| AKC | «Os próprios harnesses ainda são válidos?» | skill-comply, skill-stocktake, context-sync |

**Correção vs alinhamento de intenção.** O harness engineering foca em obter o resultado certo de primeira — prevenir erros conhecidos por meio de melhores instruções e checagens automáticas. O AKC se preocupa mais com outra pergunta: «isso está alinhado com a intenção do dono?» Um agente pode evitar todos os erros conhecidos e ainda divergir da intenção de design. O Princípio de design #3 (Non-destructive) reflete isso — proponha e espere confirmação, porque alinhamento de intenção é difícil de automatizar totalmente.

**Reativo vs proativo.** O harness engineering é reativo por natureza — cada erro dispara um novo harness. O skill-comply e o skill-stocktake do AKC adotam uma postura proativa, auditando periodicamente se as habilidades e regras ainda são seguidas e se ainda são relevantes. O Princípio de design #5 escala essa avaliação para a capacidade do modelo — rubricas para modelos pequenos, julgamento holístico para modelos de fronteira.

## Customização

As implementações de referência linkadas acima são pontos de partida. Faça fork, reescreva, adapte ao seu agente e fluxo de trabalho. O AKC define o ciclo — não a implementação. O que importa é que as fases (extract → curate → promote → measure → maintain) formem um laço fechado, não como cada fase é construída.

## Origem

Esta arquitetura foi primeiro proposta e implementada por Tatsuya Shimomoto ([@shimo4228](https://github.com/shimo4228)) em fevereiro de 2026.

As cinco primeiras habilidades foram contribuídas ao [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) entre fevereiro e março de 2026. O context-sync foi desenvolvido de forma independente.

## Como citar

Se você usar ou referenciar a arquitetura Agent Knowledge Cycle, por favor cite:

```bibtex
@software{shimomoto2026akc,
  author       = {Shimomoto, Tatsuya},
  title        = {Agent Knowledge Cycle (AKC)},
  year         = {2026},
  doi          = {10.5281/zenodo.19200727},
  url          = {https://doi.org/10.5281/zenodo.19200727},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

Ou no texto:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.19200727

## Trabalhos relacionados

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) —
  Um repositório de pesquisa independente explorando Contemplative Constitutional AI
  em um modelo local de 9B. Seu substrato de engenharia (memória em três
  camadas, destilação em duas etapas) foi o trabalho anterior que
  plantou as sementes dos ADRs do AKC. Veja [`docs/inspiration.md`](docs/inspiration.md) para detalhes.
- [Agent Attribution Practice (AAP)](https://github.com/shimo4228/agent-attribution-practice) —
  Biblioteca irmã de gênero (DOI [10.5281/zenodo.19652014](https://doi.org/10.5281/zenodo.19652014)).
  O trio de segurança extraído no AKC v2.0.0 (ADR-0001, ADR-0006, ADR-0007)
  foi reexpresso ali, junto com cinco ADRs adicionais, como oito ADRs
  harness-neutral sobre a distribuição da accountability em agentes de IA
  autônomos. AKC é o ciclo (mecanismo); AAP é a prática (conteúdo).
- [Artigos no Zenn](https://zenn.dev/shimo4228) — Diário de desenvolvimento (em japonês)
- [Artigos no Dev.to](https://dev.to/shimo4228) — Traduções em inglês

## Agradecimentos

O AKC está sobre a base do [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)
de [@affaan-m](https://github.com/affaan-m). O ECC era o harness de
base que eu usava todos os dias, e suas habilidades e regras me deram
um ponto de partida rico sobre o qual construir. Ao longo de meses de
uso diário, adicionei minhas próprias habilidades e regras sobre o
ECC, e elas proliferaram mais rápido do que eu conseguia acompanhar —
habilidades ficavam obsoletas, regras começavam a se contradizer, a
documentação se afastava do código. Eu precisava constantemente
auditar a bagunça e decidir o que manter, o que fundir e o que
promover a uma regra duradoura. O ciclo de seis fases é o que esse
trabalho recorrente de manutenção parecia quando notei o seu formato.

Sem o ECC como chão para pisar, o AKC não existiria. Um agradecimento profundo ao affaan-m e a todo(a) contribuinte do ECC.

## References

O AKC foi construído a partir da prática, não da teoria. As obras a
seguir não foram consultadas durante o processo descrito acima, mas o
ciclo resultante parece compartilhar algo com as ideias nelas
contidas. Elas são listadas aqui para leitores que possam achar a
ressonância interessante.

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  O laço bidirecional entre humano e agente tem algo em comum com
  a ideia enativista de acoplamento estrutural.
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — O modo como o humano atualiza
  regras e habilidades observando o que o agente de fato faz lembra
  vagamente um laço de automodelagem recursiva.

## License

MIT
