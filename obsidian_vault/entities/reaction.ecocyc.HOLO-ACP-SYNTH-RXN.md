---
entity_id: "reaction.ecocyc.HOLO-ACP-SYNTH-RXN"
entity_type: "reaction"
name: "HOLO-ACP-SYNTH-RXN"
source_database: "EcoCyc"
source_id: "HOLO-ACP-SYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOLO-ACP-SYNTH-RXN

`reaction.ecocyc.HOLO-ACP-SYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOLO-ACP-SYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

All-apo-ACPs + CO-A -> 3-5-ADP + All-holo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: All-apo-ACPs + CO-A -> 3-5-ADP + All-holo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by holo-[acyl-carrier-protein] synthase (complex.ecocyc.HOLO-ACP-SYNTH-CPLX), acpT (protein.P37623). Substrates: CoA (molecule.C00010). Products: Adenosine 3',5'-bisphosphate (molecule.C00054), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.PWY-6012` acyl carrier protein metabolism (EcoCyc)

## Annotation

All-apo-ACPs + CO-A -> 3-5-ADP + All-holo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6012` acyl carrier protein metabolism (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.HOLO-ACP-SYNTH-CPLX|complex.ecocyc.HOLO-ACP-SYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37623|protein.P37623]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00054|molecule.C00054]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.KCL|molecule.ecocyc.KCL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.NH42SO4|molecule.ecocyc.NH42SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[protein.P0A6A8|protein.P0A6A8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:HOLO-ACP-SYNTH-RXN`

## Notes

All-apo-ACPs + CO-A -> 3-5-ADP + All-holo-ACPs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
