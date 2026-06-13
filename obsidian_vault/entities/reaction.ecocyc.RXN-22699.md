---
entity_id: "reaction.ecocyc.RXN-22699"
entity_type: "reaction"
name: "RXN-22699"
source_database: "EcoCyc"
source_id: "RXN-22699"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22699

`reaction.ecocyc.RXN-22699`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22699`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

TusE-S-sulfanylcysteine + MnmA-Cysteine -> MnmA-Sulfanyl-Cysteine + TusE-L-cysteine; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: TusE-S-sulfanylcysteine + MnmA-Cysteine -> MnmA-Sulfanyl-Cysteine + TusE-L-cysteine; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tusE (protein.P0AB18). Substrates: a [tRNA-uridine 2-sulfurtransferase]-L-cysteine (molecule.ecocyc.MnmA-Cysteine), a [TusE sulfur carrier protein]-S-sulfanylcysteine (molecule.ecocyc.TusE-S-sulfanylcysteine). Products: a [tRNA-uridine 2-sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.MnmA-Sulfanyl-Cysteine), a [TusE sulfur carrier protein]-L-cysteine (molecule.ecocyc.TusE-L-cysteine).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

TusE-S-sulfanylcysteine + MnmA-Cysteine -> MnmA-Sulfanyl-Cysteine + TusE-L-cysteine; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AB18|protein.P0AB18]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.MnmA-Sulfanyl-Cysteine|molecule.ecocyc.MnmA-Sulfanyl-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TusE-L-cysteine|molecule.ecocyc.TusE-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.MnmA-Cysteine|molecule.ecocyc.MnmA-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TusE-S-sulfanylcysteine|molecule.ecocyc.TusE-S-sulfanylcysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22699`

## Notes

TusE-S-sulfanylcysteine + MnmA-Cysteine -> MnmA-Sulfanyl-Cysteine + TusE-L-cysteine; direction=PHYSIOL-LEFT-TO-RIGHT
