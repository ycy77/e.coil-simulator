---
entity_id: "molecule.C00288"
entity_type: "small_molecule"
name: "HCO3-"
source_database: "KEGG"
source_id: "C00288"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "HCO3-"
  - "Hydrogencarbonate"
  - "Bicarbonate"
  - "Hydrogen carbonate"
  - "Acid carbonate"
---

# HCO3-

`molecule.C00288`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00288`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: HCO3-; Hydrogencarbonate; Bicarbonate; Hydrogen carbonate; Acid carbonate EcoCyc common name: hydrogen carbonate.

## Biological Role

Consumed as substrate in 18 reaction(s). Produced in 3 reaction(s). Binds cyclopropane fatty acyl phospholipid synthase (complex.ecocyc.CFA-CPLX), 1,4-dihydroxy-2-naphthoyl-CoA synthase (complex.ecocyc.CPLX0-7882).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: HCO3-; Hydrogencarbonate; Bicarbonate; Hydrogen carbonate; Acid carbonate

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00230` Purine metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (26)

- `activates` --> [[reaction.ecocyc.3.4.11.1-RXN|reaction.ecocyc.3.4.11.1-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN-14569|reaction.ecocyc.RXN-14569]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `binds` --> [[complex.ecocyc.CFA-CPLX|complex.ecocyc.CFA-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` --> [[complex.ecocyc.CPLX0-7882|complex.ecocyc.CPLX0-7882]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.PEPCARBOX-RXN|reaction.ecocyc.PEPCARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18031|reaction.ecocyc.RXN-18031]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19659|reaction.ecocyc.RXN-19659]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00150|reaction.R00150]] `KEGG` `database` - C00002 + C00014 + C00288 <=> C00008 + C00169 + C00001
- `is_substrate_of` --> [[reaction.R00575|reaction.R00575]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` --> [[reaction.R00742|reaction.R00742]] `KEGG` `database` - C00002 + C00024 + C00288 <=> C00008 + C00009 + C00083
- `is_substrate_of` --> [[reaction.R10948|reaction.R10948]] `KEGG` `database` - C00002 + C00288 <=> C00008 + C20969
- `is_substrate_of` --> [[reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN|reaction.ecocyc.ACETYL-COA-CARBOXYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BIOTIN-CARBOXYL-RXN|reaction.ecocyc.BIOTIN-CARBOXYL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CARBAMATE-KINASE-RXN|reaction.ecocyc.CARBAMATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN|reaction.ecocyc.PROPIONYL-COA-CARBOXY-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12893|reaction.ecocyc.RXN-12893]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-13202|reaction.ecocyc.RXN-13202]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14569|reaction.ecocyc.RXN-14569]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-16909|reaction.ecocyc.RXN-16909]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18032|reaction.ecocyc.RXN-18032]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22735|reaction.ecocyc.RXN-22735]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5224|reaction.ecocyc.RXN0-5224]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-742|reaction.ecocyc.RXN0-742]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00288`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
