---
entity_id: "protein.P08400"
entity_type: "protein"
name: "phoR"
source_database: "UniProt"
source_id: "P08400"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2187152}; Multi-pass membrane protein {ECO:0000269|PubMed:2187152}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoR nmpB b0400 JW0390"
---

# phoR

`protein.P08400`

## Static

- Type: `protein`
- Source: `UniProt:P08400`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2187152}; Multi-pass membrane protein {ECO:0000269|PubMed:2187152}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system PhoR/PhoB involved in the phosphate regulon genes expression. PhoR may function as a membrane-associated protein kinase that phosphorylates PhoB in response to environmental signals.

## Biological Role

Component of sensor histidine kinase PhoR (complex.ecocyc.PHOR-CPLX), PhoR-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-PHOR).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system PhoR/PhoB involved in the phosphate regulon genes expression. PhoR may function as a membrane-associated protein kinase that phosphorylates PhoB in response to environmental signals.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.PHOR-CPLX|complex.ecocyc.PHOR-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-PHOR|complex.ecocyc.PHOSPHO-PHOR]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0400|gene.b0400]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08400`
- `KEGG:ecj:JW0390;eco:b0400;ecoc:C3026_01945;`
- `GeneID:945044;`
- `GO:GO:0000155; GO:0004721; GO:0005524; GO:0005829; GO:0005886; GO:0006355; GO:0006817; GO:0007165; GO:0016036`
- `EC:2.7.13.3`

## Notes

Phosphate regulon sensor protein PhoR (EC 2.7.13.3)
