---
entity_id: "complex.ecocyc.CPLX0-7811"
entity_type: "complex"
name: "protoporphyrinogen oxidase"
source_database: "EcoCyc"
source_id: "CPLX0-7811"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# protoporphyrinogen oxidase

`complex.ecocyc.CPLX0-7811`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7811`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ACB4|protein.P0ACB4]]

## Enriched Summary

Protoporphyrinogen oxidase (HemG) catalyzes the six-electron oxidation of protoporphyrinogen IX to protoporphyrin IX. The enzyme belongs to the long chain flavodoxin family of proteins; the insert loop which distinguishes it from other flavodoxins may be responsible for HemG activity . Early experiments showed that protoporphyrinogen oxidase is associated with the membrane fraction and inactivated by treatment with detergent, suggesting that the enzyme requires an intact electron transport system for activity . Under anaerobic conditions, the reaction can be coupled to nitrate or fumarate reduction via menaquinone within the anaerobic electron transport chain . In vitro, the purified enzyme can use menadione as the electron acceptor . Under aerobic conditions, the electron acceptor for the protoporphyrinogen oxidase reaction was initially thought to be molecular oxygen . It was later shown that the aerobic reaction is also coupled to the electron transport chain. Potential electron transport chains for both aerobic and anaerobic HemG protoporphyrinogen oxidase activity were reconstituted in vitro from purified components; both ubiquinone and menaquinone functioned as electron acceptors during HemG catalysis. Fumarate reductase, nitrate reductase, cytochrome bd and cytochrome bo were shown to function as electron acceptors. In vivo experiments using E...

## Biological Role

Catalyzes RXN-21483 (reaction.ecocyc.RXN-21483), RXN0-6259 (reaction.ecocyc.RXN0-6259). Bound by FMN (molecule.C00061).

## Annotation

Protoporphyrinogen oxidase (HemG) catalyzes the six-electron oxidation of protoporphyrinogen IX to protoporphyrin IX. The enzyme belongs to the long chain flavodoxin family of proteins; the insert loop which distinguishes it from other flavodoxins may be responsible for HemG activity . Early experiments showed that protoporphyrinogen oxidase is associated with the membrane fraction and inactivated by treatment with detergent, suggesting that the enzyme requires an intact electron transport system for activity . Under anaerobic conditions, the reaction can be coupled to nitrate or fumarate reduction via menaquinone within the anaerobic electron transport chain . In vitro, the purified enzyme can use menadione as the electron acceptor . Under aerobic conditions, the electron acceptor for the protoporphyrinogen oxidase reaction was initially thought to be molecular oxygen . It was later shown that the aerobic reaction is also coupled to the electron transport chain. Potential electron transport chains for both aerobic and anaerobic HemG protoporphyrinogen oxidase activity were reconstituted in vitro from purified components; both ubiquinone and menaquinone functioned as electron acceptors during HemG catalysis. Fumarate reductase, nitrate reductase, cytochrome bd and cytochrome bo were shown to function as electron acceptors. In vivo experiments using E. coli respiratory chain mutant strains confirmed the in vitro results. These data showed that HemG catalysis and overall heme biosynthesis is dependent upon respiratory electron transport. A model for respiratory chain-driven protoporphyrinogen oxidase was proposed . The presence of a flavodoxin motif in the sequence indicates that the enzyme may utilize FMN as a cofactor . A probable FMN cofactor was detected by MALDI-TOF,

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-21483|reaction.ecocyc.RXN-21483]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6259|reaction.ecocyc.RXN0-6259]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ACB4|protein.P0ACB4]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7811`
- `QSPROTEOME:QS00049441`

## Notes

4*protein.P0ACB4
