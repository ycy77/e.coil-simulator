---
entity_id: "reaction.ecocyc.RXN-16701"
entity_type: "reaction"
name: "RXN-16701"
source_database: "EcoCyc"
source_id: "RXN-16701"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16701

`reaction.ecocyc.RXN-16701`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16701`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-381 + NAD -> 2-KETOGLUTARATE + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CPD-381 + NAD -> 2-KETOGLUTARATE + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by phosphoglycerate dehydrogenase (complex.ecocyc.PGLYCDEHYDROG-CPLX). Substrates: NAD+ (molecule.C00003), (S)-2-Hydroxyglutarate (molecule.C03196). Products: NADH (molecule.C00004), 2-Oxoglutarate (molecule.C00026), H+ (molecule.C00080).

## Annotation

CPD-381 + NAD -> 2-KETOGLUTARATE + NADH + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.PGLYCDEHYDROG-CPLX|complex.ecocyc.PGLYCDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03196|molecule.C03196]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C02630|molecule.C02630]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03232|molecule.C03232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-16701`

## Notes

CPD-381 + NAD -> 2-KETOGLUTARATE + NADH + PROTON; direction=REVERSIBLE
