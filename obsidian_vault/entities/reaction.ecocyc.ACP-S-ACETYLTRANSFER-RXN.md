---
entity_id: "reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN"
entity_type: "reaction"
name: "ACP-S-ACETYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ACP-S-ACETYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACP-S-ACETYLTRANSFER-RXN

`reaction.ecocyc.ACP-S-ACETYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACP-S-ACETYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

One of the initial reactions in fatty acid biosynthesis. EcoCyc reaction equation: ACP + ACETYL-COA -> ACETYL-ACP + CO-A; direction=REVERSIBLE. One of the initial reactions in fatty acid biosynthesis.

## Biological Role

Catalyzed by 3-oxoacyl-[acyl carrier protein] synthase 3 (complex.ecocyc.CPLX0-252). Substrates: Acetyl-CoA (molecule.C00024). Products: CoA (molecule.C00010).

## Enriched Pathways

- `ecocyc.PWY-5966` fatty acid biosynthesis initiation II (EcoCyc)

## Annotation

One of the initial reactions in fatty acid biosynthesis.

## Pathways

- `ecocyc.PWY-5966` fatty acid biosynthesis initiation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-252|complex.ecocyc.CPLX0-252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00831|molecule.C00831]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1242|molecule.ecocyc.CPD0-1242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.IODOACETAMIDE|molecule.ecocyc.IODOACETAMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.N-ETHYLMALEIMIDE|molecule.ecocyc.N-ETHYLMALEIMIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACP-S-ACETYLTRANSFER-RXN`

## Notes

ACP + ACETYL-COA -> ACETYL-ACP + CO-A; direction=REVERSIBLE
