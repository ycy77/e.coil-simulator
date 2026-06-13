---
entity_id: "reaction.ecocyc.LEUCYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "LEUCYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "LEUCYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# LEUCYLTRANSFERASE-RXN

`reaction.ecocyc.LEUCYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:LEUCYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction can also catalyze the addition of phenylalanine instead of leucine. Addition of either leucine or phenylalanine requires an arginine, histidine or lysine at the amino-terminus of the protein that is to be modified. EcoCyc reaction equation: Charged-LEU-tRNAs + Protein-N-terminal-L-Lysine -> L-leucyl-L-lysyl-Protein + LEU-tRNAs + PROTON; direction=LEFT-TO-RIGHT. This reaction can also catalyze the addition of phenylalanine instead of leucine. Addition of either leucine or phenylalanine requires an arginine, histidine or lysine at the amino-terminus of the protein that is to be modified.

## Biological Role

Catalyzed by aat (protein.P0A8P1). Substrates: an N-terminal L-lysyl-[protein] (molecule.ecocyc.Protein-N-terminal-L-Lysine). Products: H+ (molecule.C00080), a [protein] N-terminal L-leucyl-L-lysine (molecule.ecocyc.L-leucyl-L-lysyl-Protein).

## Enriched Pathways

- `ecocyc.PWY-7801` N-end rule pathway I (prokaryotic) (EcoCyc)

## Annotation

This reaction can also catalyze the addition of phenylalanine instead of leucine. Addition of either leucine or phenylalanine requires an arginine, histidine or lysine at the amino-terminus of the protein that is to be modified.

## Pathways

- `ecocyc.PWY-7801` N-end rule pathway I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0A8P1|protein.P0A8P1]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-leucyl-L-lysyl-Protein|molecule.ecocyc.L-leucyl-L-lysyl-Protein]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-N-terminal-L-Lysine|molecule.ecocyc.Protein-N-terminal-L-Lysine]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:LEUCYLTRANSFERASE-RXN`

## Notes

Charged-LEU-tRNAs + Protein-N-terminal-L-Lysine -> L-leucyl-L-lysyl-Protein + LEU-tRNAs + PROTON; direction=LEFT-TO-RIGHT
