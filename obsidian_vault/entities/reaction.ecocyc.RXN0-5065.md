---
entity_id: "reaction.ecocyc.RXN0-5065"
entity_type: "reaction"
name: "RXN0-5065"
source_database: "EcoCyc"
source_id: "RXN0-5065"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5065

`reaction.ecocyc.RXN0-5065`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5065`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

34-DIHYDROXYPHENYLACETYL-COA + WATER -> CPD-782 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 34-DIHYDROXYPHENYLACETYL-COA + WATER -> CPD-782 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by phenylacetyl-CoA thioesterase (complex.ecocyc.CPLX0-3941). Substrates: H2O (molecule.C00001), 3,4-dihydroxyphenylacetyl-CoA (molecule.ecocyc.34-DIHYDROXYPHENYLACETYL-COA). Products: CoA (molecule.C00010), H+ (molecule.C00080), 3,4-Dihydroxyphenylacetate (molecule.C01161).

## Annotation

34-DIHYDROXYPHENYLACETYL-COA + WATER -> CPD-782 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3941|complex.ecocyc.CPLX0-3941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01161|molecule.C01161]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.34-DIHYDROXYPHENYLACETYL-COA|molecule.ecocyc.34-DIHYDROXYPHENYLACETYL-COA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5065`

## Notes

34-DIHYDROXYPHENYLACETYL-COA + WATER -> CPD-782 + CO-A + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
