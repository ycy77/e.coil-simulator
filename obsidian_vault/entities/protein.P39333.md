---
entity_id: "protein.P39333"
entity_type: "protein"
name: "bdcA"
source_database: "UniProt"
source_id: "P39333"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bdcA yjgI b4249 JW4207"
---

# bdcA

`protein.P39333`

## Static

- Type: `protein`
- Source: `UniProt:P39333`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Increases biofilm dispersal. Acts by binding directly to the signaling molecule cyclic-di-GMP, which decreases the intracellular concentration of cyclic-di-GMP and leads to biofilm dispersal. Also controls other biofilm-related phenotypes such as cell motility, cell size, cell aggregation and production of extracellular DNA and extracellular polysaccharides (EPS). Does not act as a phosphodiesterase. {ECO:0000269|PubMed:21059164}.

## Biological Role

Component of c-di-GMP-binding biofilm dispersal mediator protein (complex.ecocyc.CPLX0-8154).

## Annotation

FUNCTION: Increases biofilm dispersal. Acts by binding directly to the signaling molecule cyclic-di-GMP, which decreases the intracellular concentration of cyclic-di-GMP and leads to biofilm dispersal. Also controls other biofilm-related phenotypes such as cell motility, cell size, cell aggregation and production of extracellular DNA and extracellular polysaccharides (EPS). Does not act as a phosphodiesterase. {ECO:0000269|PubMed:21059164}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8154|complex.ecocyc.CPLX0-8154]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4249|gene.b4249]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39333`
- `KEGG:ecj:JW4207;eco:b4249;ecoc:C3026_22930;`
- `GeneID:948765;`
- `GO:GO:0035438; GO:0042803; GO:0044010; GO:0070402`

## Notes

Cyclic-di-GMP-binding biofilm dispersal mediator protein
