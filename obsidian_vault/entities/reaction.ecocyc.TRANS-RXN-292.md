---
entity_id: "reaction.ecocyc.TRANS-RXN-292"
entity_type: "reaction"
name: "Li+:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-292"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Li+:proton antiport

`reaction.ecocyc.TRANS-RXN-292`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-292`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

LI+ + PROTON -> LI+ + PROTON; direction=REVERSIBLE EcoCyc reaction equation: LI+ + PROTON -> LI+ + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by Na+:H+ antiporter NhaA (complex.ecocyc.CPLX0-7629). Substrates: H+ (molecule.C00080), Li+ (molecule.ecocyc.LI_). Products: H+ (molecule.C00080), Li+ (molecule.ecocyc.LI_).

## Annotation

LI+ + PROTON -> LI+ + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7629|complex.ecocyc.CPLX0-7629]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.LI|molecule.ecocyc.LI_]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-292`

## Notes

LI+ + PROTON -> LI+ + PROTON; direction=REVERSIBLE
