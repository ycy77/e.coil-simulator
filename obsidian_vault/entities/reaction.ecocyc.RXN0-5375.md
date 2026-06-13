---
entity_id: "reaction.ecocyc.RXN0-5375"
entity_type: "reaction"
name: "RXN0-5375"
source_database: "EcoCyc"
source_id: "RXN0-5375"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5375

`reaction.ecocyc.RXN0-5375`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5375`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ANTHRANILATE + CPD0-1148 + NAD -> PROTON + CPD0-1147 + NADH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ANTHRANILATE + CPD0-1148 + NAD -> PROTON + CPD0-1147 + NADH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by FMN dependent NADH:quinone oxidoreductase (complex.ecocyc.CPLX0-7693). Substrates: NAD+ (molecule.C00003), Anthranilate (molecule.C00108), N,N-dimethyl-1,4-phenylenediamine (molecule.ecocyc.CPD0-1148). Products: NADH (molecule.C00004), H+ (molecule.C00080), methyl red (molecule.ecocyc.CPD0-1147).

## Annotation

ANTHRANILATE + CPD0-1148 + NAD -> PROTON + CPD0-1147 + NADH; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7693|complex.ecocyc.CPLX0-7693]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1147|molecule.ecocyc.CPD0-1147]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00108|molecule.C00108]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1148|molecule.ecocyc.CPD0-1148]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5375`

## Notes

ANTHRANILATE + CPD0-1148 + NAD -> PROTON + CPD0-1147 + NADH; direction=PHYSIOL-RIGHT-TO-LEFT
