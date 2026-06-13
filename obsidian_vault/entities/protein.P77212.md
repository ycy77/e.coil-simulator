---
entity_id: "protein.P77212"
entity_type: "protein"
name: "rclA"
source_database: "UniProt"
source_id: "P77212"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rclA ykgC b0304 JW5040"
---

# rclA

`protein.P77212`

## Static

- Type: `protein`
- Source: `UniProt:P77212`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in reactive chlorine species (RCS) stress resistance. {ECO:0000269|PubMed:24078635}.

## Biological Role

Component of cupric reductase RclA (complex.ecocyc.CPLX0-8542).

## Annotation

FUNCTION: Probably involved in reactive chlorine species (RCS) stress resistance. {ECO:0000269|PubMed:24078635}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8542|complex.ecocyc.CPLX0-8542]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0304|gene.b0304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77212`
- `KEGG:ecj:JW5040;eco:b0304;ecoc:C3026_01490;ecoc:C3026_24665;`
- `GeneID:946092;`
- `GO:GO:0003955; GO:0008823; GO:0016651; GO:0016668; GO:0042803; GO:0050660; GO:1901530`

## Notes

Probable pyridine nucleotide-disulfide oxidoreductase RclA (Reactive chlorine resistance protein A)
