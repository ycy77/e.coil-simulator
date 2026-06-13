---
entity_id: "reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN"
entity_type: "reaction"
name: "METHYLENETHFDEHYDROG-NADP-RXN"
source_database: "EcoCyc"
source_id: "METHYLENETHFDEHYDROG-NADP-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHYLENETHFDEHYDROG-NADP-RXN

`reaction.ecocyc.METHYLENETHFDEHYDROG-NADP-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHYLENETHFDEHYDROG-NADP-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHYLENE-THF-GLU-N + NADP -> 5-10-METHENYL-THF-GLU-N + NADPH; direction=REVERSIBLE EcoCyc reaction equation: METHYLENE-THF-GLU-N + NADP -> 5-10-METHENYL-THF-GLU-N + NADPH; direction=REVERSIBLE.

## Biological Role

Catalyzed by bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase (complex.ecocyc.FOLD-CPLX). Substrates: NADP+ (molecule.C00006), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N). Products: NADPH (molecule.C00005), a 5,10-methenyltetrahydrofolate (molecule.ecocyc.5-10-METHENYL-THF-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Annotation

METHYLENE-THF-GLU-N + NADP -> 5-10-METHENYL-THF-GLU-N + NADPH; direction=REVERSIBLE

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (12)

- `catalyzes` <-- [[complex.ecocyc.FOLD-CPLX|complex.ecocyc.FOLD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-10-METHENYL-THF-GLU-N|molecule.ecocyc.5-10-METHENYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00234|molecule.C00234]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2685|molecule.ecocyc.CPD0-2685]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.TRIS|molecule.ecocyc.TRIS]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHYLENETHFDEHYDROG-NADP-RXN`

## Notes

METHYLENE-THF-GLU-N + NADP -> 5-10-METHENYL-THF-GLU-N + NADPH; direction=REVERSIBLE
