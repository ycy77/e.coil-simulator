---
entity_id: "reaction.ecocyc.RXN0-7024"
entity_type: "reaction"
name: "RXN0-7024"
source_database: "EcoCyc"
source_id: "RXN0-7024"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7024

`reaction.ecocyc.RXN0-7024`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7024`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-1091 + NAD -> CPD-389 + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-1091 + NAD -> CPD-389 + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ureidoglycolate dehydrogenase (complex.ecocyc.CPLX0-7993). Substrates: NAD+ (molecule.C00003), (S)-Ureidoglycolate (molecule.C00603). Products: NADH (molecule.C00004), H+ (molecule.C00080), Oxalureate (molecule.C00802).

## Enriched Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Annotation

CPD-1091 + NAD -> CPD-389 + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-41` allantoin degradation IV (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7993|complex.ecocyc.CPLX0-7993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00802|molecule.C00802]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00603|molecule.C00603]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7024`

## Notes

CPD-1091 + NAD -> CPD-389 + NADH + PROTON; direction=LEFT-TO-RIGHT
