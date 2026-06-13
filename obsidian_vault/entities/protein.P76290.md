---
entity_id: "protein.P76290"
entity_type: "protein"
name: "cmoA"
source_database: "UniProt"
source_id: "P76290"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmoA yecO b1870 JW1859"
---

# cmoA

`protein.P76290`

## Static

- Type: `protein`
- Source: `UniProt:P76290`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM). {ECO:0000255|HAMAP-Rule:MF_01589, ECO:0000269|PubMed:23676670}.

## Biological Role

Component of carboxy-S-adenosyl-L-methionine synthase (complex.ecocyc.CPLX0-8010).

## Annotation

FUNCTION: Catalyzes the conversion of S-adenosyl-L-methionine (SAM) to carboxy-S-adenosyl-L-methionine (Cx-SAM). {ECO:0000255|HAMAP-Rule:MF_01589, ECO:0000269|PubMed:23676670}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8010|complex.ecocyc.CPLX0-8010]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1870|gene.b1870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76290`
- `KEGG:ecj:JW1859;eco:b1870;ecoc:C3026_10645;`
- `GeneID:946380;`
- `GO:GO:0002098; GO:0005829; GO:0008168; GO:0016743; GO:0042803; GO:1904047`
- `EC:2.1.3.-`

## Notes

Carboxy-S-adenosyl-L-methionine synthase (Cx-SAM synthase) (EC 2.1.3.-)
