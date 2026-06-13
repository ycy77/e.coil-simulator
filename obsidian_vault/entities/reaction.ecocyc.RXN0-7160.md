---
entity_id: "reaction.ecocyc.RXN0-7160"
entity_type: "reaction"
name: "RXN0-7160"
source_database: "EcoCyc"
source_id: "RXN0-7160"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7160

`reaction.ecocyc.RXN0-7160`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7160`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Protein-L-lysine + ACETYL-COA -> CPD3O-0 + CO-A + PROTON; direction=REVERSIBLE EcoCyc reaction equation: Protein-L-lysine + ACETYL-COA -> CPD3O-0 + CO-A + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by peptidyl-lysine N-acetyltransferase (complex.ecocyc.CPLX0-8189), yjaB (protein.P09163), rimI (protein.P0A944), phnO (protein.P16691), yiaC (protein.P37664). Substrates: Acetyl-CoA (molecule.C00024), Protein lysine (molecule.C02188). Products: CoA (molecule.C00010), H+ (molecule.C00080), a [protein]-N6-acetyl-L-lysine (molecule.ecocyc.CPD3O-0).

## Annotation

Protein-L-lysine + ACETYL-COA -> CPD3O-0 + CO-A + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8189|complex.ecocyc.CPLX0-8189]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P09163|protein.P09163]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0A944|protein.P0A944]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P16691|protein.P16691]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37664|protein.P37664]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD3O-0|molecule.ecocyc.CPD3O-0]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02188|molecule.C02188]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7160`

## Notes

Protein-L-lysine + ACETYL-COA -> CPD3O-0 + CO-A + PROTON; direction=REVERSIBLE
