---
entity_id: "reaction.ecocyc.CHER-RXN"
entity_type: "reaction"
name: "CHER-RXN"
source_database: "EcoCyc"
source_id: "CHER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHER-RXN

`reaction.ecocyc.CHER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

In this reaction the methyl-accepting chemotaxis proteins (MCPs) undergo methylation. The level of MCP methylation determines the activity of the signaling domain. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Protein-alpha-L-Glutamates -> protein-L-glutamate-O4-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. In this reaction the methyl-accepting chemotaxis proteins (MCPs) undergo methylation. The level of MCP methylation determines the activity of the signaling domain.

## Biological Role

Catalyzed by cheR (protein.P07364). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [protein]-α-L-glutamate (molecule.ecocyc.Protein-alpha-L-Glutamates). Products: S-Adenosyl-L-homocysteine (molecule.C00021), a [protein]-L-glutamate-O5-methyl-ester (molecule.ecocyc.protein-L-glutamate-O4-methyl-ester).

## Annotation

In this reaction the methyl-accepting chemotaxis proteins (MCPs) undergo methylation. The level of MCP methylation determines the activity of the signaling domain.

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07364|protein.P07364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.protein-L-glutamate-O4-methyl-ester|molecule.ecocyc.protein-L-glutamate-O4-methyl-ester]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Protein-alpha-L-Glutamates|molecule.ecocyc.Protein-alpha-L-Glutamates]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CHER-RXN`

## Notes

S-ADENOSYLMETHIONINE + Protein-alpha-L-Glutamates -> protein-L-glutamate-O4-methyl-ester + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
