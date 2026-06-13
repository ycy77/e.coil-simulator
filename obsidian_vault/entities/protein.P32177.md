---
entity_id: "protein.P32177"
entity_type: "protein"
name: "fdhD"
source_database: "UniProt"
source_id: "P32177"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00187, ECO:0000269|PubMed:2170340}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fdhD b3895 JW3866"
---

# fdhD

`protein.P32177`

## Static

- Type: `protein`
- Source: `UniProt:P32177`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00187, ECO:0000269|PubMed:2170340}.

## Enriched Summary

FUNCTION: Required for formate dehydrogenase (FDH) activity (PubMed:22194618, PubMed:25649206, PubMed:3077634, PubMed:8522521). Acts as a sulfur carrier protein that transfers sulfur from IscS to the molybdenum cofactor prior to its insertion into FDH. Specifically interacts with IscS and stimulates its cysteine desulfurase activity. Also binds the molybdenum cofactor (PubMed:22194618, PubMed:25649206). Required for activity of formate dehydrogenase N (FDH-N), formate dehydrogenase O (FDH-O) and formate dehydrogenase H (FDH-H) (PubMed:22194618, PubMed:3077634, PubMed:8522521). {ECO:0000269|PubMed:22194618, ECO:0000269|PubMed:25649206, ECO:0000269|PubMed:3077634, ECO:0000269|PubMed:8522521}.

## Biological Role

Component of sulfurtransferase for molybdenum cofactor sulfuration (complex.ecocyc.CPLX0-8175).

## Annotation

FUNCTION: Required for formate dehydrogenase (FDH) activity (PubMed:22194618, PubMed:25649206, PubMed:3077634, PubMed:8522521). Acts as a sulfur carrier protein that transfers sulfur from IscS to the molybdenum cofactor prior to its insertion into FDH. Specifically interacts with IscS and stimulates its cysteine desulfurase activity. Also binds the molybdenum cofactor (PubMed:22194618, PubMed:25649206). Required for activity of formate dehydrogenase N (FDH-N), formate dehydrogenase O (FDH-O) and formate dehydrogenase H (FDH-H) (PubMed:22194618, PubMed:3077634, PubMed:8522521). {ECO:0000269|PubMed:22194618, ECO:0000269|PubMed:25649206, ECO:0000269|PubMed:3077634, ECO:0000269|PubMed:8522521}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8175|complex.ecocyc.CPLX0-8175]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3895|gene.b3895]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32177`
- `KEGG:ecj:JW3866;eco:b3895;ecoc:C3026_21060;`
- `GeneID:93778043;948393;`
- `GO:GO:0005829; GO:0006777; GO:0016783; GO:0042803; GO:0043546; GO:0097163`

## Notes

Sulfur carrier protein FdhD (Sulfurtransferase FdhD)
