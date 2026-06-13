---
entity_id: "protein.P29012"
entity_type: "protein"
name: "dadX"
source_database: "UniProt"
source_id: "P29012"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dadX alnB dadB b1190 JW1179"
---

# dadX

`protein.P29012`

## Static

- Type: `protein`
- Source: `UniProt:P29012`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Isomerizes L-alanine to D-alanine which is then oxidized to pyruvate by DadA. {ECO:0000250}.

## Biological Role

Catalyzes alanine racemase (reaction.R00401). Component of alanine racemase 2 (complex.ecocyc.CPLX0-7465).

## Enriched Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Annotation

FUNCTION: Isomerizes L-alanine to D-alanine which is then oxidized to pyruvate by DadA. {ECO:0000250}.

## Pathways

- `eco00470` D-Amino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01502` Vancomycin resistance (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00401|reaction.R00401]] `KEGG` `database` - via EC:5.1.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7465|complex.ecocyc.CPLX0-7465]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1190|gene.b1190]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P29012`
- `KEGG:ecj:JW1179;eco:b1190;ecoc:C3026_07005;`
- `GeneID:945754;`
- `GO:GO:0005829; GO:0008784; GO:0019480; GO:0030170; GO:0030632; GO:0042803`
- `EC:5.1.1.1`

## Notes

Alanine racemase, catabolic (EC 5.1.1.1)
