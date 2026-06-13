---
entity_id: "protein.P0A6B4"
entity_type: "protein"
name: "alr"
source_database: "UniProt"
source_id: "P0A6B4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "alr b4053 JW4013"
---

# alr

`protein.P0A6B4`

## Static

- Type: `protein`
- Source: `UniProt:P0A6B4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the interconversion of L-alanine and D-alanine. Provides the D-alanine required for cell wall biosynthesis. {ECO:0000269|PubMed:18434499}.

## Biological Role

Catalyzes alanine racemase (reaction.R00401). Component of alanine racemase 1 (complex.ecocyc.CPLX0-8202).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Catalyzes the interconversion of L-alanine and D-alanine. Provides the D-alanine required for cell wall biosynthesis. {ECO:0000269|PubMed:18434499}.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00401|reaction.R00401]] `KEGG` `database` - via EC:5.1.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8202|complex.ecocyc.CPLX0-8202]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4053|gene.b4053]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6B4`
- `KEGG:ecj:JW4013;eco:b4053;ecoc:C3026_21900;`
- `GeneID:75204196;948564;`
- `GO:GO:0005829; GO:0008360; GO:0008784; GO:0009252; GO:0030170; GO:0030632; GO:0042803; GO:0071555`
- `EC:5.1.1.1`

## Notes

Alanine racemase, biosynthetic (EC 5.1.1.1)
