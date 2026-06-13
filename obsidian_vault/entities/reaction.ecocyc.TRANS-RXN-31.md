---
entity_id: "reaction.ecocyc.TRANS-RXN-31"
entity_type: "reaction"
name: "xanthosine:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-31"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# xanthosine:proton symport

`reaction.ecocyc.TRANS-RXN-31`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-31`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + XANTHOSINE -> PROTON + XANTHOSINE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + XANTHOSINE -> PROTON + XANTHOSINE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by xapB (protein.P45562). Substrates: H+ (molecule.C00080), Xanthosine (molecule.C01762). Products: H+ (molecule.C00080), Xanthosine (molecule.C01762).

## Annotation

PROTON + XANTHOSINE -> PROTON + XANTHOSINE; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P45562|protein.P45562]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01762|molecule.C01762]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01762|molecule.C01762]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-31`

## Notes

PROTON + XANTHOSINE -> PROTON + XANTHOSINE; direction=LEFT-TO-RIGHT
