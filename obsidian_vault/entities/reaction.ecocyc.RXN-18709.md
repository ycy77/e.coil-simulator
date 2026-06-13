---
entity_id: "reaction.ecocyc.RXN-18709"
entity_type: "reaction"
name: "RXN-18709"
source_database: "EcoCyc"
source_id: "RXN-18709"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18709

`reaction.ecocyc.RXN-18709`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18709`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TusA-Persulfides + TusD-L-cysteine -> TusA-L-cysteine + TusD-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TusA-Persulfides + TusD-L-cysteine -> TusA-L-cysteine + TusD-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tusA (protein.P0A890). Substrates: a [TusA sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.TusA-Persulfides), a [TusD]-L-cysteine (molecule.ecocyc.TusD-L-cysteine). Products: a [TusA]-L-cysteine (molecule.ecocyc.TusA-L-cysteine), a [TusD sulfur-carrier protein]-S-sulfanyl-L-cysteine (molecule.ecocyc.TusD-Persulfides).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

TusA-Persulfides + TusD-L-cysteine -> TusA-L-cysteine + TusD-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A890|protein.P0A890]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.TusA-L-cysteine|molecule.ecocyc.TusA-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TusD-Persulfides|molecule.ecocyc.TusD-Persulfides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.TusA-Persulfides|molecule.ecocyc.TusA-Persulfides]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TusD-L-cysteine|molecule.ecocyc.TusD-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18709`

## Notes

TusA-Persulfides + TusD-L-cysteine -> TusA-L-cysteine + TusD-Persulfides; direction=PHYSIOL-LEFT-TO-RIGHT
