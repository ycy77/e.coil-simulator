---
entity_id: "reaction.ecocyc.RXN-17847"
entity_type: "reaction"
name: "RXN-17847"
source_database: "EcoCyc"
source_id: "RXN-17847"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17847

`reaction.ecocyc.RXN-17847`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17847`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Charged-PHE-tRNAs + Protein-N-terminal-L-Arginine -> L-phenylalanyl-L-arginyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Charged-PHE-tRNAs + Protein-N-terminal-L-Arginine -> L-phenylalanyl-L-arginyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aat (protein.P0A8P1). Substrates: an N-terminal arginyl-[protein] (molecule.ecocyc.Protein-N-terminal-L-Arginine). Products: H+ (molecule.C00080), L-phenylalanyl-L-arginyl-[protein] (molecule.ecocyc.L-phenylalanyl-L-arginyl-Protein).

## Annotation

Charged-PHE-tRNAs + Protein-N-terminal-L-Arginine -> L-phenylalanyl-L-arginyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A8P1|protein.P0A8P1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-phenylalanyl-L-arginyl-Protein|molecule.ecocyc.L-phenylalanyl-L-arginyl-Protein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-N-terminal-L-Arginine|molecule.ecocyc.Protein-N-terminal-L-Arginine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17847`

## Notes

Charged-PHE-tRNAs + Protein-N-terminal-L-Arginine -> L-phenylalanyl-L-arginyl-Protein + PHE-tRNAs + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
