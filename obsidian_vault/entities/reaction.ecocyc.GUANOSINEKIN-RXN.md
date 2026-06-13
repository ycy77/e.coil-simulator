---
entity_id: "reaction.ecocyc.GUANOSINEKIN-RXN"
entity_type: "reaction"
name: "GUANOSINEKIN-RXN"
source_database: "EcoCyc"
source_id: "GUANOSINEKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GUANOSINEKIN-RXN

`reaction.ecocyc.GUANOSINEKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GUANOSINEKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: GUANOSINE + ATP -> PROTON + GMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by inosine/guanosine kinase (complex.ecocyc.CPLX0-322). Substrates: ATP (molecule.C00002), Guanosine (molecule.C00387). Products: ADP (molecule.C00008), H+ (molecule.C00080), GMP (molecule.C00144).

## Enriched Pathways

- `ecocyc.PWY-6618` guanine and guanosine salvage III (EcoCyc)

## Annotation

This reaction is part of nucleotide metabolism.

## Pathways

- `ecocyc.PWY-6618` guanine and guanosine salvage III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-322|complex.ecocyc.CPLX0-322]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00387|molecule.C00387]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00035|molecule.C00035]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GUANOSINEKIN-RXN`

## Notes

GUANOSINE + ATP -> PROTON + GMP + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
