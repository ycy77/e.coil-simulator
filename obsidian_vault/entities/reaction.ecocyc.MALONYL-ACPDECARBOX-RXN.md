---
entity_id: "reaction.ecocyc.MALONYL-ACPDECARBOX-RXN"
entity_type: "reaction"
name: "MALONYL-ACPDECARBOX-RXN"
source_database: "EcoCyc"
source_id: "MALONYL-ACPDECARBOX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# MALONYL-ACPDECARBOX-RXN

`reaction.ecocyc.MALONYL-ACPDECARBOX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:MALONYL-ACPDECARBOX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

MALONYL-ACP + PROTON -> ACETYL-ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: MALONYL-ACP + PROTON -> ACETYL-ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by malonyl-ACP decarboxylase (complex.ecocyc.CPLX0-12386), 3-oxoacyl-[acyl carrier protein] synthase 1 (complex.ecocyc.FABB-CPLX). Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-5965` fatty acid biosynthesis initiation III (EcoCyc)

## Annotation

MALONYL-ACP + PROTON -> ACETYL-ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-5965` fatty acid biosynthesis initiation III (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-12386|complex.ecocyc.CPLX0-12386]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FABB-CPLX|complex.ecocyc.FABB-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:MALONYL-ACPDECARBOX-RXN`

## Notes

MALONYL-ACP + PROTON -> ACETYL-ACP + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
