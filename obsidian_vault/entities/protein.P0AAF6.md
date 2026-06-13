---
entity_id: "protein.P0AAF6"
entity_type: "protein"
name: "artP"
source_database: "UniProt"
source_id: "P0AAF6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "artP b0864 JW0848"
---

# artP

`protein.P0AAF6`

## Static

- Type: `protein`
- Source: `UniProt:P0AAF6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Peripheral membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:8801422}. ArtP is predicted to be the ATP-binding subunit of an L- arginine ABC transporter. Sequence analysis indicates that ArtP is highly homologous to the HisP ATP-binding protein of the histine/LAO (lysine/arginine/ornithine) ABC transporter system in Salmonella typhimurium. artP contains a conserved ATP-binding consensus site .

## Biological Role

Component of L-arginine ABC transporter (complex.ecocyc.ABC-4-CPLX), putative ABC transporter ArtPQMI (complex.ecocyc.CPLX0-8120).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:8801422}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.ABC-4-CPLX|complex.ecocyc.ABC-4-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8120|complex.ecocyc.CPLX0-8120]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0864|gene.b0864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAF6`
- `KEGG:ecj:JW0848;eco:b0864;ecoc:C3026_05380;`
- `GeneID:86945751;93776558;945489;`
- `GO:GO:0005524; GO:0005886; GO:0015426; GO:0016020; GO:0016887; GO:0042626; GO:0055052; GO:0097638`
- `EC:7.4.2.1`

## Notes

Arginine transport ATP-binding protein ArtP (EC 7.4.2.1)
