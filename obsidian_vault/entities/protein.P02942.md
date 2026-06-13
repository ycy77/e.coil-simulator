---
entity_id: "protein.P02942"
entity_type: "protein"
name: "tsr"
source_database: "UniProt"
source_id: "P02942"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tsr cheD b4355 JW4318"
---

# tsr

`protein.P02942`

## Static

- Type: `protein`
- Source: `UniProt:P02942`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles.

## Enriched Summary

FUNCTION: Receptor for the attractant L-serine and related amino acids. Is also responsible for chemotaxis away from a wide range of repellents, including leucine, indole, and weak acids.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Biological Role

Component of methyl-accepting chemotaxis protein - serine-sensing (complex.ecocyc.CPLX0-8103), chemotaxis signaling complex core unit - serine sensing (complex.ecocyc.TSR-CPLX), Tsrgln (protein.ecocyc.TSR-GLN), Tsrglu (protein.ecocyc.TSR-GLU), Tsrglu-Me (protein.ecocyc.TSR-GLUME).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Receptor for the attractant L-serine and related amino acids. Is also responsible for chemotaxis away from a wide range of repellents, including leucine, indole, and weak acids.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8103|complex.ecocyc.CPLX0-8103]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TSR-CPLX|complex.ecocyc.TSR-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TSR-GLN|protein.ecocyc.TSR-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TSR-GLU|protein.ecocyc.TSR-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TSR-GLUME|protein.ecocyc.TSR-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b4355|gene.b4355]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02942`
- `KEGG:ecj:JW4318;eco:b4355;ecoc:C3026_23530;`
- `GeneID:948884;`
- `GO:GO:0004888; GO:0005886; GO:0006935; GO:0007165; GO:0009593; GO:0042802; GO:0048870; GO:0071230; GO:0098561; GO:1902021`

## Notes

Methyl-accepting chemotaxis protein I (MCP-I) (Serine chemoreceptor protein)
