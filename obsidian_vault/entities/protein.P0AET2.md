---
entity_id: "protein.P0AET2"
entity_type: "protein"
name: "hdeB"
source_database: "UniProt"
source_id: "P0AET2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00947, ECO:0000269|PubMed:17085547}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hdeB yhhD yhiC b3509 JW5669"
---

# hdeB

`protein.P0AET2`

## Static

- Type: `protein`
- Source: `UniProt:P0AET2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_00947, ECO:0000269|PubMed:17085547}.

## Enriched Summary

FUNCTION: Required for optimal acid stress protection, which is important for survival of enteric bacteria in the acidic environment of the host stomach. Exhibits a chaperone-like activity at acidic pH by preventing the aggregation of many different periplasmic proteins. {ECO:0000255|HAMAP-Rule:MF_00947, ECO:0000269|PubMed:17085547}.

## Biological Role

Component of periplasmic acid stress chaperone HdeB (complex.ecocyc.CPLX0-8207).

## Annotation

FUNCTION: Required for optimal acid stress protection, which is important for survival of enteric bacteria in the acidic environment of the host stomach. Exhibits a chaperone-like activity at acidic pH by preventing the aggregation of many different periplasmic proteins. {ECO:0000255|HAMAP-Rule:MF_00947, ECO:0000269|PubMed:17085547}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8207|complex.ecocyc.CPLX0-8207]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3509|gene.b3509]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AET2`
- `KEGG:ecj:JW5669;eco:b3509;ecoc:C3026_19010;`
- `GeneID:93778476;948026;`
- `GO:GO:0010447; GO:0030288; GO:0051082; GO:1990451`

## Notes

Acid stress chaperone HdeB (10K-L protein)
