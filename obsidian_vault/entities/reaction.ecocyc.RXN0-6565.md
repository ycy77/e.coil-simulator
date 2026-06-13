---
entity_id: "reaction.ecocyc.RXN0-6565"
entity_type: "reaction"
name: "RXN0-6565"
source_database: "EcoCyc"
source_id: "RXN0-6565"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6565

`reaction.ecocyc.RXN0-6565`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6565`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DIHYDRO-THYMINE + NAD -> THYMINE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: DIHYDRO-THYMINE + NAD -> THYMINE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by dihydropyrimidine dehydrogenase (NAD+) (complex.ecocyc.CPLX0-7788). Substrates: NAD+ (molecule.C00003), 5,6-dihydrothymine (molecule.ecocyc.DIHYDRO-THYMINE). Products: NADH (molecule.C00004), H+ (molecule.C00080), Thymine (molecule.C00178).

## Annotation

DIHYDRO-THYMINE + NAD -> THYMINE + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7788|complex.ecocyc.CPLX0-7788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00178|molecule.C00178]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DIHYDRO-THYMINE|molecule.ecocyc.DIHYDRO-THYMINE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6565`

## Notes

DIHYDRO-THYMINE + NAD -> THYMINE + NADH + PROTON; direction=REVERSIBLE
