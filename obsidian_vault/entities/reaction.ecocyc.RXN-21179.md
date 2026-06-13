---
entity_id: "reaction.ecocyc.RXN-21179"
entity_type: "reaction"
name: "RXN-21179"
source_database: "EcoCyc"
source_id: "RXN-21179"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21179

`reaction.ecocyc.RXN-21179`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21179`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + tRNA-uridines -> CPD-8539 + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-uridines -> CPD-8539 + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tapT (protein.Q47319). Substrates: S-Adenosyl-L-methionine (molecule.C00019), tRNA uridine (molecule.C00868). Products: H+ (molecule.C00080), 5'-Methylthioadenosine (molecule.C00170), a 3-[(3S)-3-amino-3-carboxypropyl]-uridine in tRNA (molecule.ecocyc.CPD-8539).

## Annotation

S-ADENOSYLMETHIONINE + tRNA-uridines -> CPD-8539 + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.Q47319|protein.Q47319]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00170|molecule.C00170]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-8539|molecule.ecocyc.CPD-8539]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00868|molecule.C00868]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21179`

## Notes

S-ADENOSYLMETHIONINE + tRNA-uridines -> CPD-8539 + 5-METHYLTHIOADENOSINE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
