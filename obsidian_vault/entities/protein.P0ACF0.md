---
entity_id: "protein.P0ACF0"
entity_type: "protein"
name: "hupA"
source_database: "UniProt"
source_id: "P0ACF0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hupA b4000 JW3964"
---

# hupA

`protein.P0ACF0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACF0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}.

## Enriched Summary

FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}.

## Biological Role

Component of DNA-binding transcriptional dual regulator HU (complex.ecocyc.CPLX0-2021), HUαα (complex.ecocyc.CPLX0-8256).

## Annotation

FUNCTION: Histone-like DNA-binding protein which is capable of wrapping DNA to stabilize it, and thus to prevent its denaturation under extreme environmental conditions. {ECO:0000305|PubMed:24916461}.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2021|complex.ecocyc.CPLX0-2021]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8256|complex.ecocyc.CPLX0-8256]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4000|gene.b4000]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACF0`
- `KEGG:ecj:JW3964;eco:b4000;ecoc:C3026_21605;`
- `GeneID:86861599;93777894;948499;`
- `GO:GO:0003677; GO:0005829; GO:0006270; GO:0006281; GO:0006351; GO:0006974; GO:0016020; GO:0030261; GO:0030527; GO:0036386; GO:0042802; GO:1990103; GO:1990178`

## Notes

DNA-binding protein HU-alpha (HU-2) (NS2)
