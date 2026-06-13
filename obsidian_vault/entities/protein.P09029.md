---
entity_id: "protein.P09029"
entity_type: "protein"
name: "purK"
source_database: "UniProt"
source_id: "P09029"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purK b0522 JW0511"
---

# purK

`protein.P09029`

## Static

- Type: `protein`
- Source: `UniProt:P09029`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent conversion of 5-aminoimidazole ribonucleotide (AIR) and HCO(3)(-) to N5-carboxyaminoimidazole ribonucleotide (N5-CAIR). {ECO:0000255|HAMAP-Rule:MF_01928, ECO:0000269|PubMed:8117684}.

## Biological Role

Component of 5-(carboxyamino)imidazole ribonucleotide synthase (complex.ecocyc.PURK-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the ATP-dependent conversion of 5-aminoimidazole ribonucleotide (AIR) and HCO(3)(-) to N5-carboxyaminoimidazole ribonucleotide (N5-CAIR). {ECO:0000255|HAMAP-Rule:MF_01928, ECO:0000269|PubMed:8117684}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PURK-CPLX|complex.ecocyc.PURK-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0522|gene.b0522]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09029`
- `KEGG:ecj:JW0511;eco:b0522;ecoc:C3026_02560;`
- `GeneID:945153;`
- `GO:GO:0004638; GO:0005524; GO:0005829; GO:0006189; GO:0034028; GO:0046872`
- `EC:6.3.4.18`

## Notes

N5-carboxyaminoimidazole ribonucleotide synthase (N5-CAIR synthase) (EC 6.3.4.18) (5-(carboxyamino)imidazole ribonucleotide synthetase)
