---
entity_id: "protein.P0ABF6"
entity_type: "protein"
name: "cdd"
source_database: "UniProt"
source_id: "P0ABF6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cdd b2143 JW2131"
---

# cdd

`protein.P0ABF6`

## Static

- Type: `protein`
- Source: `UniProt:P0ABF6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This enzyme scavenges exogenous and endogenous cytidine and 2'-deoxycytidine for UMP synthesis.

## Biological Role

Catalyzes cytidine aminohydrolase (reaction.R01878), 5'-deoxy-5-fluorocytidine aminohydrolase (reaction.R08221). Component of cytidine/deoxycytidine deaminase (complex.ecocyc.CYTIDEAM-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: This enzyme scavenges exogenous and endogenous cytidine and 2'-deoxycytidine for UMP synthesis.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R01878|reaction.R01878]] `KEGG` `database` - via EC:3.5.4.5
- `catalyzes` --> [[reaction.R08221|reaction.R08221]] `KEGG` `database` - via EC:3.5.4.5
- `is_component_of` --> [[complex.ecocyc.CYTIDEAM-CPLX|complex.ecocyc.CYTIDEAM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2143|gene.b2143]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABF6`
- `KEGG:ecj:JW2131;eco:b2143;ecoc:C3026_12010;`
- `GeneID:93775039;946663;`
- `GO:GO:0001884; GO:0004126; GO:0005829; GO:0006217; GO:0008270; GO:0015949; GO:0042802; GO:0042803`
- `EC:3.5.4.5`

## Notes

Cytidine deaminase (EC 3.5.4.5) (Cytidine aminohydrolase) (CDA)
