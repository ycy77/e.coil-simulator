---
entity_id: "protein.P0ADU2"
entity_type: "protein"
name: "ygiN"
source_database: "UniProt"
source_id: "P0ADU2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygiN b3029 JW2997"
---

# ygiN

`protein.P0ADU2`

## Static

- Type: `protein`
- Source: `UniProt:P0ADU2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Can oxidize menadiol to menadione (PubMed:15613473). May work in concert with MdaB to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473}.

## Biological Role

Component of putative quinol monooxygenase YgiN (complex.ecocyc.CPLX0-3141).

## Annotation

FUNCTION: Can oxidize menadiol to menadione (PubMed:15613473). May work in concert with MdaB to form a quinone redox cycle (PubMed:15613473). {ECO:0000269|PubMed:15613473}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3141|complex.ecocyc.CPLX0-3141]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3029|gene.b3029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADU2`
- `KEGG:ecj:JW2997;eco:b3029;ecoc:C3026_16545;`
- `GeneID:93778964;947506;`
- `GO:GO:0005829; GO:0010447; GO:0016491; GO:0042803`
- `EC:1.-.-.-`

## Notes

Probable quinol monooxygenase YgiN (QuMo) (EC 1.-.-.-)
