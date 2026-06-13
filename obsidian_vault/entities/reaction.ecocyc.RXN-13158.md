---
entity_id: "reaction.ecocyc.RXN-13158"
entity_type: "reaction"
name: "RXN-13158"
source_database: "EcoCyc"
source_id: "RXN-13158"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-13158

`reaction.ecocyc.RXN-13158`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-13158`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-isopropylmalate dehydrogenase (complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX), dmlA (protein.P76251). Substrates: NAD+ (molecule.C00003), (2R,3S)-3-Isopropylmalate (molecule.C04411). Products: NADH (molecule.C00004), CO2 (molecule.C00011), 4-Methyl-2-oxopentanoate (molecule.C00233).

## Annotation

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX|complex.ecocyc.3-ISOPROPYLMALDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76251|protein.P76251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00233|molecule.C00233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04411|molecule.C04411]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-13158`

## Notes

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> 2K-4CH3-PENTANOATE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
