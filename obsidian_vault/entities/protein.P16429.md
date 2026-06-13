---
entity_id: "protein.P16429"
entity_type: "protein"
name: "hycC"
source_database: "UniProt"
source_id: "P16429"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycC hevC b2723 JW2693"
---

# hycC

`protein.P16429`

## Static

- Type: `protein`
- Source: `UniProt:P16429`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

Formate hydrogenlyase subunit 3 (FHL subunit 3) (Hydrogenase-3 component C)

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

Formate hydrogenlyase subunit 3 (FHL subunit 3) (Hydrogenase-3 component C)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2723|gene.b2723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16429`
- `KEGG:ecj:JW2693;eco:b2723;ecoc:C3026_14980;`
- `GeneID:945327;`
- `GO:GO:0005886; GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0016491; GO:0019645; GO:0042773`

## Notes

Formate hydrogenlyase subunit 3 (FHL subunit 3) (Hydrogenase-3 component C)
