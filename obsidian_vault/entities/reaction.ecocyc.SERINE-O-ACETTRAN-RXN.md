---
entity_id: "reaction.ecocyc.SERINE-O-ACETTRAN-RXN"
entity_type: "reaction"
name: "SERINE-O-ACETTRAN-RXN"
source_database: "EcoCyc"
source_id: "SERINE-O-ACETTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SERINE-O-ACETTRAN-RXN

`reaction.ecocyc.SERINE-O-ACETTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SERINE-O-ACETTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction in the conversion of serine to cysteine. EcoCyc reaction equation: SER + ACETYL-COA -> ACETYLSERINE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first reaction in the conversion of serine to cysteine.

## Biological Role

Catalyzed by serine acetyltransferase (complex.ecocyc.CPLX0-237). Substrates: Acetyl-CoA (molecule.C00024), L-Serine (molecule.C00065). Products: CoA (molecule.C00010), O-Acetyl-L-serine (molecule.C00979).

## Enriched Pathways

- `ecocyc.CYSTSYN-PWY` L-cysteine biosynthesis I (EcoCyc)
- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Annotation

This is the first reaction in the conversion of serine to cysteine.

## Pathways

- `ecocyc.CYSTSYN-PWY` L-cysteine biosynthesis I (EcoCyc)
- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-237|complex.ecocyc.CPLX0-237]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00979|molecule.C00979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00041|molecule.C00041]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:SERINE-O-ACETTRAN-RXN`

## Notes

SER + ACETYL-COA -> ACETYLSERINE + CO-A; direction=PHYSIOL-LEFT-TO-RIGHT
