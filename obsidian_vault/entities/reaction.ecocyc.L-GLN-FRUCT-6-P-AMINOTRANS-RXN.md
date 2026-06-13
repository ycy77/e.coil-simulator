---
entity_id: "reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN"
entity_type: "reaction"
name: "L-GLN-FRUCT-6-P-AMINOTRANS-RXN"
source_database: "EcoCyc"
source_id: "L-GLN-FRUCT-6-P-AMINOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-GLN-FRUCT-6-P-AMINOTRANS-RXN

`reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:L-GLN-FRUCT-6-P-AMINOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in hexosamine biosynthesis. EcoCyc reaction equation: FRUCTOSE-6P + GLN -> D-GLUCOSAMINE-6-P + GLT; direction=REVERSIBLE. This is the first reaction in hexosamine biosynthesis.

## Biological Role

Catalyzed by L-glutamine—D-fructose-6-phosphate aminotransferase (complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX). Substrates: L-Glutamine (molecule.C00064), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P). Products: L-Glutamate (molecule.C00025), D-Glucosamine 6-phosphate (molecule.C00352).

## Enriched Pathways

- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Annotation

This is the first reaction in hexosamine biosynthesis.

## Pathways

- `ecocyc.UDPNAGSYN-PWY` UDP-N-acetyl-D-glucosamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX|complex.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01165|molecule.C01165]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C03273|molecule.C03273]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9051|molecule.ecocyc.CPD-9051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1235|molecule.ecocyc.CPD0-1235]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1236|molecule.ecocyc.CPD0-1236]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1237|molecule.ecocyc.CPD0-1237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1627|molecule.ecocyc.CPD0-1627]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DIETHYLPYROCARBONATE|molecule.ecocyc.DIETHYLPYROCARBONATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:L-GLN-FRUCT-6-P-AMINOTRANS-RXN`

## Notes

FRUCTOSE-6P + GLN -> D-GLUCOSAMINE-6-P + GLT; direction=REVERSIBLE
