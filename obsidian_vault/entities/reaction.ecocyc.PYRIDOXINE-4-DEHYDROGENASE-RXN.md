---
entity_id: "reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "PYRIDOXINE-4-DEHYDROGENASE-RXN"
source_database: "EcoCyc"
source_id: "PYRIDOXINE-4-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRIDOXINE-4-DEHYDROGENASE-RXN

`reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRIDOXINE-4-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NADP + PYRIDOXINE -> PROTON + NADPH + PYRIDOXAL; direction=REVERSIBLE EcoCyc reaction equation: NADP + PYRIDOXINE -> PROTON + NADPH + PYRIDOXAL; direction=REVERSIBLE.

## Biological Role

Catalyzed by pdxI (protein.P25906). Substrates: NADP+ (molecule.C00006), Pyridoxine (molecule.C00314). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Pyridoxal (molecule.C00250).

## Enriched Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Annotation

NADP + PYRIDOXINE -> PROTON + NADPH + PYRIDOXAL; direction=REVERSIBLE

## Pathways

- `ecocyc.PLPSAL-PWY` pyridoxal 5'-phosphate salvage I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25906|protein.P25906]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00250|molecule.C00250]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00314|molecule.C00314]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRIDOXINE-4-DEHYDROGENASE-RXN`

## Notes

NADP + PYRIDOXINE -> PROTON + NADPH + PYRIDOXAL; direction=REVERSIBLE
