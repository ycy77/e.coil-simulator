---
entity_id: "reaction.ecocyc.RXN0-2201"
entity_type: "reaction"
name: "RXN0-2201"
source_database: "EcoCyc"
source_id: "RXN0-2201"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2201

`reaction.ecocyc.RXN0-2201`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2201`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SER + NADP -> 2-AMINOMALONATE-SEMIALDEHYDE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SER + NADP -> 2-AMINOMALONATE-SEMIALDEHYDE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 3-hydroxy acid dehydrogenase YdfG (complex.ecocyc.CPLX0-1962). Substrates: NADP+ (molecule.C00006), L-Serine (molecule.C00065). Products: NADPH (molecule.C00005), H+ (molecule.C00080), 3-oxo-L-alanine (molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE).

## Annotation

SER + NADP -> 2-AMINOMALONATE-SEMIALDEHYDE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1962|complex.ecocyc.CPLX0-1962]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE|molecule.ecocyc.2-AMINOMALONATE-SEMIALDEHYDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2201`

## Notes

SER + NADP -> 2-AMINOMALONATE-SEMIALDEHYDE + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
