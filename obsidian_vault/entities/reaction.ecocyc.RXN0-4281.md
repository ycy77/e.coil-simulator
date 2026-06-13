---
entity_id: "reaction.ecocyc.RXN0-4281"
entity_type: "reaction"
name: "RXN0-4281"
source_database: "EcoCyc"
source_id: "RXN0-4281"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4281

`reaction.ecocyc.RXN0-4281`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4281`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETOL + NADP -> PROTON + METHYL-GLYOXAL + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ACETOL + NADP -> PROTON + METHYL-GLYOXAL + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by NADPH-dependent aldehyde reductase YqhD (complex.ecocyc.CPLX0-7667), dkgB (protein.P30863), yeaE (protein.P76234), gpr (protein.Q46851), dkgA (protein.Q46857). Substrates: NADP+ (molecule.C00006), Hydroxyacetone (molecule.C05235). Products: NADPH (molecule.C00005), H+ (molecule.C00080), Methylglyoxal (molecule.C00546).

## Enriched Pathways

- `ecocyc.PWY-5453` methylglyoxal degradation III (EcoCyc)

## Annotation

ACETOL + NADP -> PROTON + METHYL-GLYOXAL + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.PWY-5453` methylglyoxal degradation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7667|complex.ecocyc.CPLX0-7667]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P30863|protein.P30863]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76234|protein.P76234]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46851|protein.Q46851]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.Q46857|protein.Q46857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00546|molecule.C00546]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05235|molecule.C05235]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-4281`

## Notes

ACETOL + NADP -> PROTON + METHYL-GLYOXAL + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
