---
entity_id: "protein.P10346"
entity_type: "protein"
name: "glnQ"
source_database: "UniProt"
source_id: "P10346"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glnQ b0809 JW0794"
---

# glnQ

`protein.P10346`

## Static

- Type: `protein`
- Source: `UniProt:P10346`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Peripheral membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Part of the binding-protein-dependent transport system for glutamine. Probably responsible for energy coupling to the transport system. GlnQ is the predicted ATP binding subunit of an L-glutamine ABC transporter complex; GlnQ contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Component of L-glutamine ABC transporter (complex.ecocyc.ABC-12-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the binding-protein-dependent transport system for glutamine. Probably responsible for energy coupling to the transport system.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-12-CPLX|complex.ecocyc.ABC-12-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0809|gene.b0809]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P10346`
- `KEGG:ecj:JW0794;eco:b0809;ecoc:C3026_05095;`
- `GeneID:945435;`
- `GO:GO:0005524; GO:0005886; GO:0006868; GO:0015186; GO:0015424; GO:0016020; GO:0016887; GO:0042626; GO:0055052; GO:1903803`

## Notes

Glutamine transport ATP-binding protein GlnQ
