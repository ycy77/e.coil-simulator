---
entity_id: "reaction.ecocyc.RXN0-7198"
entity_type: "reaction"
name: "RXN0-7198"
source_database: "EcoCyc"
source_id: "RXN0-7198"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7198

`reaction.ecocyc.RXN0-7198`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7198`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated. EcoCyc reaction equation: PRECURSOR-Z + MoeB-YnjE-acyl-disulfide + Reduced-ferredoxins + WATER + PROTON -> CPD-4 + YnjE-Proteins + MPT-Synthases + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Biological Role

Substrates: H2O (molecule.C00001), H+ (molecule.C00080), cyclic pyranopterin phosphate (molecule.ecocyc.PRECURSOR-Z). Products: Molybdopterin (molecule.C05924).

## Annotation

This is the second part of the multistep synthesis of the thiazole moiety of thiamin. Not all of the individual reactions and enzymes have been delineated.

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C05924|molecule.C05924]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PRECURSOR-Z|molecule.ecocyc.PRECURSOR-Z]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7198`

## Notes

PRECURSOR-Z + MoeB-YnjE-acyl-disulfide + Reduced-ferredoxins + WATER + PROTON -> CPD-4 + YnjE-Proteins + MPT-Synthases + Oxidized-ferredoxins; direction=PHYSIOL-LEFT-TO-RIGHT
