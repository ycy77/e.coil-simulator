---
entity_id: "reaction.ecocyc.R4-RXN"
entity_type: "reaction"
name: "R4-RXN"
source_database: "EcoCyc"
source_id: "R4-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# R4-RXN

`reaction.ecocyc.R4-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:R4-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction converts hydroperoxides of lipids or nucleic acids to their corresponding alcohols. The reaction equation employs the generic ROOH and ROH to represent the specific substrates. EcoCyc reaction equation: Alkyl-Hydro-Peroxides + NADH + PROTON -> Alcohols + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction converts hydroperoxides of lipids or nucleic acids to their corresponding alcohols. The reaction equation employs the generic ROOH and ROH to represent the specific substrates.

## Biological Role

Catalyzed by alkyl hydroperoxide reductase (complex.ecocyc.CPLX0-245). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), an organic hydroperoxide (molecule.ecocyc.Alkyl-Hydro-Peroxides). Products: H2O (molecule.C00001), NAD+ (molecule.C00003), an alcohol (molecule.ecocyc.Alcohols).

## Annotation

This reaction converts hydroperoxides of lipids or nucleic acids to their corresponding alcohols. The reaction equation employs the generic ROOH and ROH to represent the specific substrates.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.ecocyc.NH42SO4|molecule.ecocyc.NH42SO4]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-245|complex.ecocyc.CPLX0-245]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Alcohols|molecule.ecocyc.Alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Alkyl-Hydro-Peroxides|molecule.ecocyc.Alkyl-Hydro-Peroxides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:R4-RXN`

## Notes

Alkyl-Hydro-Peroxides + NADH + PROTON -> Alcohols + WATER + NAD; direction=PHYSIOL-LEFT-TO-RIGHT
