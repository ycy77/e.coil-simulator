---
entity_id: "protein.P75914"
entity_type: "protein"
name: "ycdX"
source_database: "UniProt"
source_id: "P75914"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycdX b1034 JW1017"
---

# ycdX

`protein.P75914`

## Static

- Type: `protein`
- Source: `UniProt:P75914`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes p-nitrophenyl phosphate (pNPP) in vitro. Involved in the swarming motility process. {ECO:0000269|PubMed:21965574}.

## Biological Role

Component of zinc-binding phosphatase YcdX (complex.ecocyc.CPLX0-7945).

## Annotation

FUNCTION: Hydrolyzes p-nitrophenyl phosphate (pNPP) in vitro. Involved in the swarming motility process. {ECO:0000269|PubMed:21965574}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7945|complex.ecocyc.CPLX0-7945]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b1034|gene.b1034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75914`
- `KEGG:ecj:JW1017;eco:b1034;ecoc:C3026_06300;`
- `GeneID:75203622;948477;`
- `GO:GO:0005829; GO:0008270; GO:0016791; GO:0042578; GO:0042802; GO:0071978`
- `EC:3.1.3.-`

## Notes

Probable phosphatase YcdX (EC 3.1.3.-)
