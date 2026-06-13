---
entity_id: "reaction.ecocyc.RXN-17823"
entity_type: "reaction"
name: "RXN-17823"
source_database: "EcoCyc"
source_id: "RXN-17823"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17823

`reaction.ecocyc.RXN-17823`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17823`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

a-DNA-methyl-phosphotriester + PROT-CYS -> DNA-N + Protein-S-methyl-L-cysteine + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: a-DNA-methyl-phosphotriester + PROT-CYS -> DNA-N + Protein-S-methyl-L-cysteine + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ada (protein.P06134). Substrates: a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS). Products: H+ (molecule.C00080), a [protein]-S-methyl-L-cysteine (molecule.ecocyc.Protein-S-methyl-L-cysteine).

## Annotation

a-DNA-methyl-phosphotriester + PROT-CYS -> DNA-N + Protein-S-methyl-L-cysteine + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P06134|protein.P06134]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-S-methyl-L-cysteine|molecule.ecocyc.Protein-S-methyl-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17823`

## Notes

a-DNA-methyl-phosphotriester + PROT-CYS -> DNA-N + Protein-S-methyl-L-cysteine + PROTON; direction=LEFT-TO-RIGHT
