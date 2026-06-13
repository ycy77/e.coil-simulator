---
entity_id: "reaction.ecocyc.RXN-6423"
entity_type: "reaction"
name: "RXN-6423"
source_database: "EcoCyc"
source_id: "RXN-6423"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6423

`reaction.ecocyc.RXN-6423`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6423`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

4-aminobutanal exists in equilibrium with the cyclic compound 1-pyrroline and can be interconverted spontaneously . EcoCyc reaction equation: 4-AMINO-BUTYRALDEHYDE -> CPD-6124 + WATER; direction=REVERSIBLE. 4-aminobutanal exists in equilibrium with the cyclic compound 1-pyrroline and can be interconverted spontaneously .

## Biological Role

Substrates: 4-Aminobutyraldehyde (molecule.C00555). Products: H2O (molecule.C00001), 1-pyrroline (molecule.ecocyc.CPD-6124).

## Enriched Pathways

- `ecocyc.ORNDEG-PWY` superpathway of ornithine degradation (EcoCyc)

## Annotation

4-aminobutanal exists in equilibrium with the cyclic compound 1-pyrroline and can be interconverted spontaneously .

## Pathways

- `ecocyc.ORNDEG-PWY` superpathway of ornithine degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-6124|molecule.ecocyc.CPD-6124]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00555|molecule.C00555]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-6423`

## Notes

4-AMINO-BUTYRALDEHYDE -> CPD-6124 + WATER; direction=REVERSIBLE
