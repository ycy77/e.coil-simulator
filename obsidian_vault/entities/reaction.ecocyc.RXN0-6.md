---
entity_id: "reaction.ecocyc.RXN0-6"
entity_type: "reaction"
name: "Fe2+:proton antiport"
source_database: "EcoCyc"
source_id: "RXN0-6"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Fe2+:proton antiport

`reaction.ecocyc.RXN0-6`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + FE+2 -> PROTON + FE+2; direction=REVERSIBLE EcoCyc reaction equation: PROTON + FE+2 -> PROTON + FE+2; direction=REVERSIBLE.

## Biological Role

Catalyzed by Zn2+/Fe2+/Cd2+ exporter (complex.ecocyc.CPLX0-7641). Substrates: H+ (molecule.C00080), Fe2+ (molecule.C14818). Products: H+ (molecule.C00080), Fe2+ (molecule.C14818).

## Annotation

PROTON + FE+2 -> PROTON + FE+2; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7641|complex.ecocyc.CPLX0-7641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6`

## Notes

PROTON + FE+2 -> PROTON + FE+2; direction=REVERSIBLE
