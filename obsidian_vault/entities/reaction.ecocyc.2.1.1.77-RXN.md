---
entity_id: "reaction.ecocyc.2.1.1.77-RXN"
entity_type: "reaction"
name: "2.1.1.77-RXN"
source_database: "EcoCyc"
source_id: "2.1.1.77-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PROTEIN &beta"
  - "-ASPARTATE O-METHYLTRANSFERASE"
  - "PROTEIN D-ASPARTATE METHYLTRANSFERASE"
  - "PROTEIN L-ISOASPARTYL METHYLTRANSFERASE"
---

# 2.1.1.77-RXN

`reaction.ecocyc.2.1.1.77-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.1.1.77-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-ASPARTATE (BUT NOT L-ASPARTATE) RESIDUES IN PROTEINS CAN ALSO ACT AS ACCEPTORS. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + PROTEIN-L-BETA-ISOASPARTATES -> ADENOSYL-HOMO-CYS + PROTEIN-L-BETA-ISOSPARTATE-METHYL-ESTERS; direction=PHYSIOL-LEFT-TO-RIGHT. D-ASPARTATE (BUT NOT L-ASPARTATE) RESIDUES IN PROTEINS CAN ALSO ACT AS ACCEPTORS.

## Biological Role

Catalyzed by pcm (protein.P0A7A5). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a [protein]-L-β-isoaspartate (molecule.ecocyc.PROTEIN-L-BETA-ISOASPARTATES). Products: S-Adenosyl-L-homocysteine (molecule.C00021), a protein L-β-isoaspartate α-methyl ester (molecule.ecocyc.PROTEIN-L-BETA-ISOSPARTATE-METHYL-ESTERS).

## Annotation

D-ASPARTATE (BUT NOT L-ASPARTATE) RESIDUES IN PROTEINS CAN ALSO ACT AS ACCEPTORS.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7A5|protein.P0A7A5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.PROTEIN-L-BETA-ISOSPARTATE-METHYL-ESTERS|molecule.ecocyc.PROTEIN-L-BETA-ISOSPARTATE-METHYL-ESTERS]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROTEIN-L-BETA-ISOASPARTATES|molecule.ecocyc.PROTEIN-L-BETA-ISOASPARTATES]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.1.1.77-RXN`

## Notes

S-ADENOSYLMETHIONINE + PROTEIN-L-BETA-ISOASPARTATES -> ADENOSYL-HOMO-CYS + PROTEIN-L-BETA-ISOSPARTATE-METHYL-ESTERS; direction=PHYSIOL-LEFT-TO-RIGHT
