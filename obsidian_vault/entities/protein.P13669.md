---
entity_id: "protein.P13669"
entity_type: "protein"
name: "mngR"
source_database: "UniProt"
source_id: "P13669"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mngR farR g30 ybgB b0730 JW0719"
---

# mngR

`protein.P13669`

## Static

- Type: `protein`
- Source: `UniProt:P13669`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Represses mngA and mngB. Regulates its own expression. {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:7805834}.

## Biological Role

Component of DNA-binding transcriptional repressor MngR (complex.ecocyc.PC00103).

## Annotation

FUNCTION: Represses mngA and mngB. Regulates its own expression. {ECO:0000269|PubMed:14645248, ECO:0000269|PubMed:7805834}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.PC00103|complex.ecocyc.PC00103]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0730|gene.b0730]] `RegulonDB` `S` - regulator=MngR; target=mngR; function=-
- `represses` --> [[gene.b0731|gene.b0731]] `RegulonDB` `S` - regulator=MngR; target=mngA; function=-
- `represses` --> [[gene.b0732|gene.b0732]] `RegulonDB` `S` - regulator=MngR; target=mngB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0730|gene.b0730]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13669`
- `KEGG:ecj:JW0719;eco:b0730;ecoc:C3026_03655;`
- `GeneID:945371;`
- `GO:GO:0003677; GO:0003700; GO:0009408; GO:0045892`

## Notes

Mannosyl-D-glycerate transport/metabolism system repressor MngR (Fatty acyl-responsive regulator) (Protein P30)
