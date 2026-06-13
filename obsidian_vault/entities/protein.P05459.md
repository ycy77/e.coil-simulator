---
entity_id: "protein.P05459"
entity_type: "protein"
name: "pdxB"
source_database: "UniProt"
source_id: "P05459"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01825}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxB b2320 JW2317"
---

# pdxB

`protein.P05459`

## Static

- Type: `protein`
- Source: `UniProt:P05459`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01825}.

## Enriched Summary

FUNCTION: Catalyzes the oxidation of erythronate-4-phosphate to 3-hydroxy-2-oxo-4-phosphonooxybutanoate. {ECO:0000255|HAMAP-Rule:MF_01825}.

## Biological Role

Component of erythronate-4-phosphate dehydrogenase (complex.ecocyc.CPLX0-8212).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of erythronate-4-phosphate to 3-hydroxy-2-oxo-4-phosphonooxybutanoate. {ECO:0000255|HAMAP-Rule:MF_01825}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8212|complex.ecocyc.CPLX0-8212]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2320|gene.b2320]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05459`
- `KEGG:ecj:JW2317;eco:b2320;ecoc:C3026_12930;`
- `GeneID:946785;`
- `GO:GO:0005829; GO:0008615; GO:0033711; GO:0036001; GO:0042803; GO:0051287`
- `EC:1.1.1.290`

## Notes

Erythronate-4-phosphate dehydrogenase (EC 1.1.1.290)
