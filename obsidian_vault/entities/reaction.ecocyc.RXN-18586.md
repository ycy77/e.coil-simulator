---
entity_id: "reaction.ecocyc.RXN-18586"
entity_type: "reaction"
name: "RXN-18586"
source_database: "EcoCyc"
source_id: "RXN-18586"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18586

`reaction.ecocyc.RXN-18586`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18586`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

SULFO-CYSTEINE + Red-Glutaredoxins -> CYS + SO3 + Ox-Glutaredoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: SULFO-CYSTEINE + Red-Glutaredoxins -> CYS + SO3 + Ox-Glutaredoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Sulfo-L-cysteine (molecule.C05824). Products: H+ (molecule.C00080), Sulfite (molecule.C00094), L-Cysteine (molecule.C00097).

## Enriched Pathways

- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Annotation

SULFO-CYSTEINE + Red-Glutaredoxins -> CYS + SO3 + Ox-Glutaredoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7870` L-cysteine biosynthesis VII (from S-sulfo-L-cysteine) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00094|molecule.C00094]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05824|molecule.C05824]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18586`

## Notes

SULFO-CYSTEINE + Red-Glutaredoxins -> CYS + SO3 + Ox-Glutaredoxins + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
