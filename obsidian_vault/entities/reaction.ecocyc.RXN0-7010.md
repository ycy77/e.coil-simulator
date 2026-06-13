---
entity_id: "reaction.ecocyc.RXN0-7010"
entity_type: "reaction"
name: "RXN0-7010"
source_database: "EcoCyc"
source_id: "RXN0-7010"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7010

`reaction.ecocyc.RXN0-7010`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7010`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-2511 + GLUTATHIONE -> CPD-16720 + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2511 + GLUTATHIONE -> CPD-16720 + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by glutathionyl-hydroquinone reductase YqjG (complex.ecocyc.CPLX0-7984). Substrates: Glutathione (molecule.C00051), 6-(glutathion-S-yl)-2-methylhydroquinone (molecule.ecocyc.CPD0-2511). Products: Glutathione disulfide (molecule.C00127), toluquinol (molecule.ecocyc.CPD-16720).

## Annotation

CPD0-2511 + GLUTATHIONE -> CPD-16720 + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7984|complex.ecocyc.CPLX0-7984]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16720|molecule.ecocyc.CPD-16720]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2511|molecule.ecocyc.CPD0-2511]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7010`

## Notes

CPD0-2511 + GLUTATHIONE -> CPD-16720 + OXIDIZED-GLUTATHIONE; direction=PHYSIOL-LEFT-TO-RIGHT
