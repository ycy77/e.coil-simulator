---
entity_id: "reaction.ecocyc.RXN-12353"
entity_type: "reaction"
name: "RXN-12353"
source_database: "EcoCyc"
source_id: "RXN-12353"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-12353

`reaction.ecocyc.RXN-12353`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12353`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Methylated-DNA-Bases + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> Nucleobases-in-DNA + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Methylated-DNA-Bases + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> Nucleobases-in-DNA + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), a methylated nucleobase within DNA (molecule.ecocyc.Methylated-DNA-Bases). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), a nucleobase within DNA (molecule.ecocyc.Nucleobases-in-DNA).

## Annotation

Methylated-DNA-Bases + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> Nucleobases-in-DNA + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Nucleobases-in-DNA|molecule.ecocyc.Nucleobases-in-DNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Methylated-DNA-Bases|molecule.ecocyc.Methylated-DNA-Bases]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12353`

## Notes

Methylated-DNA-Bases + OXYGEN-MOLECULE + 2-KETOGLUTARATE -> Nucleobases-in-DNA + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
