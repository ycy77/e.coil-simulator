---
entity_id: "reaction.ecocyc.TRANS-RXN0-469"
entity_type: "reaction"
name: "alanine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-469"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# alanine:proton antiport

`reaction.ecocyc.TRANS-RXN0-469`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-469`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-ALPHA-ALANINE + PROTON -> L-ALPHA-ALANINE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: L-ALPHA-ALANINE + PROTON -> L-ALPHA-ALANINE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by L-alanine exporter (complex.ecocyc.CPLX0-8791). Substrates: L-Alanine (molecule.C00041), H+ (molecule.C00080). Products: L-Alanine (molecule.C00041), H+ (molecule.C00080).

## Annotation

L-ALPHA-ALANINE + PROTON -> L-ALPHA-ALANINE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8791|complex.ecocyc.CPLX0-8791]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00740|molecule.C00740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-469`

## Notes

L-ALPHA-ALANINE + PROTON -> L-ALPHA-ALANINE + PROTON; direction=REVERSIBLE
