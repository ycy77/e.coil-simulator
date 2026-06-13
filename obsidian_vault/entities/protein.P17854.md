---
entity_id: "protein.P17854"
entity_type: "protein"
name: "cysH"
source_database: "UniProt"
source_id: "P17854"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00063, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysH b2762 JW2732"
---

# cysH

`protein.P17854`

## Static

- Type: `protein`
- Source: `UniProt:P17854`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00063, ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the formation of sulfite from phosphoadenosine 5'-phosphosulfate (PAPS) using thioredoxin as an electron donor. {ECO:0000255|HAMAP-Rule:MF_00063, ECO:0000269|PubMed:7588765}.

## Biological Role

Component of phosphoadenosine phosphosulfate reductase (complex.ecocyc.PAPSSULFOTRANS-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of sulfite from phosphoadenosine 5'-phosphosulfate (PAPS) using thioredoxin as an electron donor. {ECO:0000255|HAMAP-Rule:MF_00063, ECO:0000269|PubMed:7588765}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.PAPSSULFOTRANS-CPLX|complex.ecocyc.PAPSSULFOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2762|gene.b2762]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17854`
- `KEGG:ecj:JW2732;eco:b2762;ecoc:C3026_15180;`
- `GeneID:75058622;947230;`
- `GO:GO:0004604; GO:0005737; GO:0006790; GO:0019379; GO:0070814`
- `EC:1.8.4.8`

## Notes

Phosphoadenosine 5'-phosphosulfate reductase (PAPS reductase) (EC 1.8.4.8) (3'-phosphoadenylylsulfate reductase) (PAPS reductase, thioredoxin dependent) (PAPS sulfotransferase) (PAdoPS reductase)
