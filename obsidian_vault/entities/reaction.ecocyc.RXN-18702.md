---
entity_id: "reaction.ecocyc.RXN-18702"
entity_type: "reaction"
name: "RXN-18702"
source_database: "EcoCyc"
source_id: "RXN-18702"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18702

`reaction.ecocyc.RXN-18702`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18702`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

3-MERCAPTO-PYRUVATE + TUM1-L-cysteine -> TUM1-S-sulfanylcysteine + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 3-MERCAPTO-PYRUVATE + TUM1-L-cysteine -> TUM1-S-sulfanylcysteine + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Mercaptopyruvate (molecule.C00957), a [3-mercaptopyruvate sulfurtransferase]-L-cysteine (molecule.ecocyc.TUM1-L-cysteine). Products: Pyruvate (molecule.C00022), a [3-mercaptopyruvate sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.TUM1-S-sulfanylcysteine).

## Annotation

3-MERCAPTO-PYRUVATE + TUM1-L-cysteine -> TUM1-S-sulfanylcysteine + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.TUM1-S-sulfanylcysteine|molecule.ecocyc.TUM1-S-sulfanylcysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00957|molecule.C00957]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.TUM1-L-cysteine|molecule.ecocyc.TUM1-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18702`

## Notes

3-MERCAPTO-PYRUVATE + TUM1-L-cysteine -> TUM1-S-sulfanylcysteine + PYRUVATE; direction=PHYSIOL-LEFT-TO-RIGHT
