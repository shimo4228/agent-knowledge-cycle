Language: [English](README.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [Português (Brasil)](README.pt-BR.md) | Español

# Agent Knowledge Cycle (AKC)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19200727.svg)](https://doi.org/10.5281/zenodo.19200727)

Un ciclo de conocimiento para agentes de IA — uno que crece junto con las personas que lo dan forma.

## Qué es AKC

AKC trata el conocimiento del agente como un **activo vivo**: los episodios se registran de forma inmutable, se destilan en patrones, se promueven a reglas y se auditan continuamente. Seis fases componibles (Research → Extract → Curate → Promote → Measure → Maintain) mantienen habilidades, reglas y documentación alineadas con la realidad. Sin un bucle de mantenimiento, el conocimiento del agente se degrada: las habilidades se vuelven obsoletas, las reglas se contradicen entre sí y la documentación se aleja del código.

Este no es un bucle de optimización unidireccional — el ciclo también cambia al humano. Véase [¿Por qué un ciclo?](#por-qué-un-ciclo) más abajo.

AKC se entrega como especificaciones, schemas, ADRs y una implementación de referencia mínima. Trae tu propio LLM y tu propio adaptador.

## Qué hay en este repositorio

```
agent-knowledge-cycle/
├── docs/
│   ├── akc-cycle.md              # Reglas de comportamiento — el ciclo entero como un único archivo de reglas
│   ├── scaffold-dissolution.md   # Las habilidades son andamios; aquí está cómo se disuelven
│   ├── inspiration.md            # Trabajo previo
│   ├── adr/
│   │   ├── 0002-immutable-episode-log.md         # JSONL, append-only, umask 0600
│   │   ├── 0003-three-layer-distillation.md      # Raw → Knowledge → Identity/Rules
│   │   ├── 0004-two-stage-distill-pipeline.md    # Texto libre → formato estructurado
│   │   ├── 0005-human-approval-gate.md           # Sin promoción automática a reglas
│   │   ├── 0008-code-and-llm-collaboration.md    # El código se encarga del flujo de control; el LLM, del significado
│   │   ├── 0009-akc-is-a-cycle-not-a-harness.md  # El ciclo es la única característica definitoria
│   │   ├── 0010-human-cognitive-resource-as-central-constraint.md  # signal-first Research; economía cognitiva
│   │   └── 0011-cycle-applies-to-any-knowledge-body.md  # El ciclo es neutral respecto al género del conocimiento que fluye
│   └── skills/                   # Habilidades de patrón de diseño emparejadas 1:1 con ADRs
│       ├── when-code-when-llm.md                 # Por tarea: estructural vs semántico
│       ├── code-and-llm-collaboration.md         # Por pipeline: cuatro patrones de capas
│       └── signal-first-research.md              # Diseño del filtro de intake para el ADR-0010
├── schemas/
│   ├── episode-log.schema.json   # Forma del registro de la Layer 1
│   └── knowledge.schema.json     # Forma del patrón de la Layer 2
└── examples/
    ├── minimal_harness/          # Demostración del mecanismo — ciclo sobre patrones de comportamiento
    │   ├── episode_log.py        # Layer 1
    │   ├── knowledge_store.py    # Layer 2 + decaimiento temporal + validación de subcadenas prohibidas
    │   ├── distill.py            # Pipeline en dos etapas, agnóstico al LLM
    │   └── demo.py               # python3 -m examples.minimal_harness.demo
    └── constitution_amend/       # Referencia río abajo — ciclo sobre valores constitucionales
        └── README.md             # Mapea las fases de AKC sobre el flujo de enmienda de contemplative-agent
```

Ocho ADRs, ocho principios de diseño, tres habilidades de patrón de diseño, dos JSON schemas, una implementación de referencia ejecutable de unas 300 líneas y el archivo de reglas que instala todo el ciclo con un único `cp`. AKC define tres capas de memoria y cuatro patrones de capas entre código y LLM. Las seis cycle skills listadas a continuación siguen siendo la implementación opinada y completa de cada fase.

AKC entrega **dos tipos de habilidades**:

- **Cycle skills** (repositorios externos) — una por cada fase del bucle de auto-mejora: `search-first`, `learn-eval`, `skill-stocktake`, `rules-distill`, `skill-comply`, `context-sync`.
- **Design-pattern skills** ([`docs/skills/`](docs/skills/)) — guías largas de «how» emparejadas 1:1 con ADRs. Son transversales y aplican a múltiples fases.

## El ciclo

AKC es un conjunto de seis habilidades componibles que forman un bucle cerrado de auto-mejora:

```
Experience → learn-eval → skill-stocktake → rules-distill → Behavior change → ...
               (extract)    (curate)          (promote)            ↑
                                                            skill-comply
                                                              (measure)
                                              context-sync ← (maintain)
```

Cada habilidad atiende una fase del ciclo de vida del conocimiento:

| Skill | Phase | Qué hace |
|-------|-------|----------|
| [search-first](https://github.com/shimo4228/claude-skill-search-first) | Research | Buscar ampliamente, filtrar por señal — ingerir solo lo que cambiaría la siguiente acción |
| [learn-eval](https://github.com/shimo4228/claude-skill-learn-eval) | Extract | Extraer patrones reutilizables de las sesiones con compuertas de calidad |
| [skill-stocktake](https://github.com/shimo4228/claude-skill-stocktake) | Curate | Auditar las habilidades instaladas en busca de obsolescencia, conflictos y redundancia |
| [rules-distill](https://github.com/shimo4228/claude-skill-rules-distill) | Promote | Destilar principios transversales desde las habilidades hacia reglas |
| [skill-comply](https://github.com/shimo4228/claude-skill-comply) | Measure | Comprobar si los agentes realmente siguen sus habilidades y reglas |
| [context-sync](https://github.com/shimo4228/claude-skill-context-sync) | Maintain | Auditar la documentación en busca de solapamiento de roles, contenido obsoleto y registros de decisión faltantes |

## Rules — instala el ciclo sin las habilidades

No necesitas las seis habilidades para hacer girar el ciclo. El archivo [`docs/akc-cycle.md`](docs/akc-cycle.md) destila las seis fases en principios de comportamiento que cualquier agente de IA puede seguir mediante conversación natural.

### Instalación rápida

```bash
# Copia al directorio de reglas de tu agente
cp docs/akc-cycle.md ~/.claude/rules/common/akc-cycle.md
```

Eso es todo. El ciclo correrá a través de la conversación — sin habilidades, sin plugins, sin herramientas CLI.

### Qué cubren las reglas

| Phase | Resumen de la regla |
|-------|---------------------|
| Research | Buscar ampliamente, filtrar por señal — ingerir solo lo que cambiaría la siguiente acción |
| Extract | Capturar patrones reutilizables de las sesiones con evaluación de calidad |
| Curate | Auditar periódicamente redundancia, obsolescencia y silencio |
| Promote | Elevar a la capa de reglas los patrones que se repiten 3+ veces |
| Measure | Verificar el cambio de comportamiento de forma cuantitativa, no subjetiva |
| Maintain | Mantener limpios los roles de la documentación y fresco el contenido |

### Skills vs Rules

- **Skills** ofrecen flujos de trabajo profundos y paso a paso para cada fase. Instálalas cuando quieras ejecución guiada.
- **Rules** ofrecen principios y condiciones de disparo. Instálalas cuando quieras que el ciclo emerja naturalmente de la conversación.
- Ambos pueden coexistir. Las reglas garantizan que el ciclo corra incluso cuando las habilidades no se disparan.

## Por qué un ciclo

La configuración estática se desvía. Las habilidades se añaden pero nunca se revisan. Las reglas se acumulan pero nunca se mide el cumplimiento. La documentación envejece.

AKC trata el conocimiento del agente como un sistema vivo que requiere mantenimiento continuo — no una configuración única.

| Problema | Respuesta de AKC |
|----------|------------------|
| Las habilidades se vuelven obsoletas | skill-stocktake audita la calidad periódicamente |
| Las reglas no coinciden con la práctica | skill-comply mide el cumplimiento real del comportamiento |
| El conocimiento queda disperso | rules-distill promueve patrones recurrentes a principios |
| La documentación se desvía | context-sync detecta solapamientos de roles y contenido obsoleto |
| Se reinventan las ruedas | search-first comprueba primero si ya existe una solución |
| Los aprendizajes se pierden | learn-eval extrae patrones con compuertas de calidad |

El ciclo también cambia al humano. A través de decisiones repetidas de Curate y Promote, los usuarios afinan su criterio sobre qué conocimiento merece conservarse. A través de Research, desarrollan mejor intuición sobre cuándo adoptar soluciones existentes y cuándo construir las propias. A través de Measure, aprenden qué distingue una buena regla de una aspiración vaga. AKC no es un bucle de optimización unidireccional en el que el agente mejora aisladamente — es un bucle de crecimiento bidireccional en el que humano y agente se desarrollan juntos a través de una interacción sostenida.

### ¿De quién es el presupuesto cognitivo que el ciclo está protegiendo?

Del humano. A medida que crece la capacidad del agente, el recurso escaso ya no es cómputo ni contexto, sino **la atención y el juicio humanos**. Las fases de AKC están moldeadas en torno a esa escasez: Research es signal-first para que la ingesta no exceda la digestión; Promote convierte decisiones recurrentes en reglas, para no rehacer el mismo juicio cada sesión; Measure sustituye la reauditoría manual por comprobaciones de cumplimiento observables; y el diálogo previo a la implementación se adelanta porque el desalineamiento de intención descubierto en la revisión sale más caro que la conversación que lo habría evitado. Hacer girar el ciclo no es gratis — pero es así como el ciclo protege el único recurso que no escala con el modelo. Véase [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

## Principios de diseño

1. **Composable** — Cada habilidad funciona de forma independiente. Usa una o las seis.
2. **Observable** — skill-comply produce tasas de cumplimiento cuantitativas, no evaluaciones subjetivas.
3. **Non-destructive** — Cada habilidad propone cambios y espera confirmación. Nada se aplica de forma automática.
4. **Tool-agnostic in concept** — Diseñado para Claude Code, pero la arquitectura aplica a cualquier agente con configuración persistente.
5. **Evaluation scales with model capability** — Los modelos pequeños se benefician de la puntuación basada en rúbrica; los modelos de razonamiento (clase Opus) evalúan con contexto completo y juicio cualitativo. AKC no prescribe un único enfoque — adapta la profundidad de la evaluación a la capacidad de razonamiento del modelo.
6. **Scaffold dissolution** — Las habilidades son andamios. A medida que el usuario y el agente interiorizan el ciclo, las habilidades se vuelven innecesarias y solo las reglas sostienen el bucle. Véase [docs/scaffold-dissolution.md](docs/scaffold-dissolution.md).
7. **Code-LLM Layering** — El código se encarga del determinismo, la auditabilidad y el flujo de control. El LLM se encarga del significado. Estructúralos en capas de manera explícita; nunca dejes que el LLM mantenga estado duradero o decida la condición de terminación. Véase [ADR-0008](docs/adr/0008-code-and-llm-collaboration.md).
8. **Human cognitive resource is the bottleneck** — A medida que crece la capacidad del agente, el recurso escaso ya no es cómputo ni contexto, sino la atención y el juicio humanos. Cada fase está moldeada para proteger ese presupuesto: ingesta signal-first en Research, promoción de reglas para no rehacer la misma decisión, medición de cumplimiento para que el humano no reaudite manualmente, y diálogo adelantado porque una implementación desalineada cuesta más que la conversación que la habría evitado. Véase [ADR-0010](docs/adr/0010-human-cognitive-resource-as-central-constraint.md).

## Relación con la Harness Engineering

AKC comparte terreno común con la [harness engineering](https://mitchellh.com/writing/my-ai-adoption-journey) (Mitchell Hashimoto, 2025) — la práctica de ingeniar soluciones para que un agente nunca repita el mismo error, combinando prompts mejorados (por ejemplo, actualizaciones de AGENTS.md) y herramientas programáticas (scripts, comandos de verificación). Ambas buscan hacer a los agentes más fiables. Difieren en aquello en lo que se enfocan.

| Capa | Pregunta | Atendida por |
|------|----------|--------------|
| Harness | «¿Es correcta esta salida?» | Linters, pruebas y scripts individuales |
| AKC | «¿Siguen siendo válidos los propios harnesses?» | skill-comply, skill-stocktake, context-sync |

**Corrección vs alineamiento de intención.** La harness engineering se enfoca en obtener el resultado correcto a la primera — prevenir errores conocidos mediante mejores instrucciones y comprobaciones automatizadas. AKC se preocupa más por otra pregunta: «¿está esto alineado con la intención del dueño?» Un agente puede evitar todos los errores conocidos y, aun así, divergir de la intención de diseño. El Principio de diseño #3 (Non-destructive) refleja esto — propón y luego espera confirmación, porque alinear la intención es difícil de automatizar por completo.

**Reactivo vs proactivo.** La harness engineering es reactiva por naturaleza — cada error dispara un nuevo harness. skill-comply y skill-stocktake de AKC adoptan una postura proactiva, auditando periódicamente si las habilidades y reglas se siguen realmente y si siguen siendo relevantes. El Principio de diseño #5 escala esa evaluación según la capacidad del modelo — rúbricas para modelos pequeños, juicio holístico para modelos de frontera.

## Personalización

Las implementaciones de referencia enlazadas arriba son puntos de partida. Haz fork, reescríbelas, adáptalas a tu agente y a tu flujo de trabajo. AKC define el ciclo — no la implementación. Lo que importa es que las fases (extract → curate → promote → measure → maintain) formen un bucle cerrado, no cómo se construye cada fase.

## Origen

Esta arquitectura fue propuesta e implementada por primera vez por Tatsuya Shimomoto ([@shimo4228](https://github.com/shimo4228)) en febrero de 2026.

Las primeras cinco habilidades fueron contribuidas a [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) entre febrero y marzo de 2026. context-sync se desarrolló de forma independiente.

## Cómo citar

Si usas o referencias la arquitectura Agent Knowledge Cycle, por favor cita:

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

O en el texto:

> Shimomoto, T. (2026). Agent Knowledge Cycle (AKC). doi:10.5281/zenodo.19200727

## Trabajos relacionados

- [Contemplative Agent](https://github.com/shimo4228/contemplative-agent) —
  Un repositorio de investigación independiente que explora Contemplative Constitutional AI
  sobre un modelo local de 9B. Su sustrato de ingeniería (memoria de tres
  capas, destilación en dos etapas) fue el trabajo previo que sembró
  los ADRs de AKC. Véase [`docs/inspiration.md`](docs/inspiration.md) para más detalles.
- [Artículos en Zenn](https://zenn.dev/shimo4228) — Diario de desarrollo (en japonés)
- [Artículos en Dev.to](https://dev.to/shimo4228) — Traducciones al inglés

## Agradecimientos

AKC se apoya en la base de [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code)
de [@affaan-m](https://github.com/affaan-m). ECC era el harness de
base que yo usaba todos los días, y sus habilidades y reglas me
dieron un punto de partida rico sobre el cual construir. A lo largo
de meses de uso diario añadí mis propias habilidades y reglas sobre
ECC, y proliferaron más rápido de lo que yo podía seguir — las
habilidades se volvían obsoletas, las reglas empezaban a contradecirse,
la documentación se alejaba del código. Tenía que auditar el desorden
constantemente y decidir qué conservar, qué fusionar y qué promover a
una regla duradera. El ciclo de seis fases es lo que ese trabajo
recurrente de mantenimiento parecía una vez que noté su forma.

Sin ECC como suelo donde apoyarse, AKC no existiría. Un profundo agradecimiento a affaan-m y a cada contribuidor(a) de ECC.

## References

AKC se construyó desde la práctica, no desde la teoría. Las obras
siguientes no fueron consultadas durante el proceso descrito arriba,
pero el ciclo resultante parece compartir algo con las ideas que
contienen. Las listamos aquí para lectores que puedan encontrar
interesante esa resonancia.

- [Mind in Life](https://www.hup.harvard.edu/books/9780674057517) (Evan Thompson, 2007) —
  El bucle bidireccional entre humano y agente tiene algo en común
  con la idea enactivista de acoplamiento estructural.
- [A Beautiful Loop: An Active Inference Theory of Consciousness](https://www.sciencedirect.com/science/article/pii/S0149763425002970)
  (Laukkonen, Friston, & Chandaria, 2025) — La forma en que el humano actualiza
  reglas y habilidades observando lo que el agente realmente hace
  recuerda vagamente a un bucle de auto-modelado recursivo.

## License

MIT
