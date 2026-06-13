---
entity_id: "protein.P0AG18"
entity_type: "protein"
name: "purE"
source_database: "UniProt"
source_id: "P0AG18"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purE b0523 JW0512"
---

# purE

`protein.P0AG18`

## Static

- Type: `protein`
- Source: `UniProt:P0AG18`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) to 4-carboxy-5-aminoimidazole ribonucleotide (CAIR). {ECO:0000255|HAMAP-Rule:MF_01929, ECO:0000269|PubMed:8117684}.

## Biological Role

Component of N5-carboxyaminoimidazole ribonucleotide mutase (complex.ecocyc.PURE-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) to 4-carboxy-5-aminoimidazole ribonucleotide (CAIR). {ECO:0000255|HAMAP-Rule:MF_01929, ECO:0000269|PubMed:8117684}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PURE-CPLX|complex.ecocyc.PURE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b0523|gene.b0523]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG18`
- `KEGG:ecj:JW0512;eco:b0523;ecoc:C3026_02565;`
- `GeneID:86863072;86945437;949031;`
- `GO:GO:0005829; GO:0006189; GO:0034023; GO:0042802`
- `EC:5.4.99.18`

## Notes

N5-carboxyaminoimidazole ribonucleotide mutase (N5-CAIR mutase) (EC 5.4.99.18) (5-(carboxyamino)imidazole ribonucleotide mutase)
