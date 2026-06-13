---
entity_id: "reaction.ecocyc.2.5.1.25-RXN"
entity_type: "reaction"
name: "2.5.1.25-RXN"
source_database: "EcoCyc"
source_id: "2.5.1.25-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.5.1.25-RXN

`reaction.ecocyc.2.5.1.25-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.5.1.25-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Uridine47-in-tRNAPhe -> 3-N-3-carboxypropyl-uridine47-tRNAPhe + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Uridine47-in-tRNAPhe -> 3-N-3-carboxypropyl-uridine47-tRNAPhe + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uridine47 in tRNAPhe (molecule.ecocyc.Uridine47-in-tRNAPhe). Products: H+ (molecule.C00080), 5'-Methylthioadenosine (molecule.C00170), a 3-[(3S)-3-amino-3-carboxypropyl]-uridine47 in tRNAPhe (molecule.ecocyc.3-N-3-carboxypropyl-uridine47-tRNAPhe).

## Annotation

S-ADENOSYLMETHIONINE + Uridine47-in-tRNAPhe -> 3-N-3-carboxypropyl-uridine47-tRNAPhe + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.3-N-3-carboxypropyl-uridine47-tRNAPhe|molecule.ecocyc.3-N-3-carboxypropyl-uridine47-tRNAPhe]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Uridine47-in-tRNAPhe|molecule.ecocyc.Uridine47-in-tRNAPhe]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.5.1.25-RXN`

## Notes

S-ADENOSYLMETHIONINE + Uridine47-in-tRNAPhe -> 3-N-3-carboxypropyl-uridine47-tRNAPhe + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
