---
entity_id: "reaction.ecocyc.RXN0-5398"
entity_type: "reaction"
name: "RXN0-5398"
source_database: "EcoCyc"
source_id: "RXN0-5398"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Pseudouridine synthase"
  - "Uracil hydrolyase"
  - "TRUB PSEUDOURIDINE (PSI) SYNTHASE HOMOLOG 1"
---

# RXN0-5398

`reaction.ecocyc.RXN0-5398`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5398`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-15317 + URACIL -> WATER + PSEUDOURIDINE-5-P; direction=REVERSIBLE EcoCyc reaction equation: CPD-15317 + URACIL -> WATER + PSEUDOURIDINE-5-P; direction=REVERSIBLE.

## Biological Role

Catalyzed by pseudouridine-5'-phosphate glycosidase (complex.ecocyc.CPLX0-8233). Substrates: Uracil (molecule.C00106), D-ribofuranose 5-phosphate (molecule.ecocyc.CPD-15317). Products: H2O (molecule.C00001), Pseudouridine 5'-phosphate (molecule.C01168).

## Enriched Pathways

- `ecocyc.PWY-6019` pseudouridine degradation (EcoCyc)

## Annotation

CPD-15317 + URACIL -> WATER + PSEUDOURIDINE-5-P; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-6019` pseudouridine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8233|complex.ecocyc.CPLX0-8233]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01168|molecule.C01168]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-15317|molecule.ecocyc.CPD-15317]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5398`

## Notes

CPD-15317 + URACIL -> WATER + PSEUDOURIDINE-5-P; direction=REVERSIBLE
