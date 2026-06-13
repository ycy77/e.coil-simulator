---
entity_id: "reaction.ecocyc.RXN-17775"
entity_type: "reaction"
name: "RXN-17775"
source_database: "EcoCyc"
source_id: "RXN-17775"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17775

`reaction.ecocyc.RXN-17775`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17775`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OLEOYL-COA + ETF-Oxidized + PROTON -> CPD-19172 + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: OLEOYL-COA + ETF-Oxidized + PROTON -> CPD-19172 + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Catalyzed by fadE (protein.Q47146). Substrates: H+ (molecule.C00080), Oleoyl-CoA (molecule.C00510). Products: (2E,9Z)-octadec-2,9-enoyl-CoA (molecule.ecocyc.CPD-19172).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

OLEOYL-COA + ETF-Oxidized + PROTON -> CPD-19172 + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.Q47146|protein.Q47146]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-19172|molecule.ecocyc.CPD-19172]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00510|molecule.C00510]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17775`

## Notes

OLEOYL-COA + ETF-Oxidized + PROTON -> CPD-19172 + ETF-Reduced; direction=REVERSIBLE
