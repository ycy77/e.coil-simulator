---
entity_id: "molecule.C00533"
entity_type: "small_molecule"
name: "Nitric oxide"
source_database: "KEGG"
source_id: "C00533"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nitric oxide"
  - "NO"
  - "Nitrogen monoxide"
---

# Nitric oxide

`molecule.C00533`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00533`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nitric oxide; NO; Nitrogen monoxide Nitric oxide is a free radical, consisting of one nitrogen and one oxygen atom. In the vasculature, nitric oxide, which is the active moiety of the endothelium-derived relaxing factor, relaxes smooth muscle and inhibits platelet and leukocyte adhesion. Outside the vasculature, NO participates in the immunologic response to infection and serves as a neurotransmitter.

## Biological Role

Consumed as substrate in 8 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Nitric oxide; NO; Nitrogen monoxide

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (15)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7751|complex.ecocyc.CPLX0-7751]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_substrate_of` --> [[reaction.R05724|reaction.R05724]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_substrate_of` --> [[reaction.R05725|reaction.R05725]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_substrate_of` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23276|reaction.ecocyc.RXN-23276]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23850|reaction.ecocyc.RXN-23850]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2721|reaction.ecocyc.RXN0-2721]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5487|reaction.ecocyc.RXN0-5487]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7493|reaction.ecocyc.RXN0-7493]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.IMP-DEHYDROG-RXN|reaction.ecocyc.IMP-DEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-19777|reaction.ecocyc.RXN-19777]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-2601|reaction.ecocyc.RXN0-2601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-4261|reaction.ecocyc.RXN0-4261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5266|reaction.ecocyc.RXN0-5266]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5268|reaction.ecocyc.RXN0-5268]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00533`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
