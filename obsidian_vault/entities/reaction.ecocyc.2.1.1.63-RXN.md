---
entity_id: "reaction.ecocyc.2.1.1.63-RXN"
entity_type: "reaction"
name: "2.1.1.63-RXN"
source_database: "EcoCyc"
source_id: "2.1.1.63-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "O-6-METHYLGUANINE-DNA-ALKYLTRANSFERASE"
  - "6-O-METHYLGUANINE-DNA METHYLTRANSFERASE"
---

# 2.1.1.63-RXN

`reaction.ecocyc.2.1.1.63-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.1.1.63-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROT-CYS + DNA-6-O-Methyl-Guanines -> Protein-S-methyl-L-cysteine + DNA-Guanines; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROT-CYS + DNA-6-O-Methyl-Guanines -> Protein-S-methyl-L-cysteine + DNA-Guanines; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ada (protein.P06134), ogt (protein.P0AFH0). Substrates: an O6-methylguanine in DNA (molecule.ecocyc.DNA-6-O-Methyl-Guanines), a [protein]-L-cysteine (molecule.ecocyc.PROT-CYS). Products: a guanine in DNA (molecule.ecocyc.DNA-Guanines), a [protein]-S-methyl-L-cysteine (molecule.ecocyc.Protein-S-methyl-L-cysteine).

## Annotation

PROT-CYS + DNA-6-O-Methyl-Guanines -> Protein-S-methyl-L-cysteine + DNA-Guanines; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P06134|protein.P06134]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFH0|protein.P0AFH0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.DNA-Guanines|molecule.ecocyc.DNA-Guanines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Protein-S-methyl-L-cysteine|molecule.ecocyc.Protein-S-methyl-L-cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-6-O-Methyl-Guanines|molecule.ecocyc.DNA-6-O-Methyl-Guanines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.PROT-CYS|molecule.ecocyc.PROT-CYS]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.1.1.63-RXN`

## Notes

PROT-CYS + DNA-6-O-Methyl-Guanines -> Protein-S-methyl-L-cysteine + DNA-Guanines; direction=PHYSIOL-LEFT-TO-RIGHT
