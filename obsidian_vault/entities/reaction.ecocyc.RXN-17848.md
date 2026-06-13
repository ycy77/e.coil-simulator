---
entity_id: "reaction.ecocyc.RXN-17848"
entity_type: "reaction"
name: "RXN-17848"
source_database: "EcoCyc"
source_id: "RXN-17848"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17848

`reaction.ecocyc.RXN-17848`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17848`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Charged-PHE-tRNAs + Protein-N-terminal-L-Lysine -> L-phenylalanyl-L-lysyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Charged-PHE-tRNAs + Protein-N-terminal-L-Lysine -> L-phenylalanyl-L-lysyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aat (protein.P0A8P1). Substrates: an N-terminal L-lysyl-[protein] (molecule.ecocyc.Protein-N-terminal-L-Lysine). Products: H+ (molecule.C00080), L-phenylalanyl-L-lysyl-[protein] (molecule.ecocyc.L-phenylalanyl-L-lysyl-Protein).

## Annotation

Charged-PHE-tRNAs + Protein-N-terminal-L-Lysine -> L-phenylalanyl-L-lysyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A8P1|protein.P0A8P1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-phenylalanyl-L-lysyl-Protein|molecule.ecocyc.L-phenylalanyl-L-lysyl-Protein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-N-terminal-L-Lysine|molecule.ecocyc.Protein-N-terminal-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17848`

## Notes

Charged-PHE-tRNAs + Protein-N-terminal-L-Lysine -> L-phenylalanyl-L-lysyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
