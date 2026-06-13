---
entity_id: "reaction.ecocyc.RXN-17920"
entity_type: "reaction"
name: "RXN-17920"
source_database: "EcoCyc"
source_id: "RXN-17920"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17920

`reaction.ecocyc.RXN-17920`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17920`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

NAD + DNA-Ligase-L-lysine -> DNA-Ligase-L-lysine-adenylate + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: NAD + DNA-Ligase-L-lysine -> DNA-Ligase-L-lysine-adenylate + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: NAD+ (molecule.C00003), a [DNA ligase]-L-lysine (molecule.ecocyc.DNA-Ligase-L-lysine). Products: H+ (molecule.C00080), Nicotinamide D-ribonucleotide (molecule.C00455), a [DNA ligase]-N6-(5'-adenylyl)-L-lysine (molecule.ecocyc.DNA-Ligase-L-lysine-adenylate).

## Annotation

NAD + DNA-Ligase-L-lysine -> DNA-Ligase-L-lysine-adenylate + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00455|molecule.C00455]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DNA-Ligase-L-lysine-adenylate|molecule.ecocyc.DNA-Ligase-L-lysine-adenylate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-Ligase-L-lysine|molecule.ecocyc.DNA-Ligase-L-lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17920`

## Notes

NAD + DNA-Ligase-L-lysine -> DNA-Ligase-L-lysine-adenylate + NICOTINAMIDE_NUCLEOTIDE + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
