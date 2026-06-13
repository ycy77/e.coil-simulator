---
entity_id: "protein.P16430"
entity_type: "protein"
name: "hycD"
source_database: "UniProt"
source_id: "P16430"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycD hevD b2722 JW2692"
---

# hycD

`protein.P16430`

## Static

- Type: `protein`
- Source: `UniProt:P16430`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

Formate hydrogenlyase subunit 4 (FHL subunit 4) (Hydrogenase 3 component D)

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

Formate hydrogenlyase subunit 4 (FHL subunit 4) (Hydrogenase 3 component D)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2722|gene.b2722]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16430`
- `KEGG:ecj:JW2692;eco:b2722;ecoc:C3026_14975;`
- `GeneID:86860819;89517533;948994;`
- `GO:GO:0005886; GO:0006007; GO:0009061; GO:0009326; GO:0015944; GO:0016491; GO:0019645`

## Notes

Formate hydrogenlyase subunit 4 (FHL subunit 4) (Hydrogenase 3 component D)
