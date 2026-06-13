---
entity_id: "protein.P0A7D7"
entity_type: "protein"
name: "purC"
source_database: "UniProt"
source_id: "P0A7D7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purC b2476 JW2461"
---

# purC

`protein.P0A7D7`

## Static

- Type: `protein`
- Source: `UniProt:P0A7D7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 4-carboxy-5-aminoimidazole ribonucleotide (CAIR) to 4-(N-succinylcarboxamide)-5-aminoimidazole ribonucleotide (SAICAR). {ECO:0000269|PubMed:1534690}.

## Biological Role

Component of phosphoribosylaminoimidazole-succinocarboxamide synthase (complex.ecocyc.SAICARSYN-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Converts 4-carboxy-5-aminoimidazole ribonucleotide (CAIR) to 4-(N-succinylcarboxamide)-5-aminoimidazole ribonucleotide (SAICAR). {ECO:0000269|PubMed:1534690}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SAICARSYN-CPLX|complex.ecocyc.SAICARSYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b2476|gene.b2476]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7D7`
- `KEGG:ecj:JW2461;eco:b2476;ecoc:C3026_13740;`
- `GeneID:86860609;89517285;946957;`
- `GO:GO:0004639; GO:0005524; GO:0005829; GO:0006189; GO:0009236; GO:0016020; GO:0097216`
- `EC:6.3.2.6`

## Notes

Phosphoribosylaminoimidazole-succinocarboxamide synthase (EC 6.3.2.6) (SAICAR synthetase)
