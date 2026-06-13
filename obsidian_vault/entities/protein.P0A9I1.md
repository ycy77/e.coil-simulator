---
entity_id: "protein.P0A9I1"
entity_type: "protein"
name: "citE"
source_database: "UniProt"
source_id: "P0A9I1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citE ybdW b0616 JW0608"
---

# citE

`protein.P0A9I1`

## Static

- Type: `protein`
- Source: `UniProt:P0A9I1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Represents a citryl-ACP lyase. {ECO:0000250}.

## Biological Role

Catalyzes (3S)-citryl-CoA oxaloacetate-lyase (acetyl-CoA-forming) (reaction.R00354). Component of citrate lyase (complex.ecocyc.ACECITLY-CPLX), citrate lyase, inactive (complex.ecocyc.CITLY-CPLX), citrate lyase, citryl-acyl carrrier protein lyase component (complex.ecocyc.CITRYLY-CPLX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Represents a citryl-ACP lyase. {ECO:0000250}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.R00354|reaction.R00354]] `KEGG` `database` - via EC:4.1.3.34
- `is_component_of` --> [[complex.ecocyc.ACECITLY-CPLX|complex.ecocyc.ACECITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` --> [[complex.ecocyc.CITRYLY-CPLX|complex.ecocyc.CITRYLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0616|gene.b0616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9I1`
- `KEGG:ecj:JW0608;eco:b0616;ecoc:C3026_03080;`
- `GeneID:86863136;93776869;945406;`
- `GO:GO:0000287; GO:0005737; GO:0006084; GO:0006101; GO:0006107; GO:0008815; GO:0008816; GO:0009346`
- `EC:4.1.3.34; 4.1.3.6`

## Notes

Citrate lyase subunit beta (Citrase beta chain) (EC 4.1.3.6) (Citrate (pro-3S)-lyase subunit beta) (Citryl-CoA lyase subunit) (EC 4.1.3.34)
