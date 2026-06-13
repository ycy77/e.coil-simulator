---
entity_id: "reaction.ecocyc.RXN-7682"
entity_type: "reaction"
name: "RXN-7682"
source_database: "EcoCyc"
source_id: "RXN-7682"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-7682

`reaction.ecocyc.RXN-7682`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-7682`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

HYPOXANTHINE + NAD + WATER -> XANTHINE + NADH + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: HYPOXANTHINE + NAD + WATER -> XANTHINE + NADH + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Hypoxanthine (molecule.C00262). Products: NADH (molecule.C00004), H+ (molecule.C00080), Xanthine (molecule.C00385).

## Enriched Pathways

- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Annotation

HYPOXANTHINE + NAD + WATER -> XANTHINE + NADH + PROTON; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.SALVADEHYPOX-PWY` adenosine nucleotides degradation II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00262|molecule.C00262]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-7682`

## Notes

HYPOXANTHINE + NAD + WATER -> XANTHINE + NADH + PROTON; direction=LEFT-TO-RIGHT
