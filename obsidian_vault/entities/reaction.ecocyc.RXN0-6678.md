---
entity_id: "reaction.ecocyc.RXN0-6678"
entity_type: "reaction"
name: "RXN0-6678"
source_database: "EcoCyc"
source_id: "RXN0-6678"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6678

`reaction.ecocyc.RXN0-6678`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6678`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-Oxo-carboxylates + AMMONIUM + E- + PROTON -> D-Amino-Acids + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-Oxo-carboxylates + AMMONIUM + E- + PROTON -> D-Amino-Acids + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a 2-oxo carboxylate (molecule.ecocyc.2-Oxo-carboxylates), ammonium (molecule.ecocyc.AMMONIUM). Products: H2O (molecule.C00001), a D-amino acid (molecule.ecocyc.D-Amino-Acids).

## Annotation

2-Oxo-carboxylates + AMMONIUM + E- + PROTON -> D-Amino-Acids + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.D-Amino-Acids|molecule.ecocyc.D-Amino-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-Oxo-carboxylates|molecule.ecocyc.2-Oxo-carboxylates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6678`

## Notes

2-Oxo-carboxylates + AMMONIUM + E- + PROTON -> D-Amino-Acids + WATER; direction=LEFT-TO-RIGHT
