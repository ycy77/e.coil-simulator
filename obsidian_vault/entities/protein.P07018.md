---
entity_id: "protein.P07018"
entity_type: "protein"
name: "tap"
source_database: "UniProt"
source_id: "P07018"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tap b1885 JW1874"
---

# tap

`protein.P07018`

## Static

- Type: `protein`
- Source: `UniProt:P07018`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles.

## Enriched Summary

FUNCTION: Mediates taxis toward dipeptides via an interaction with the periplasmic dipeptide-binding protein.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Biological Role

Component of methyl-accepting chemotaxis protein - dipeptide-sensing (complex.ecocyc.CPLX0-8104), chemotaxis signaling complex core unit - dipeptide sensing (complex.ecocyc.TAP-CPLX), Tapgln (protein.ecocyc.TAP-GLN), Tapglu (protein.ecocyc.TAP-GLU), Tapglu-Me (protein.ecocyc.TAP-GLUME).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Mediates taxis toward dipeptides via an interaction with the periplasmic dipeptide-binding protein.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8104|complex.ecocyc.CPLX0-8104]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TAP-CPLX|complex.ecocyc.TAP-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAP-GLN|protein.ecocyc.TAP-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAP-GLU|protein.ecocyc.TAP-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAP-GLUME|protein.ecocyc.TAP-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1885|gene.b1885]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07018`
- `KEGG:ecj:JW1874;eco:b1885;ecoc:C3026_10720;`
- `GeneID:946397;`
- `GO:GO:0004888; GO:0005886; GO:0006935; GO:0007165`

## Notes

Methyl-accepting chemotaxis protein IV (MCP-IV) (Dipeptide chemoreceptor protein)
