---
entity_id: "reaction.ecocyc.RXN-11474"
entity_type: "reaction"
name: "3-oxo-glutaryl-[acp] methyl ester synthase"
source_database: "EcoCyc"
source_id: "RXN-11474"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-oxo-glutaryl-[acp] methyl ester synthase

`reaction.ecocyc.RXN-11474`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11474`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Malonyl-acp-methyl-ester + MALONYL-ACP + PROTON -> 3-Ketoglutaryl-ACP-methyl-ester + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Malonyl-acp-methyl-ester + MALONYL-ACP + PROTON -> 3-Ketoglutaryl-ACP-methyl-ester + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: CO2 (molecule.C00011).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Malonyl-acp-methyl-ester + MALONYL-ACP + PROTON -> 3-Ketoglutaryl-ACP-methyl-ester + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11474`

## Notes

Malonyl-acp-methyl-ester + MALONYL-ACP + PROTON -> 3-Ketoglutaryl-ACP-methyl-ester + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
