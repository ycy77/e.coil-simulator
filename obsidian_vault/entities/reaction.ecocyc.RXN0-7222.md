---
entity_id: "reaction.ecocyc.RXN0-7222"
entity_type: "reaction"
name: "L-galactose:proton symport"
source_database: "EcoCyc"
source_id: "RXN0-7222"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-galactose:proton symport

`reaction.ecocyc.RXN0-7222`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7222`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

L-Galactose + PROTON -> L-Galactose + PROTON; direction=REVERSIBLE EcoCyc reaction equation: L-Galactose + PROTON -> L-Galactose + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by fucP (protein.P11551). Substrates: H+ (molecule.C00080), L-Galactose (molecule.C01825). Products: H+ (molecule.C00080), L-Galactose (molecule.C01825).

## Annotation

L-Galactose + PROTON -> L-Galactose + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P11551|protein.P11551]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01825|molecule.C01825]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01825|molecule.C01825]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7222`

## Notes

L-Galactose + PROTON -> L-Galactose + PROTON; direction=REVERSIBLE
