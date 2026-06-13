---
entity_id: "protein.P36566"
entity_type: "protein"
name: "cmoM"
source_database: "UniProt"
source_id: "P36566"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmoM smtA ycbD b0921 JW0904"
---

# cmoM

`protein.P36566`

## Static

- Type: `protein`
- Source: `UniProt:P36566`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the methylation of 5-carboxymethoxyuridine (cmo5U) to form 5-methoxycarbonylmethoxyuridine (mcmo5U) at position 34 in tRNAs. Four tRNAs (tRNA(Ala1), tRNA(Ser1), tRNA(Pro3) and tRNA(Thr4)) are fully modified with mcmo5U in stationary-phase E.coli. Also present at low frequency in tRNA(Leu3) and tRNA(Val1). {ECO:0000269|PubMed:26681692}.

## Biological Role

Component of tRNA cmo5U34 methyltransferase (complex.ecocyc.CPLX0-11245).

## Annotation

FUNCTION: Catalyzes the methylation of 5-carboxymethoxyuridine (cmo5U) to form 5-methoxycarbonylmethoxyuridine (mcmo5U) at position 34 in tRNAs. Four tRNAs (tRNA(Ala1), tRNA(Ser1), tRNA(Pro3) and tRNA(Thr4)) are fully modified with mcmo5U in stationary-phase E.coli. Also present at low frequency in tRNA(Leu3) and tRNA(Val1). {ECO:0000269|PubMed:26681692}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11245|complex.ecocyc.CPLX0-11245]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0921|gene.b0921]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36566`
- `KEGG:ecj:JW0904;eco:b0921;ecoc:C3026_05665;`
- `GeneID:93776494;945547;`
- `GO:GO:0002098; GO:0008168; GO:0030488; GO:0097697`
- `EC:2.1.1.-`

## Notes

tRNA 5-carboxymethoxyuridine methyltransferase (EC 2.1.1.-) (cmo5U methyltransferase)
