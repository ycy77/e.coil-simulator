---
entity_id: "protein.P0A8H3"
entity_type: "protein"
name: "zupT"
source_database: "UniProt"
source_id: "P0A8H3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00548, ECO:0000269|PubMed:20225068, ECO:0000269|PubMed:34793140}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00548}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zupT ygiE b3040 JW3008"
---

# zupT

`protein.P0A8H3`

## Static

- Type: `protein`
- Source: `UniProt:P0A8H3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_00548, ECO:0000269|PubMed:20225068, ECO:0000269|PubMed:34793140}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_00548}.

## Enriched Summary

FUNCTION: Mediates zinc uptake (PubMed:11790762, PubMed:15716430, PubMed:20225068, PubMed:34793140). Has broad metal specificity and can also mediate the uptake of cadmium, cobalt, iron, manganese and possibly copper (PubMed:11790762, PubMed:15716430, PubMed:20225068, PubMed:34793140). Has a slight preference for zinc (PubMed:20225068). {ECO:0000269|PubMed:11790762, ECO:0000269|PubMed:15716430, ECO:0000269|PubMed:20225068, ECO:0000269|PubMed:34793140}.

## Biological Role

Component of divalent metal ion transporter ZupT (complex.ecocyc.CPLX0-8617).

## Annotation

FUNCTION: Mediates zinc uptake (PubMed:11790762, PubMed:15716430, PubMed:20225068, PubMed:34793140). Has broad metal specificity and can also mediate the uptake of cadmium, cobalt, iron, manganese and possibly copper (PubMed:11790762, PubMed:15716430, PubMed:20225068, PubMed:34793140). Has a slight preference for zinc (PubMed:20225068). {ECO:0000269|PubMed:11790762, ECO:0000269|PubMed:15716430, ECO:0000269|PubMed:20225068, ECO:0000269|PubMed:34793140}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8617|complex.ecocyc.CPLX0-8617]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3040|gene.b3040]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8H3`
- `KEGG:ecj:JW3008;eco:b3040;ecoc:C3026_16600;`
- `GeneID:93778954;947035;`
- `GO:GO:0005385; GO:0005886; GO:0006824; GO:0006829; GO:0015093; GO:0016020; GO:0046872; GO:0071577; GO:0071578; GO:0098711`

## Notes

Zinc transporter ZupT (Divalent metal ion transporter ZupT) (Zinc uptake transporter)
