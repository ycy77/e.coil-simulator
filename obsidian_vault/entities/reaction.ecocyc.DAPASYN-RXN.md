---
entity_id: "reaction.ecocyc.DAPASYN-RXN"
entity_type: "reaction"
name: "DAPASYN-RXN"
source_database: "EcoCyc"
source_id: "DAPASYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "7,8-DIAMINO-PELARGONIC ACID AMINOTRANSFERASE"
  - "7,8-DIAMINONANOATE AMINOTRANSFERASE"
  - "DAPA AMINOTRANSFERASE"
---

# DAPASYN-RXN

`reaction.ecocyc.DAPASYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DAPASYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The second step in the biosynthesis of biotin. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 8-AMINO-7-OXONONANOATE -> S-ADENOSYL-4-METHYLTHIO-2-OXOBUTANOATE + DIAMINONONANOATE; direction=REVERSIBLE. The second step in the biosynthesis of biotin.

## Biological Role

Catalyzed by adenosylmethionine-8-amino-7-oxononanoate aminotransferase (complex.ecocyc.DAPASYN-CPLX). Substrates: S-Adenosyl-L-methionine (molecule.C00019), 8-Amino-7-oxononanoate (molecule.C01092). Products: 7,8-Diaminononanoate (molecule.C01037), S-adenosyl-4-methylsulfanyl-2-oxobutanoate (molecule.ecocyc.S-ADENOSYL-4-METHYLTHIO-2-OXOBUTANOATE).

## Enriched Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Annotation

The second step in the biosynthesis of biotin.

## Pathways

- `ecocyc.PWY0-1507` biotin biosynthesis from 8-amino-7-oxononanoate I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.DAPASYN-CPLX|complex.ecocyc.DAPASYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01037|molecule.C01037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.S-ADENOSYL-4-METHYLTHIO-2-OXOBUTANOATE|molecule.ecocyc.S-ADENOSYL-4-METHYLTHIO-2-OXOBUTANOATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01092|molecule.C01092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00147|molecule.C00147]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01092|molecule.C01092]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1481|molecule.ecocyc.CPD0-1481]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1482|molecule.ecocyc.CPD0-1482]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1483|molecule.ecocyc.CPD0-1483]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1484|molecule.ecocyc.CPD0-1484]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DAPASYN-RXN`

## Notes

S-ADENOSYLMETHIONINE + 8-AMINO-7-OXONONANOATE -> S-ADENOSYL-4-METHYLTHIO-2-OXOBUTANOATE + DIAMINONONANOATE; direction=REVERSIBLE
