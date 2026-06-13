---
entity_id: "protein.P0ACF4"
entity_type: "protein"
name: "hupB"
source_database: "UniProt"
source_id: "P0ACF4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hupB hopD b0440 JW0430"
---

# hupB

`protein.P0ACF4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACF4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}.

## Biological Role

Component of DNA-binding transcriptional dual regulator HU (complex.ecocyc.CPLX0-2021).

## Annotation

FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2021|complex.ecocyc.CPLX0-2021]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0440|gene.b0440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACF4`
- `KEGG:ecj:JW0430;eco:b0440;ecoc:C3026_02155;`
- `GeneID:86945354;949095;`
- `GO:GO:0003677; GO:0005829; GO:0006270; GO:0006281; GO:0006351; GO:0030261; GO:0030527; GO:0036386; GO:0042802; GO:1990103; GO:1990178`

## Notes

DNA-binding protein HU-beta (HU-1) (NS1)
