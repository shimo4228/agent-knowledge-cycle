Language: [English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | Português (Brasil) | [Español](README.es.md)

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200726.svg)](https://doi.org/10.5281/zenodo.19200726)

<details>
<summary>Ordem de leitura para agentes de IA</summary>

1. [`graph.jsonld`](graph.jsonld) — mapa canônico de relações legível por máquina (seis fases, binding fase-skill, três camadas de memória, padrões code-LLM)
2. [`llms.txt`](llms.txt) — índice de navegação compacto
3. [`llms-full.txt`](llms-full.txt) — referência factual consolidada
4. README e documentos específicos do repositório — narrativa e detalhes

Para o mapa canônico de relações do ecossistema de pesquisa do shimo4228, consulte:
https://github.com/shimo4228/shimo4228/blob/main/graph.jsonld

</details>

Um ciclo de conhecimento para agentes de IA — que cresce junto com as pessoas que o moldam.

## O que é o AKC

O AKC parte de uma única observação: à medida que a capacidade do agente cresce, o recurso escasso deixa de ser computação ou contexto — passa a ser a **atenção e o julgamento humanos** que mantêm o laço em movimento. O AKC está centrado nessa escassez. Veja [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

Proteger esse orçamento reformula para que serve o ciclo. O objetivo não é «que o agente produza uma saída individualmente correta» — é «que o comportamento do agente permaneça alinhado com a intenção do operador ao longo das sessões». A correção pode ser verificada por testes; o alinhamento, não, porque a própria intenção se move à medida que o julgamento do operador se afia com o uso.

O alinhamento, portanto, é sustentado ao longo do tempo, não configurado uma única vez. **O ciclo também muda o humano**: através de decisões repetidas de Curate, Promote e Measure, o julgamento do operador sobre o que constitui um bom comportamento do agente se afia sessão após sessão — por isso a frase-guia diz que o ciclo cresce *junto com* as pessoas que o moldam, não *para* elas. Em termos técnicos, isso é um laço de crescimento bidirecional (bidirectional growth loop) em que o comportamento do agente e o julgamento humano se desenvolvem juntos.

Quem implementa isso são seis fases compostáveis — Research → Extract → Curate → Promote → Measure → Maintain. Ingestão signal-first, para não gastar atenção em informação que não muda a próxima ação; promoção das decisões recorrentes a regras, para não refazer o mesmo julgamento toda vez; verificações de conformidade observáveis, para que o humano não tenha de reauditar manualmente cada sessão. Sem este laço, o conhecimento do agente se degrada — as habilidades ficam obsoletas, as regras se contradizem, a documentação se afasta do código.

O AKC é entregue como especificações, schemas, ADRs e uma implementação de referência mínima. Traga seu próprio LLM e seu próprio adaptador.

## Por que o AKC

### O gargalo se deslocou

À medida que a capacidade do agente cresce, o recurso escasso deixa de ser computação ou contexto e passa a ser a atenção e o julgamento humanos. Cada framework concorrente otimiza o lado do agente — mais ferramentas, mais memória, mais contexto, mais automação. O AKC faz a pergunta inversa: dado que o humano no laço dispõe de um orçamento fixo e diário de atenção e julgamento, como o ciclo deve ser moldado para que esse orçamento não seja desperdiçado?

As fases do AKC são moldadas em torno dessa escassez. Research é signal-first, para que a ingestão não ultrapasse a digestão. Promote converte decisões recorrentes em regras, para que o mesmo julgamento não seja refeito a cada sessão. Measure substitui a reauditoria manual por verificações de conformidade observáveis. O diálogo pré-implementação é antecipado porque o desalinhamento de intenção descoberto na revisão custa mais do que a conversa que o teria evitado. Rodar o ciclo não é de graça — mas é assim que o ciclo protege o único recurso que não escala com o modelo. Veja [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

| Problema de manutenção | Resposta do AKC |
|----------|-----------------|
| Habilidades ficam obsoletas | skill-stocktake audita a qualidade periodicamente |
| Regras não batem com a prática | skill-comply mede a conformidade comportamental real |
| O conhecimento fica espalhado | rules-distill promove padrões recorrentes a princípios |
| A documentação desvia | context-sync detecta sobreposições de papéis e conteúdo obsoleto |
| Rodas são reinventadas | search-first checa se já existe uma solução |
| Aprendizados se perdem | learn-eval extrai padrões com portas de qualidade |

Cada linha substitui uma tarefa de manutenção que, de outra forma, o humano carregaria à mão. O ciclo não é de graça, mas sai mais barato do que refazer a mesma auditoria toda vez que a pergunta volta.

### Alinhado com a intenção, não apenas correto

A correção pode ser automatizada: testes, tipos, linters e ferramentas de revisão verificam se uma saída passa em critérios específicos. O alinhamento não pode ser automatizado no mesmo grau, porque a própria intenção se move à medida que o julgamento do operador se afia com o uso. Um agente pode satisfazer todas as verificações de correção e ainda assim se desviar da intenção.

As escolhas de design do AKC refletem isso. O Princípio de design #3 (Non-destructive) — propor e então esperar confirmação — coloca cada mudança em um ponto de checagem onde a intenção pode ser reformulada. O diálogo pré-implementação é tratado como um **investimento em economia cognitiva**, não como atrito. Essa mesma distinção explica em que o AKC difere da harness engineering: harnesses otimizam a correção de primeira, enquanto o AKC mantém os próprios harnesses alinhados com a intenção à medida que essa intenção evolui. Para a comparação por camadas, veja [Relação com Harness Engineering](#relação-com-harness-engineering).

### O ciclo também muda o humano

Ao repetir decisões de Curate e Promote, os usuários afiam seu julgamento sobre que conhecimento vale a pena manter. Através de Research, desenvolvem melhor intuição sobre quando adotar soluções existentes versus construir novas. Através de Measure, aprendem o que distingue uma boa regra de uma aspiração vaga. O AKC não é um laço de otimização unidirecional em que o agente melhora isoladamente — o comportamento do agente e o julgamento humano se desenvolvem juntos por meio de interação sustentada. A frase-guia — *que cresce junto com as pessoas que o moldam* — nomeia exatamente essa propriedade.

## O que há neste repositório

Nove ADRs, oito princípios de design, três habilidades de padrão de projeto, dois JSON schemas, uma implementação de referência executável de cerca de 500 linhas e o arquivo de regras que instala todo o ciclo com um único `cp`. O AKC define três camadas de memória e quatro padrões de camadas entre código e LLM. As seis cycle skills listadas abaixo continuam sendo a implementação opinionada e completa de cada fase.

O AKC entrega **dois tipos de habilidades**:

- **Cycle skills** (repositórios externos) — uma para cada fase do ciclo: `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — guias longos de «how» pareados 1:1 com ADRs. São transversais e se aplicam a múltiplas fases.

Para a árvore completa do repositório e o roteamento de papéis documentais, veja [`docs/CODEMAPS/architecture.md`](docs/CODEMAPS/architecture.md).

## O ciclo

O AKC é um conjunto de seis habilidades compostáveis, uma para cada fase do ciclo:

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

**Correção vs alinhamento de intenção.** O harness engineering foca em obter o resultado certo de primeira — prevenir erros conhecidos por meio de melhores instruções e checagens automáticas. O AKC se preocupa com outra pergunta: o comportamento do agente continua alinhado com a intenção em evolução do operador? Para o desenvolvimento independente dessa tese, veja [Por que o AKC → Alinhado com a intenção](#alinhado-com-a-intenção-não-apenas-correto).

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
  version      = {2.1.0},
  doi          = {10.5281/zenodo.20076396},
  url          = {https://doi.org/10.5281/zenodo.20076396},
  note         = {A knowledge cycle for AI agents — one that grows with the people who shape it}
}
```

Ou no texto:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.20076396

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
