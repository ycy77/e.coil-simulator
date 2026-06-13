---
entity_id: "reaction.ecocyc.RXN-17824"
entity_type: "reaction"
name: "RXN-17824"
source_database: "EcoCyc"
source_id: "RXN-17824"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17824

`reaction.ecocyc.RXN-17824`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17824`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-19186 + PROT-CYS -> a-thymine-in-DNA + Protein-S-methyl-L-cysteine; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-19186 + PROT-CYS -> a-thymine-in-DNA + Protein-S-methyl-L-cysteine; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ada (protein.P06134), ogt (protein.P0AFH0). Substrates: an O4-methylthymine in DNA (molecule.ecocyc.CPD-19186), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS). Products: a [protein]-S-methyl-L-cysteine (molecule.ecocyc.Protein-S-methyl-L-cysteine), a thymine in DNA (molecule.ecocyc.a-thymine-in-DNA).

## Annotation

CPD-19186 + PROT-CYS -> a-thymine-in-DNA + Protein-S-methyl-L-cysteine; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06134|protein.P06134]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFH0|protein.P0AFH0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Protein-S-methyl-L-cysteine|molecule.ecocyc.Protein-S-methyl-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.a-thymine-in-DNA|molecule.ecocyc.a-thymine-in-DNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-19186|molecule.ecocyc.CPD-19186]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17824`

## Notes

CPD-19186 + PROT-CYS -> a-thymine-in-DNA + Protein-S-methyl-L-cysteine; direction=LEFT-TO-RIGHT
