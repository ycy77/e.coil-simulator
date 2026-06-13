---
entity_id: "protein.P75726"
entity_type: "protein"
name: "citF"
source_database: "UniProt"
source_id: "P75726"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citF ybdV b0615 JW5087"
---

# citF

`protein.P75726`

## Static

- Type: `protein`
- Source: `UniProt:P75726`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Represents a citrate:acetyl-ACP transferase. {ECO:0000250}.

## Biological Role

Catalyzes acetyl-CoA:citrate CoA-transferase (reaction.R01323). Component of citrate lyase (complex.ecocyc.ACECITLY-CPLX), citrate lyase, inactive (complex.ecocyc.CITLY-CPLX), citrate lyase, citrate-acyl carrier protein transferase component (complex.ecocyc.CITTRANS-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Represents a citrate:acetyl-ACP transferase. {ECO:0000250}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R01323|reaction.R01323]] `KEGG` `database` - via EC:2.8.3.10
- `is_component_of` --> [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CITTRANS-CPLX|complex.ecocyc.CITTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0615|gene.b0615]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75726`
- `KEGG:ecj:JW5087;eco:b0615;ecoc:C3026_03075;`
- `GeneID:945230;`
- `GO:GO:0005737; GO:0006084; GO:0006101; GO:0008814; GO:0008815; GO:0009346`
- `EC:2.8.3.10; 4.1.3.6`

## Notes

Citrate lyase alpha chain (Citrase alpha chain) (EC 4.1.3.6) (Citrate (pro-3S)-lyase alpha chain) (Citrate CoA-transferase subunit) (EC 2.8.3.10)
