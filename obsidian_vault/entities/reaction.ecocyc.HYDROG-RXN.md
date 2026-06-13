---
entity_id: "reaction.ecocyc.HYDROG-RXN"
entity_type: "reaction"
name: "hydrogenase"
source_database: "EcoCyc"
source_id: "HYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# hydrogenase

`reaction.ecocyc.HYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYDROGEN-MOLECULE + Oxidized-ferredoxins -> Reduced-ferredoxins + PROTON; direction=REVERSIBLE EcoCyc reaction equation: HYDROGEN-MOLECULE + Oxidized-ferredoxins -> Reduced-ferredoxins + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX). Substrates: Hydrogen (molecule.C00282). Products: H+ (molecule.C00080).

## Annotation

HYDROGEN-MOLECULE + Oxidized-ferredoxins -> Reduced-ferredoxins + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00282|molecule.C00282]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HYDROG-RXN`

## Notes

HYDROGEN-MOLECULE + Oxidized-ferredoxins -> Reduced-ferredoxins + PROTON; direction=REVERSIBLE
