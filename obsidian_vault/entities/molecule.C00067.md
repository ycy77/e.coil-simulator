---
entity_id: "molecule.C00067"
entity_type: "small_molecule"
name: "Formaldehyde"
source_database: "KEGG"
source_id: "C00067"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Formaldehyde"
  - "Methanal"
  - "Oxomethane"
  - "Oxomethylene"
  - "Methylene oxide"
  - "Formalin"
---

# Formaldehyde

`molecule.C00067`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00067`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Formaldehyde; Methanal; Oxomethane; Oxomethylene; Methylene oxide; Formalin

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 12 reaction(s).

## Enriched Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Annotation

KEGG compound: Formaldehyde; Methanal; Oxomethane; Oxomethylene; Methylene oxide; Formalin

## Pathways

- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00680` Methane metabolism (KEGG)

## Outgoing Edges (18)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8235|complex.ecocyc.CPLX0-8235]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00602|reaction.R00602]] `KEGG` `database` - C00132 + C00027 <=> C00067 + 2 C00001
- `is_product_of` --> [[reaction.ecocyc.RXN-12353|reaction.ecocyc.RXN-12353]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18737|reaction.ecocyc.RXN-18737]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18738|reaction.ecocyc.RXN-18738]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-18739|reaction.ecocyc.RXN-18739]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21233|reaction.ecocyc.RXN-21233]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21235|reaction.ecocyc.RXN-21235]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21236|reaction.ecocyc.RXN-21236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-2961|reaction.ecocyc.RXN-2961]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-301|reaction.ecocyc.RXN0-301]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7280|reaction.ecocyc.RXN0-7280]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-984|reaction.ecocyc.RXN0-984]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-2881|reaction.ecocyc.RXN-2881]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-9559|reaction.ecocyc.RXN-9559]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7266|reaction.ecocyc.RXN0-7266]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-19249|reaction.ecocyc.RXN-19249]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00067`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
