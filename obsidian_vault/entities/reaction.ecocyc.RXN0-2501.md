---
entity_id: "reaction.ecocyc.RXN0-2501"
entity_type: "reaction"
name: "chloride:proton antiport"
source_database: "EcoCyc"
source_id: "RXN0-2501"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# chloride:proton antiport

`reaction.ecocyc.RXN0-2501`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2501`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

CL- + PROTON -> CL- + PROTON; direction=REVERSIBLE EcoCyc reaction equation: CL- + PROTON -> CL- + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by chloride:H+ antiporter ClcA (complex.ecocyc.CPLX0-7961), clcB (protein.P76175). Substrates: H+ (molecule.C00080), chloride (molecule.ecocyc.CL-). Products: H+ (molecule.C00080), chloride (molecule.ecocyc.CL-).

## Annotation

CL- + PROTON -> CL- + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7961|complex.ecocyc.CPLX0-7961]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76175|protein.P76175]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CL-|molecule.ecocyc.CL-]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-8783|molecule.ecocyc.CPD-8783]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.F-|molecule.ecocyc.F-]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2501`

## Notes

CL- + PROTON -> CL- + PROTON; direction=REVERSIBLE
