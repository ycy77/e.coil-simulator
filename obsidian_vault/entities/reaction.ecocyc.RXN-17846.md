---
entity_id: "reaction.ecocyc.RXN-17846"
entity_type: "reaction"
name: "RXN-17846"
source_database: "EcoCyc"
source_id: "RXN-17846"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17846

`reaction.ecocyc.RXN-17846`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17846`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Charged-LEU-tRNAs + Protein-N-terminal-L-Arginine -> L-leucyl-L-arginyl-Protein + LEU-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Charged-LEU-tRNAs + Protein-N-terminal-L-Arginine -> L-leucyl-L-arginyl-Protein + LEU-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aat (protein.P0A8P1). Substrates: an N-terminal arginyl-[protein] (molecule.ecocyc.Protein-N-terminal-L-Arginine). Products: H+ (molecule.C00080), a [protein] N-terminal L-leucyl-L-arginine (molecule.ecocyc.L-leucyl-L-arginyl-Protein).

## Enriched Pathways

- `ecocyc.PWY-7801` N-end rule pathway I (prokaryotic) (EcoCyc)

## Annotation

Charged-LEU-tRNAs + Protein-N-terminal-L-Arginine -> L-leucyl-L-arginyl-Protein + LEU-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7801` N-end rule pathway I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A8P1|protein.P0A8P1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-leucyl-L-arginyl-Protein|molecule.ecocyc.L-leucyl-L-arginyl-Protein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-N-terminal-L-Arginine|molecule.ecocyc.Protein-N-terminal-L-Arginine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17846`

## Notes

Charged-LEU-tRNAs + Protein-N-terminal-L-Arginine -> L-leucyl-L-arginyl-Protein + LEU-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
