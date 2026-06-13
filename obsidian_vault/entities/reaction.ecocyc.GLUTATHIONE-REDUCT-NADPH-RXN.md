---
entity_id: "reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN"
entity_type: "reaction"
name: "GLUTATHIONE-REDUCT-NADPH-RXN"
source_database: "EcoCyc"
source_id: "GLUTATHIONE-REDUCT-NADPH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTATHIONE-REDUCT-NADPH-RXN

`reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTATHIONE-REDUCT-NADPH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is necessary to recycle oxidized glutathione to maintain high levels of reduced glutathione in the cytosol. EcoCyc reaction equation: GLUTATHIONE + NADP -> OXIDIZED-GLUTATHIONE + NADPH + PROTON; direction=RIGHT-TO-LEFT. This reaction is necessary to recycle oxidized glutathione to maintain high levels of reduced glutathione in the cytosol.

## Biological Role

Catalyzed by glutathione reductase (complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX). Substrates: NADP+ (molecule.C00006), Glutathione (molecule.C00051). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Glutathione disulfide (molecule.C00127).

## Annotation

This reaction is necessary to recycle oxidized glutathione to maintain high levels of reduced glutathione in the cytosol.

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX|complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00051|molecule.C00051]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00127|molecule.C00127]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTATHIONE-REDUCT-NADPH-RXN`

## Notes

GLUTATHIONE + NADP -> OXIDIZED-GLUTATHIONE + NADPH + PROTON; direction=RIGHT-TO-LEFT
