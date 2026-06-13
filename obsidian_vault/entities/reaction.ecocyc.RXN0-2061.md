---
entity_id: "reaction.ecocyc.RXN0-2061"
entity_type: "reaction"
name: "RXN0-2061"
source_database: "EcoCyc"
source_id: "RXN0-2061"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2061

`reaction.ecocyc.RXN0-2061`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2061`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-MURNAC-TETRAPEPTIDE + WATER -> D-ALANINE + UDP-AAGM-DIAMINOHEPTANEDIOATE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UDP-MURNAC-TETRAPEPTIDE + WATER -> D-ALANINE + UDP-AAGM-DIAMINOHEPTANEDIOATE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by murein tetrapeptide carboxypeptidase (complex.ecocyc.CPLX0-8616). Substrates: H2O (molecule.C00001), UDP-MurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala (molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE). Products: D-Alanine (molecule.C00133), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877).

## Annotation

UDP-MURNAC-TETRAPEPTIDE + WATER -> D-ALANINE + UDP-AAGM-DIAMINOHEPTANEDIOATE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8616|complex.ecocyc.CPLX0-8616]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04877|molecule.C04877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE|molecule.ecocyc.UDP-MURNAC-TETRAPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C01941|molecule.C01941]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2061`

## Notes

UDP-MURNAC-TETRAPEPTIDE + WATER -> D-ALANINE + UDP-AAGM-DIAMINOHEPTANEDIOATE; direction=LEFT-TO-RIGHT
