---
entity_id: "reaction.ecocyc.TRANS-RXN0-228"
entity_type: "reaction"
name: "5-ketogluconate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-228"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 5-ketogluconate:proton symport

`reaction.ecocyc.TRANS-RXN0-228`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-228`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + 5-DEHYDROGLUCONATE -> 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: PROTON + 5-DEHYDROGLUCONATE -> 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by idnT (protein.P39344). Substrates: H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE). Products: H+ (molecule.C00080), 5-dehydro-D-gluconate (molecule.ecocyc.5-DEHYDROGLUCONATE).

## Annotation

PROTON + 5-DEHYDROGLUCONATE -> 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P39344|protein.P39344]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-DEHYDROGLUCONATE|molecule.ecocyc.5-DEHYDROGLUCONATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-228`

## Notes

PROTON + 5-DEHYDROGLUCONATE -> 5-DEHYDROGLUCONATE + PROTON; direction=REVERSIBLE
