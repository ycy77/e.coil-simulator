---
entity_id: "protein.P76339"
entity_type: "protein"
name: "hprS"
source_database: "UniProt"
source_id: "P76339"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hprS yedV b1968 JW1951"
---

# hprS

`protein.P76339`

## Static

- Type: `protein`
- Source: `UniProt:P76339`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Senses H(2)O(2), maybe via the redox state of the membrane (PubMed:27983483). Activates HprR by phosphorylation (PubMed:15522865). Can also phosphorylate CusR (PubMed:15522865). {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}.

## Biological Role

Component of sensor histidine kinase HprS (complex.ecocyc.CPLX0-9039), HprS-N-phospho-L-histidine (complex.ecocyc.CPLX0-9041).

## Annotation

FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Senses H(2)O(2), maybe via the redox state of the membrane (PubMed:27983483). Activates HprR by phosphorylation (PubMed:15522865). Can also phosphorylate CusR (PubMed:15522865). {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-9039|complex.ecocyc.CPLX0-9039]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-9041|complex.ecocyc.CPLX0-9041]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1968|gene.b1968]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76339`
- `KEGG:ecj:JW1951;eco:b1968;ecoc:C3026_11120;`
- `GeneID:946487;`
- `GO:GO:0000155; GO:0000160; GO:0004672; GO:0005524; GO:0005886; GO:0006974; GO:0016772; GO:0046688; GO:1901530`
- `EC:2.7.13.3`

## Notes

Sensor histidine kinase HprS (EC 2.7.13.3) (Hydrogen peroxide response sensor)
