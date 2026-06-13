---
entity_id: "protein.P07017"
entity_type: "protein"
name: "tar"
source_database: "UniProt"
source_id: "P07017"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tar cheM b1886 JW1875"
---

# tar

`protein.P07017`

## Static

- Type: `protein`
- Source: `UniProt:P07017`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles.

## Enriched Summary

FUNCTION: Receptor for the attractant L-aspartate and related amino and dicarboxylic acids. Tar also mediates taxis to the attractant maltose via an interaction with the periplasmic maltose binding protein. Tar mediates taxis away from the repellents cobalt and nickel.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Biological Role

Component of methyl-accepting chemotaxis protein Tar (complex.ecocyc.CPLX0-8102), chemotaxis signaling complex core unit - aspartate sensing (complex.ecocyc.TAR-CPLX), Targln (protein.ecocyc.TAR-GLN), Targlu (protein.ecocyc.TAR-GLU), Targlu-Me (protein.ecocyc.TAR-GLUME).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Receptor for the attractant L-aspartate and related amino and dicarboxylic acids. Tar also mediates taxis to the attractant maltose via an interaction with the periplasmic maltose binding protein. Tar mediates taxis away from the repellents cobalt and nickel.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8102|complex.ecocyc.CPLX0-8102]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TAR-CPLX|complex.ecocyc.TAR-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAR-GLN|protein.ecocyc.TAR-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAR-GLU|protein.ecocyc.TAR-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TAR-GLUME|protein.ecocyc.TAR-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1886|gene.b1886]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07017`
- `KEGG:ecj:JW1875;eco:b1886;ecoc:C3026_10725;`
- `GeneID:946399;`
- `GO:GO:0004888; GO:0005886; GO:0006935; GO:0009593; GO:0035556; GO:0042802; GO:0042803; GO:0043424; GO:0051260; GO:0051286; GO:0071230; GO:0098561`

## Notes

Methyl-accepting chemotaxis protein II (MCP-II) (Aspartate chemoreceptor protein)
