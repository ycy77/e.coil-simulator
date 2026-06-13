---
entity_id: "reaction.ecocyc.RXN-14992"
entity_type: "reaction"
name: "RXN-14992"
source_database: "EcoCyc"
source_id: "RXN-14992"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14992

`reaction.ecocyc.RXN-14992`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14992`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Release-factor-L-glutamine -> Release-factor-N5-Methyl-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Release-factor-L-glutamine -> Release-factor-N5-Methyl-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by prmC (protein.P0ACC1). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [release factor]-L-glutamine (molecule.ecocyc.Release-factor-L-glutamine). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a [release factor]-N5-methyl-L-glutamine (molecule.ecocyc.Release-factor-N5-Methyl-L-glutamine).

## Annotation

S-ADENOSYLMETHIONINE + Release-factor-L-glutamine -> Release-factor-N5-Methyl-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0ACC1|protein.P0ACC1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Release-factor-N5-Methyl-L-glutamine|molecule.ecocyc.Release-factor-N5-Methyl-L-glutamine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Release-factor-L-glutamine|molecule.ecocyc.Release-factor-L-glutamine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-14992`

## Notes

S-ADENOSYLMETHIONINE + Release-factor-L-glutamine -> Release-factor-N5-Methyl-L-glutamine + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
