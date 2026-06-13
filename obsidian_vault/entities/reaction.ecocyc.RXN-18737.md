---
entity_id: "reaction.ecocyc.RXN-18737"
entity_type: "reaction"
name: "RXN-18737"
source_database: "EcoCyc"
source_id: "RXN-18737"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18737

`reaction.ecocyc.RXN-18737`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18737`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

an-Nsup1sup-methyladenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: an-Nsup1sup-methyladenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), an N1-methyladenine in DNA (molecule.ecocyc.an-Nsup1sup-methyladenine-in-DNA). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), an adenine in DNA (molecule.ecocyc.DNA-Adenines).

## Annotation

an-Nsup1sup-methyladenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Adenines|molecule.ecocyc.DNA-Adenines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.an-Nsup1sup-methyladenine-in-DNA|molecule.ecocyc.an-Nsup1sup-methyladenine-in-DNA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00389|molecule.C00389]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1231|molecule.ecocyc.CPD0-1231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-18737`

## Notes

an-Nsup1sup-methyladenine-in-DNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> DNA-Adenines + CARBON-DIOXIDE + FORMALDEHYDE + SUC; direction=PHYSIOL-LEFT-TO-RIGHT
