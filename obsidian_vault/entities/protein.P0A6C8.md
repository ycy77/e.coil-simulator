---
entity_id: "protein.P0A6C8"
entity_type: "protein"
name: "argB"
source_database: "UniProt"
source_id: "P0A6C8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00082}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argB b3959 JW5553"
---

# argB

`protein.P0A6C8`

## Static

- Type: `protein`
- Source: `UniProt:P0A6C8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00082}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent phosphorylation of N-acetyl-L-glutamate. {ECO:0000255|HAMAP-Rule:MF_00082, ECO:0000269|PubMed:10393305, ECO:0000269|PubMed:14623187}.

## Biological Role

Component of acetylglutamate kinase (complex.ecocyc.ACETYLGLUTKIN-CPLX).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent phosphorylation of N-acetyl-L-glutamate. {ECO:0000255|HAMAP-Rule:MF_00082, ECO:0000269|PubMed:10393305, ECO:0000269|PubMed:14623187}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ACETYLGLUTKIN-CPLX|complex.ecocyc.ACETYLGLUTKIN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3959|gene.b3959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6C8`
- `KEGG:ecj:JW5553;eco:b3959;`
- `GeneID:75169403;75203211;948464;`
- `GO:GO:0003991; GO:0005524; GO:0005737; GO:0006526; GO:0006974; GO:0042450`
- `EC:2.7.2.8`

## Notes

Acetylglutamate kinase (EC 2.7.2.8) (N-acetyl-L-glutamate 5-phosphotransferase) (NAG kinase) (NAGK)
