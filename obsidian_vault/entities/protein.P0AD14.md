---
entity_id: "protein.P0AD14"
entity_type: "protein"
name: "btsS"
source_database: "UniProt"
source_id: "P0AD14"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "btsS yehU b2126 JW5353"
---

# btsS

`protein.P0AD14`

## Static

- Type: `protein`
- Source: `UniProt:P0AD14`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsS is a high-affinity receptor for extracellular pyruvate that activates BtsR by phosphorylation. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}.

## Biological Role

Component of high-affinity pyruvate receptor (complex.ecocyc.CPLX0-10815).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system BtsS/BtsR, which is part of a nutrient-sensing regulatory network composed of BtsS/BtsR, the low-affinity pyruvate signaling system YpdA/YpdB and their respective target proteins, BtsT and YhjX. Responds to depletion of nutrients, specifically serine, and the concomitant presence of extracellular pyruvate. BtsS is a high-affinity receptor for extracellular pyruvate that activates BtsR by phosphorylation. Activation of the BtsS/BtsR signaling cascade also suppresses YpdA/YpdB-mediated yhjX induction. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22685278, ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:28469239}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10815|complex.ecocyc.CPLX0-10815]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2126|gene.b2126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD14`
- `KEGG:ecj:JW5353;eco:b2126;ecoc:C3026_11920;`
- `GeneID:75172247;75206372;949027;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0007165; GO:0031667; GO:0033293; GO:0071555`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase BtsS (EC 2.7.13.3)
