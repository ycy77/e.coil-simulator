---
entity_id: "reaction.ecocyc.RXN0-1941"
entity_type: "reaction"
name: "RXN0-1941"
source_database: "EcoCyc"
source_id: "RXN0-1941"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1941

`reaction.ecocyc.RXN0-1941`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1941`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE + NADP -> ETHYL-2-METHYLACETOACETATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE + NADP -> ETHYL-2-METHYLACETOACETATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by dkgA (protein.Q46857). Substrates: NADP+ (molecule.C00006), ethyl-(2R)-methyl-(3S)-hydroxybutanoate (molecule.ecocyc.ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE). Products: NADPH (molecule.C00005), H+ (molecule.C00080), ethyl-2-methylacetoacetate (molecule.ecocyc.ETHYL-2-METHYLACETOACETATE).

## Annotation

ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE + NADP -> ETHYL-2-METHYLACETOACETATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.Q46857|protein.Q46857]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.ETHYL-2-METHYLACETOACETATE|molecule.ecocyc.ETHYL-2-METHYLACETOACETATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE|molecule.ecocyc.ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1941`

## Notes

ETHYL-2R-METHYL-3S-HYDROXYBUTANOATE + NADP -> ETHYL-2-METHYLACETOACETATE + NADPH + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
