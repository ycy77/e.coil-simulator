---
entity_id: "reaction.ecocyc.RXN-25215"
entity_type: "reaction"
name: "RXN-25215"
source_database: "EcoCyc"
source_id: "RXN-25215"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-25215

`reaction.ecocyc.RXN-25215`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25215`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-6-DihydroUracil2449-23S-rRNAs + NAD -> 23S-rRNA-uridine2449 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: 5-6-DihydroUracil2449-23S-rRNAs + NAD -> 23S-rRNA-uridine2449 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by rdsA (protein.P37631). Substrates: NAD+ (molecule.C00003), a 5,6-dihydrouracil2449 in 23S rRNA (molecule.ecocyc.5-6-DihydroUracil2449-23S-rRNAs). Products: NADH (molecule.C00004), H+ (molecule.C00080), uridine2449 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine2449).

## Annotation

5-6-DihydroUracil2449-23S-rRNAs + NAD -> 23S-rRNA-uridine2449 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37631|protein.P37631]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-uridine2449|molecule.ecocyc.23S-rRNA-uridine2449]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-6-DihydroUracil2449-23S-rRNAs|molecule.ecocyc.5-6-DihydroUracil2449-23S-rRNAs]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25215`

## Notes

5-6-DihydroUracil2449-23S-rRNAs + NAD -> 23S-rRNA-uridine2449 + NADH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
