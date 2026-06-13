---
entity_id: "protein.P77485"
entity_type: "protein"
name: "cusS"
source_database: "UniProt"
source_id: "P77485"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cusS ybcZ b0570 JW5082"
---

# cusS

`protein.P77485`

## Static

- Type: `protein`
- Source: `UniProt:P77485`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Acts as a copper/silver ion sensor. Activates CusR by phosphorylation. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22348296}. This is the phosphorylated form of G6318-MONOMER "CusS" - the sensor histidine kinase of the CusSR two-component signal transduction system.

## Biological Role

Component of sensor histidine kinase CusS (complex.ecocyc.CPLX0-8288).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system CusS/CusR involved in response to copper and silver. Acts as a copper/silver ion sensor. Activates CusR by phosphorylation. {ECO:0000269|PubMed:11004187, ECO:0000269|PubMed:11283292, ECO:0000269|PubMed:11399769, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:22348296}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8288|complex.ecocyc.CPLX0-8288]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0570|gene.b0570]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77485`
- `KEGG:ecj:JW5082;eco:b0570;ecoc:C3026_02830;`
- `GeneID:945978;`
- `GO:GO:0000155; GO:0000160; GO:0004673; GO:0005524; GO:0005886; GO:0007165; GO:0016020; GO:0046872; GO:0071280; GO:0071292`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase CusS (EC 2.7.13.3)
