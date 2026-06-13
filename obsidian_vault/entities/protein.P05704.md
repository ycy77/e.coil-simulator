---
entity_id: "protein.P05704"
entity_type: "protein"
name: "trg"
source_database: "UniProt"
source_id: "P05704"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "trg b1421 JW1417"
---

# trg

`protein.P05704`

## Static

- Type: `protein`
- Source: `UniProt:P05704`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22380631}. Note=Found predominantly at cell poles.

## Enriched Summary

FUNCTION: Mediates taxis to the sugars ribose and galactose via an interaction with the periplasmic ribose- or galactose-binding proteins.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Biological Role

Component of methyl-accepting chemotaxis protein Trg - ribose/galactose/glucose-sensing (complex.ecocyc.CPLX0-8105), chemotaxis signaling complex core unit - ribose/galactose/glucose sensing (complex.ecocyc.TRG-CPLX), Trggln (protein.ecocyc.TRG-GLN), Trgglu (protein.ecocyc.TRG-GLU), Trgglu-Me (protein.ecocyc.TRG-GLUME).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Mediates taxis to the sugars ribose and galactose via an interaction with the periplasmic ribose- or galactose-binding proteins.; FUNCTION: Chemotactic-signal transducers respond to changes in the concentration of attractants and repellents in the environment, transduce a signal from the outside to the inside of the cell, and facilitate sensory adaptation through the variation of the level of methylation. Attractants increase the level of methylation while repellents decrease the level of methylation, the methyl groups are added by the methyltransferase CheR and removed by the methylesterase CheB.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8105|complex.ecocyc.CPLX0-8105]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.TRG-CPLX|complex.ecocyc.TRG-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TRG-GLN|protein.ecocyc.TRG-GLN]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TRG-GLU|protein.ecocyc.TRG-GLU]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12
- `is_component_of` --> [[protein.ecocyc.TRG-GLUME|protein.ecocyc.TRG-GLUME]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=12

## Incoming Edges (1)

- `encodes` <-- [[gene.b1421|gene.b1421]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05704`
- `KEGG:ecj:JW1417;eco:b1421;ecoc:C3026_08275;`
- `GeneID:945995;`
- `GO:GO:0004888; GO:0005886; GO:0006935; GO:0007165; GO:0042803; GO:0098561`

## Notes

Methyl-accepting chemotaxis protein III (MCP-III) (Ribose and galactose chemoreceptor protein)
