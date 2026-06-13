---
entity_id: "reaction.ecocyc.RXN-11484"
entity_type: "reaction"
name: "RXN-11484"
source_database: "EcoCyc"
source_id: "RXN-11484"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11484

`reaction.ecocyc.RXN-11484`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11484`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Pimeloyl-ACPs + L-ALPHA-ALANINE + PROTON -> 8-AMINO-7-OXONONANOATE + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: Pimeloyl-ACPs + L-ALPHA-ALANINE + PROTON -> 8-AMINO-7-OXONONANOATE + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 8-amino-7-oxononanoate synthase (complex.ecocyc.7KAPSYN-CPLX). Substrates: L-Alanine (molecule.C00041), H+ (molecule.C00080). Products: CO2 (molecule.C00011), 8-Amino-7-oxononanoate (molecule.C01092).

## Enriched Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Annotation

Pimeloyl-ACPs + L-ALPHA-ALANINE + PROTON -> 8-AMINO-7-OXONONANOATE + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6519` 8-amino-7-oxononanoate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.7KAPSYN-CPLX|complex.ecocyc.7KAPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01092|molecule.C01092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11484`

## Notes

Pimeloyl-ACPs + L-ALPHA-ALANINE + PROTON -> 8-AMINO-7-OXONONANOATE + CARBON-DIOXIDE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
