---
entity_id: "protein.P0AED7"
entity_type: "protein"
name: "dapE"
source_database: "UniProt"
source_id: "P0AED7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dapE msgB b2472 JW2456"
---

# dapE

`protein.P0AED7`

## Static

- Type: `protein`
- Source: `UniProt:P0AED7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of N-succinyl-L,L-diaminopimelic acid (SDAP), forming succinate and LL-2,6-diaminopimelate (DAP), an intermediate involved in the bacterial biosynthesis of lysine and meso-diaminopimelic acid, an essential component of bacterial cell walls. {ECO:0000269|PubMed:3276674}.

## Biological Role

Component of succinyl-diaminopimelate desuccinylase (complex.ecocyc.CPLX0-3161).

## Enriched Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of N-succinyl-L,L-diaminopimelic acid (SDAP), forming succinate and LL-2,6-diaminopimelate (DAP), an intermediate involved in the bacterial biosynthesis of lysine and meso-diaminopimelic acid, an essential component of bacterial cell walls. {ECO:0000269|PubMed:3276674}.

## Pathways

- `eco00300` Lysine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3161|complex.ecocyc.CPLX0-3161]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2472|gene.b2472]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AED7`
- `KEGG:ecj:JW2456;eco:b2472;ecoc:C3026_13715;`
- `GeneID:948313;`
- `GO:GO:0005829; GO:0008270; GO:0009014; GO:0009089; GO:0019877; GO:0032153; GO:0042802; GO:0043093; GO:0050897`
- `EC:3.5.1.18`

## Notes

Succinyl-diaminopimelate desuccinylase (SDAP desuccinylase) (EC 3.5.1.18) (N-succinyl-LL-2,6-diaminoheptanedioate amidohydrolase)
