---
entity_id: "protein.P37309"
entity_type: "protein"
name: "arsR"
source_database: "UniProt"
source_id: "P37309"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "arsR arsE b3501 JW3468"
---

# arsR

`protein.P37309`

## Static

- Type: `protein`
- Source: `UniProt:P37309`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional repressor for the arsEFG operon. ArsE is a trans-acting regulatory protein which controls its own expression. The repressive effect of ArsE is alleviated by oxyions of +III oxidation state of arsenic, antimony, and bismuth, as well as arsenate (As(V)) (By similarity). {ECO:0000250}.

## Biological Role

Component of DNA-binding transcriptional repressor ArsR (complex.ecocyc.CPLX0-7734), ArsR-arsenite (complex.ecocyc.CPLX0-7736), ArsR-antimonite (complex.ecocyc.CPLX0-7739).

## Annotation

FUNCTION: Transcriptional repressor for the arsEFG operon. ArsE is a trans-acting regulatory protein which controls its own expression. The repressive effect of ArsE is alleviated by oxyions of +III oxidation state of arsenic, antimony, and bismuth, as well as arsenate (As(V)) (By similarity). {ECO:0000250}.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7734|complex.ecocyc.CPLX0-7734]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-7736|complex.ecocyc.CPLX0-7736]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7739|complex.ecocyc.CPLX0-7739]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3501|gene.b3501]] `RegulonDB` `S` - regulator=ArsR; target=arsR; function=-
- `represses` --> [[gene.b3502|gene.b3502]] `RegulonDB` `S` - regulator=ArsR; target=arsB; function=-
- `represses` --> [[gene.b3503|gene.b3503]] `RegulonDB` `S` - regulator=ArsR; target=arsC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3501|gene.b3501]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37309`
- `KEGG:ecj:JW3468;eco:b3501;ecoc:C3026_18965;`
- `GeneID:93778491;948013;`
- `GO:GO:0003677; GO:0003700; GO:0006351; GO:0006355; GO:0046685`

## Notes

Arsenical resistance operon repressor
