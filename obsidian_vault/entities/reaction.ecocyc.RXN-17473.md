---
entity_id: "reaction.ecocyc.RXN-17473"
entity_type: "reaction"
name: "RXN-17473"
source_database: "EcoCyc"
source_id: "RXN-17473"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17473

`reaction.ecocyc.RXN-17473`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17473`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD-5662 -> BIOTIN + CH33ADO + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-5662 -> BIOTIN + CH33ADO + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019), 4,5-secobiotin (molecule.ecocyc.CPD-5662). Products: L-Methionine (molecule.C00073), H+ (molecule.C00080), Biotin (molecule.C00120), 5'-deoxyadenosine (molecule.ecocyc.CH33ADO).

## Enriched Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + CPD-5662 -> BIOTIN + CH33ADO + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00120|molecule.C00120]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CH33ADO|molecule.ecocyc.CH33ADO]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-5662|molecule.ecocyc.CPD-5662]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17473`

## Notes

S-ADENOSYLMETHIONINE + CPD-5662 -> BIOTIN + CH33ADO + MET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
