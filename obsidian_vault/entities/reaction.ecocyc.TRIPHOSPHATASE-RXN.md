---
entity_id: "reaction.ecocyc.TRIPHOSPHATASE-RXN"
entity_type: "reaction"
name: "TRIPHOSPHATASE-RXN"
source_database: "EcoCyc"
source_id: "TRIPHOSPHATASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC|CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRIPHOSPHATASE-RXN

`reaction.ecocyc.TRIPHOSPHATASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRIPHOSPHATASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC|CCO-CYTOSOL

## Enriched Summary

WATER + P3I -> PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + P3I -> PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by alkaline phosphatase (complex.ecocyc.ALKAPHOSPHA-CPLX), inorganic pyrophosphatase (complex.ecocyc.CPLX0-243), ygiF (protein.P30871). Substrates: H2O (molecule.C00001), Triphosphate (molecule.C00536). Products: Diphosphate (molecule.C00013), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + P3I -> PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ALKAPHOSPHA-CPLX|complex.ecocyc.ALKAPHOSPHA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-243|complex.ecocyc.CPLX0-243]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30871|protein.P30871]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00536|molecule.C00536]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRIPHOSPHATASE-RXN`

## Notes

WATER + P3I -> PPI + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
