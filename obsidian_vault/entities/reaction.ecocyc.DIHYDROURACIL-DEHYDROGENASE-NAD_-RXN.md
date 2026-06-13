---
entity_id: "reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN"
entity_type: "reaction"
name: "DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN"
source_database: "EcoCyc"
source_id: "DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN

`reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + DI-H-URACIL -> PROTON + NADH + URACIL; direction=REVERSIBLE EcoCyc reaction equation: NAD + DI-H-URACIL -> PROTON + NADH + URACIL; direction=REVERSIBLE.

## Biological Role

Catalyzed by dihydropyrimidine dehydrogenase (NAD+) (complex.ecocyc.CPLX0-7788). Substrates: NAD+ (molecule.C00003), 5,6-Dihydrouracil (molecule.C00429). Products: NADH (molecule.C00004), H+ (molecule.C00080), Uracil (molecule.C00106).

## Annotation

NAD + DI-H-URACIL -> PROTON + NADH + URACIL; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7788|complex.ecocyc.CPLX0-7788]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00106|molecule.C00106]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00429|molecule.C00429]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN`

## Notes

NAD + DI-H-URACIL -> PROTON + NADH + URACIL; direction=REVERSIBLE
