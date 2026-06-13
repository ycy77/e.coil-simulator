---
entity_id: "reaction.ecocyc.RXN-25385"
entity_type: "reaction"
name: "peptidyl-lysine N-lactoyltransferase"
source_database: "EcoCyc"
source_id: "RXN-25385"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "peptidyl-lysine N-lactyltransferase"
---

# peptidyl-lysine N-lactoyltransferase

`reaction.ecocyc.RXN-25385`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-25385`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-lysine + LACTOYL-COA -> PROTEIN-N6-LACTOYL-L-LYSINES + CO-A + PROTON; direction=REVERSIBLE EcoCyc reaction equation: Protein-L-lysine + LACTOYL-COA -> PROTEIN-N6-LACTOYL-L-LYSINES + CO-A + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by yiaC (protein.P37664). Substrates: Protein lysine (molecule.C02188), (S)-lactoyl-CoA (molecule.ecocyc.LACTOYL-COA). Products: CoA (molecule.C00010), H+ (molecule.C00080), a [protein]-N6-(S)-lactoyl-L-lysine (molecule.ecocyc.PROTEIN-N6-LACTOYL-L-LYSINES).

## Annotation

Protein-L-lysine + LACTOYL-COA -> PROTEIN-N6-LACTOYL-L-LYSINES + CO-A + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37664|protein.P37664]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-N6-LACTOYL-L-LYSINES|molecule.ecocyc.PROTEIN-N6-LACTOYL-L-LYSINES]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.LACTOYL-COA|molecule.ecocyc.LACTOYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-25385`

## Notes

Protein-L-lysine + LACTOYL-COA -> PROTEIN-N6-LACTOYL-L-LYSINES + CO-A + PROTON; direction=REVERSIBLE
