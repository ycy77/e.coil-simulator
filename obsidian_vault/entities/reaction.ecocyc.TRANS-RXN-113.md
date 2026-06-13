---
entity_id: "reaction.ecocyc.TRANS-RXN-113"
entity_type: "reaction"
name: "2-dehydro-3-deoxy-D-gluconate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-113"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-dehydro-3-deoxy-D-gluconate:proton symport

`reaction.ecocyc.TRANS-RXN-113`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-113`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE -> PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=REVERSIBLE EcoCyc reaction equation: PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE -> PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by kdgT (protein.P0A712). Substrates: H+ (molecule.C00080), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: H+ (molecule.C00080), 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204).

## Annotation

PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE -> PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A712|protein.P0A712]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-113`

## Notes

PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE -> PROTON + 2-DEHYDRO-3-DEOXY-D-GLUCONATE; direction=REVERSIBLE
