---
entity_id: "reaction.ecocyc.RXN0-6992"
entity_type: "reaction"
name: "RXN0-6992"
source_database: "EcoCyc"
source_id: "RXN0-6992"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6992

`reaction.ecocyc.RXN0-6992`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6992`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

The oxidation of D-cysteine to D-cystine is predicted to occur in the oxidising environment of the periplasm. A similar reaction has been reported for the optical isomer L-cysteine . EcoCyc reaction equation: MONOMER0-4152 + D-CYSTEINE -> CPD0-1564 + DISULFOXRED-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT. The oxidation of D-cysteine to D-cystine is predicted to occur in the oxidising environment of the periplasm. A similar reaction has been reported for the optical isomer L-cysteine .

## Biological Role

Substrates: D-Cysteine (molecule.C00793). Products: D-cystine (molecule.ecocyc.CPD0-1564).

## Annotation

The oxidation of D-cysteine to D-cystine is predicted to occur in the oxidising environment of the periplasm. A similar reaction has been reported for the optical isomer L-cysteine .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.ecocyc.CPD0-1564|molecule.ecocyc.CPD0-1564]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00793|molecule.C00793]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6992`

## Notes

MONOMER0-4152 + D-CYSTEINE -> CPD0-1564 + DISULFOXRED-MONOMER; direction=PHYSIOL-LEFT-TO-RIGHT
