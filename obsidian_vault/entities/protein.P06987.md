---
entity_id: "protein.P06987"
entity_type: "protein"
name: "hisB"
source_database: "UniProt"
source_id: "P06987"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01022}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hisB b2022 JW2004"
---

# hisB

`protein.P06987`

## Static

- Type: `protein`
- Source: `UniProt:P06987`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01022}.

## Enriched Summary

Histidine biosynthesis bifunctional protein HisB [Includes: Histidinol-phosphatase (EC 3.1.3.15); Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19)]

## Biological Role

Catalyzes D-erythro-1-(imidazol-4-yl)glycerol 3-phosphate hydro-lyase (reaction.R03457). Component of imidazoleglycerol-phosphate dehydratase / histidinol-phosphatase (complex.ecocyc.IMIDHISTID-CPLX).

## Enriched Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

Histidine biosynthesis bifunctional protein HisB [Includes: Histidinol-phosphatase (EC 3.1.3.15); Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19)]

## Pathways

- `eco00340` Histidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03457|reaction.R03457]] `KEGG` `database` - via EC:4.2.1.19
- `is_component_of` --> [[complex.ecocyc.IMIDHISTID-CPLX|complex.ecocyc.IMIDHISTID-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2022|gene.b2022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06987`
- `KEGG:ecj:JW2004;eco:b2022;ecoc:C3026_11400;`
- `GeneID:946552;`
- `GO:GO:0000105; GO:0004401; GO:0004424; GO:0005737; GO:0042802; GO:0046872`
- `EC:3.1.3.15; 4.2.1.19`

## Notes

Histidine biosynthesis bifunctional protein HisB [Includes: Histidinol-phosphatase (EC 3.1.3.15); Imidazoleglycerol-phosphate dehydratase (IGPD) (EC 4.2.1.19)]
