---
entity_id: "reaction.ecocyc.RXN-17651"
entity_type: "reaction"
name: "RXN-17651"
source_database: "EcoCyc"
source_id: "RXN-17651"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17651

`reaction.ecocyc.RXN-17651`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17651`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-methionine-S-S-oxides + E- + PROTON -> Protein-L-methionine + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: Protein-L-methionine-S-S-oxides + E- + PROTON -> Protein-L-methionine + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a protein-L-methionine-(S)-S-oxide (molecule.ecocyc.Protein-L-methionine-S-S-oxides). Products: H2O (molecule.C00001), a [protein]-L-methionine (molecule.ecocyc.Protein-L-methionine).

## Annotation

Protein-L-methionine-S-S-oxides + E- + PROTON -> Protein-L-methionine + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-L-methionine|molecule.ecocyc.Protein-L-methionine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-L-methionine-S-S-oxides|molecule.ecocyc.Protein-L-methionine-S-S-oxides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17651`

## Notes

Protein-L-methionine-S-S-oxides + E- + PROTON -> Protein-L-methionine + WATER; direction=LEFT-TO-RIGHT
