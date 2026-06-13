---
entity_id: "protein.P27896"
entity_type: "protein"
name: "narQ"
source_database: "UniProt"
source_id: "P27896"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narQ b2469 JW2453"
---

# narQ

`protein.P27896`

## Static

- Type: `protein`
- Source: `UniProt:P27896`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate/nitrite availability to the NarL/NarP proteins. NarQ probably activates NarL and NarP by phosphorylation. NarQ probably negatively regulates the NarL protein by dephosphorylation.

## Biological Role

Component of sensor histidine kinase NarQ (complex.ecocyc.NARQ-CPLX), NarQ-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-NARQ).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate/nitrite availability to the NarL/NarP proteins. NarQ probably activates NarL and NarP by phosphorylation. NarQ probably negatively regulates the NarL protein by dephosphorylation.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.NARQ-CPLX|complex.ecocyc.NARQ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-NARQ|complex.ecocyc.PHOSPHO-NARQ]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2469|gene.b2469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27896`
- `KEGG:ecj:JW2453;eco:b2469;ecoc:C3026_13695;`
- `GeneID:946948;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0007165; GO:0042128; GO:0046983; GO:0071249; GO:0071250`
- `EC:2.7.13.3`

## Notes

Nitrate/nitrite sensor protein NarQ (EC 2.7.13.3)
