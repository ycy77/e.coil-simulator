---
entity_id: "reaction.ecocyc.DLACTDEHYDROGNAD-RXN"
entity_type: "reaction"
name: "DLACTDEHYDROGNAD-RXN"
source_database: "EcoCyc"
source_id: "DLACTDEHYDROGNAD-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DLACTDEHYDROGNAD-RXN

`reaction.ecocyc.DLACTDEHYDROGNAD-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DLACTDEHYDROGNAD-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + D-LACTATE -> PROTON + NADH + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: NAD + D-LACTATE -> PROTON + NADH + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by D-lactate dehydrogenase (complex.ecocyc.CPLX0-8158). Substrates: NAD+ (molecule.C00003), (R)-Lactate (molecule.C00256). Products: NADH (molecule.C00004), Pyruvate (molecule.C00022), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-8274` pyruvate fermentation to (R)-lactate (EcoCyc)

## Annotation

NAD + D-LACTATE -> PROTON + NADH + PYRUVATE; direction=REVERSIBLE

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-8274` pyruvate fermentation to (R)-lactate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8158|complex.ecocyc.CPLX0-8158]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00256|molecule.C00256]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01444|molecule.C01444]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DLACTDEHYDROGNAD-RXN`

## Notes

NAD + D-LACTATE -> PROTON + NADH + PYRUVATE; direction=REVERSIBLE
