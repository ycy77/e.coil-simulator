---
entity_id: "reaction.ecocyc.RXN-21235"
entity_type: "reaction"
name: "RXN-21235"
source_database: "EcoCyc"
source_id: "RXN-21235"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21235

`reaction.ecocyc.RXN-21235`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21235`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N3-METHYLCYTOSINE-RNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> RNA-Cytosines + CARBON-DIOXIDE + FORMALDEHYDE + SUC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N3-METHYLCYTOSINE-RNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> RNA-Cytosines + CARBON-DIOXIDE + FORMALDEHYDE + SUC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkB (protein.P05050). Substrates: Oxygen (molecule.C00007), 2-Oxoglutarate (molecule.C00026), an N3-methylcytosine in RNA (molecule.ecocyc.N3-METHYLCYTOSINE-RNA). Products: CO2 (molecule.C00011), Succinate (molecule.C00042), Formaldehyde (molecule.C00067), H+ (molecule.C00080), a cytosine in RNA (molecule.ecocyc.RNA-Cytosines).

## Annotation

N3-METHYLCYTOSINE-RNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> RNA-Cytosines + CARBON-DIOXIDE + FORMALDEHYDE + SUC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P05050|protein.P05050]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00042|molecule.C00042]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.RNA-Cytosines|molecule.ecocyc.RNA-Cytosines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N3-METHYLCYTOSINE-RNA|molecule.ecocyc.N3-METHYLCYTOSINE-RNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21235`

## Notes

N3-METHYLCYTOSINE-RNA + 2-KETOGLUTARATE + OXYGEN-MOLECULE -> RNA-Cytosines + CARBON-DIOXIDE + FORMALDEHYDE + SUC + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
