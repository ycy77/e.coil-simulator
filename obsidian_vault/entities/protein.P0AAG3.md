---
entity_id: "protein.P0AAG3"
entity_type: "protein"
name: "gltL"
source_database: "UniProt"
source_id: "P0AAG3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:9593292}; Peripheral membrane protein {ECO:0000305|PubMed:9593292}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gltL b0652 JW0647"
---

# gltL

`protein.P0AAG3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAG3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:9593292}; Peripheral membrane protein {ECO:0000305|PubMed:9593292}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9593292}. GltL is the predicted ATP binding subunit of a glutamate/aspartate ABC transporter complex; GltL contains signature motifs conserved in ATP-binding cassette (ABC) proteins .

## Biological Role

Component of glutamate / aspartate ABC transporter (complex.ecocyc.ABC-13-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex GltIJKL involved in glutamate and aspartate uptake. Probably responsible for energy coupling to the transport system. {ECO:0000305|PubMed:9593292}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-13-CPLX|complex.ecocyc.ABC-13-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0652|gene.b0652]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAG3`
- `KEGG:ecj:JW0647;eco:b0652;ecoc:C3026_03260;`
- `GeneID:86945534;93776830;945254;`
- `GO:GO:0005524; GO:0005886; GO:0016020; GO:0016887; GO:0042626; GO:0055052; GO:0098712; GO:0102013; GO:0140009`
- `EC:7.4.2.1`

## Notes

Glutamate/aspartate import ATP-binding protein GltL (EC 7.4.2.1)
