---
entity_id: "reaction.ecocyc.RXN-22438"
entity_type: "reaction"
name: "RXN-22438"
source_database: "EcoCyc"
source_id: "RXN-22438"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22438

`reaction.ecocyc.RXN-22438`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22438`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-METHYL-THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + NADH + PROTON; direction=REVERSIBLE EcoCyc reaction equation: 5-METHYL-THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + NADH + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by 5,10-methylenetetrahydrofolate reductase (complex.ecocyc.METHYLENETHFREDUCT-CPLX). Substrates: NAD+ (molecule.C00003), a 5-methyltetrahydrofolate (molecule.ecocyc.5-METHYL-THF-GLU-N). Products: NADH (molecule.C00004), H+ (molecule.C00080), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Annotation

5-METHYL-THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + NADH + PROTON; direction=REVERSIBLE

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.METHYLENETHFREDUCT-CPLX|complex.ecocyc.METHYLENETHFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-METHYL-THF-GLU-N|molecule.ecocyc.5-METHYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22438`

## Notes

5-METHYL-THF-GLU-N + NAD -> METHYLENE-THF-GLU-N + NADH + PROTON; direction=REVERSIBLE
