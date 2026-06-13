---
entity_id: "reaction.ecocyc.RXN0-310"
entity_type: "reaction"
name: "RXN0-310"
source_database: "EcoCyc"
source_id: "RXN0-310"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-310

`reaction.ecocyc.RXN0-310`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-310`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + METHYL-MALONYL-COA -> PROPIONYL-COA + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + METHYL-MALONYL-COA -> PROPIONYL-COA + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by methylmalonyl-CoA decarboxylase (complex.ecocyc.CPLX0-254). Substrates: H+ (molecule.C00080), (R)-Methylmalonyl-CoA (molecule.C01213). Products: CO2 (molecule.C00011), Propanoyl-CoA (molecule.C00100).

## Enriched Pathways

- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Annotation

PROTON + METHYL-MALONYL-COA -> PROPIONYL-COA + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-43` conversion of succinate to propanoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-254|complex.ecocyc.CPLX0-254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01213|molecule.C01213]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-310`

## Notes

PROTON + METHYL-MALONYL-COA -> PROPIONYL-COA + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
