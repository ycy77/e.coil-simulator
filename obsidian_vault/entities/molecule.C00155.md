---
entity_id: "molecule.C00155"
entity_type: "small_molecule"
name: "L-Homocysteine"
source_database: "KEGG"
source_id: "C00155"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Homocysteine"
  - "L-2-Amino-4-mercaptobutyric acid"
  - "Homocysteine"
---

# L-Homocysteine

`molecule.C00155`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00155`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Homocysteine; L-2-Amino-4-mercaptobutyric acid; Homocysteine L-homocysteine is one of the major Protein-bound-uremic-retention-solutes "protein-bound uremic retention solutes". At concentrations encountered during uremia L-homocysteine predisposes uremic patients to cardiovascular disease through impairment of endothelial and smooth muscle cell functions.

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: L-Homocysteine; L-2-Amino-4-mercaptobutyric acid; Homocysteine

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7752|complex.ecocyc.CPLX0-7752]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN|reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN|reaction.ecocyc.RIBOSYLHOMOCYSTEINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15131|reaction.ecocyc.RXN-15131]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00650|reaction.R00650]] `KEGG` `database` - C00019 + C00155 <=> C00021 + C00073
- `is_substrate_of` --> [[reaction.R04405|reaction.R04405]] `KEGG` `database` - C04489 + C00155 <=> C04144 + C00073
- `is_substrate_of` --> [[reaction.ecocyc.HOMOCYSMET-RXN|reaction.ecocyc.HOMOCYSMET-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HOMOCYSMETB12-RXN|reaction.ecocyc.HOMOCYSMETB12-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN|reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.MMUM-RXN|reaction.ecocyc.MMUM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-21538|reaction.ecocyc.RXN-21538]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23922|reaction.ecocyc.RXN-23922]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23924|reaction.ecocyc.RXN-23924]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5501|reaction.ecocyc.RXN0-5501]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.HOMOSERKIN-RXN|reaction.ecocyc.HOMOSERKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00155`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
