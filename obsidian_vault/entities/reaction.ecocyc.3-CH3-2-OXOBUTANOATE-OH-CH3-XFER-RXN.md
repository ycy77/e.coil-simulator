---
entity_id: "reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN"
entity_type: "reaction"
name: "3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN"
source_database: "EcoCyc"
source_id: "3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN

`reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction of the pantothenate biosynthesis pathway. EcoCyc reaction equation: METHYLENE-THF-GLU-N + 2-KETO-ISOVALERATE + WATER -> 2-DEHYDROPANTOATE + THF-GLU-N; direction=REVERSIBLE. This is the first reaction of the pantothenate biosynthesis pathway.

## Biological Role

Catalyzed by 3-methyl-2-oxobutanoate hydroxymethyltransferase (complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX). Substrates: H2O (molecule.C00001), 3-Methyl-2-oxobutanoic acid (molecule.C00141), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N). Products: 2-Dehydropantoate (molecule.C00966), THF-polyglutamate (molecule.C03541).

## Enriched Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Annotation

This is the first reaction of the pantothenate biosynthesis pathway.

## Pathways

- `ecocyc.PANTO-PWY` phosphopantothenate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `catalyzes` <-- [[complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX|complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00966|molecule.C00966]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00141|molecule.C00141]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00101|molecule.C00101]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00183|molecule.C00183]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00522|molecule.C00522]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00864|molecule.C00864]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-3642|molecule.ecocyc.CPD-3642]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1307|molecule.ecocyc.CPD0-1307]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.ISOVALERATE|molecule.ecocyc.ISOVALERATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN`

## Notes

METHYLENE-THF-GLU-N + 2-KETO-ISOVALERATE + WATER -> 2-DEHYDROPANTOATE + THF-GLU-N; direction=REVERSIBLE
