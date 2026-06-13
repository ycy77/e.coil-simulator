---
entity_id: "protein.P77434"
entity_type: "protein"
name: "alaC"
source_database: "UniProt"
source_id: "P77434"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alaC yfdZ b2379 JW2376"
---

# alaC

`protein.P77434`

## Static

- Type: `protein`
- Source: `UniProt:P77434`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of alanine (PubMed:20729367). Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction (PubMed:20729367). {ECO:0000269|PubMed:20729367, ECO:0000269|PubMed:21597182}.

## Biological Role

Component of glutamate—pyruvate aminotransferase AlaC (complex.ecocyc.CPLX0-7887).

## Annotation

FUNCTION: Involved in the biosynthesis of alanine (PubMed:20729367). Catalyzes the transamination of pyruvate by glutamate, leading to the formation of L-alanine and 2-oxoglutarate. Is also able to catalyze the reverse reaction (PubMed:20729367). {ECO:0000269|PubMed:20729367, ECO:0000269|PubMed:21597182}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7887|complex.ecocyc.CPLX0-7887]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2379|gene.b2379]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77434`
- `KEGG:ecj:JW2376;eco:b2379;ecoc:C3026_13230;`
- `GeneID:75172498;75202552;946850;`
- `GO:GO:0004021; GO:0005737; GO:0006523; GO:0008483; GO:0019272; GO:0030170; GO:0030632; GO:0042803`
- `EC:2.6.1.2`

## Notes

Glutamate-pyruvate aminotransferase AlaC (EC 2.6.1.2)
