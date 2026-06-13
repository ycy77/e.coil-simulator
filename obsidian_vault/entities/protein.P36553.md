---
entity_id: "protein.P36553"
entity_type: "protein"
name: "hemF"
source_database: "UniProt"
source_id: "P36553"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemF b2436 JW2429"
---

# hemF

`protein.P36553`

## Static

- Type: `protein`
- Source: `UniProt:P36553`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Involved in the heme biosynthesis. Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX. {ECO:0000255|HAMAP-Rule:MF_00333, ECO:0000269|PubMed:12975365, ECO:0000269|PubMed:13129604}.

## Biological Role

Component of coproporphyrinogen III oxidase (complex.ecocyc.CPLX0-7808).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the heme biosynthesis. Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX. {ECO:0000255|HAMAP-Rule:MF_00333, ECO:0000269|PubMed:12975365, ECO:0000269|PubMed:13129604}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7808|complex.ecocyc.CPLX0-7808]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2436|gene.b2436]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36553`
- `KEGG:ecj:JW2429;eco:b2436;ecoc:C3026_13530;`
- `GeneID:946908;`
- `GO:GO:0004109; GO:0005737; GO:0006782; GO:0006783; GO:0019353; GO:0030145; GO:0033194; GO:0042803; GO:0046906`
- `EC:1.3.3.3`

## Notes

Oxygen-dependent coproporphyrinogen-III oxidase (CPO) (Coprogen oxidase) (Coproporphyrinogenase) (EC 1.3.3.3)
