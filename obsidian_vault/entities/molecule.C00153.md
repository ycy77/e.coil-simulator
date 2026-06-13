---
entity_id: "molecule.C00153"
entity_type: "small_molecule"
name: "Nicotinamide"
source_database: "KEGG"
source_id: "C00153"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nicotinamide"
  - "Nicotinic acid amide"
  - "Niacinamide"
  - "Vitamin PP"
---

# Nicotinamide

`molecule.C00153`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00153`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nicotinamide; Nicotinic acid amide; Niacinamide; Vitamin PP Nicotinamide is one of three forms of vitamin B3: NIACINE, NIACINAMIDE, and NICOTINAMIDE_RIBOSE "nicotinamide riboside" [more accurately named 1-(β-D ribofuranosyl)nicotinamide]. These three forms are interchangeable, and are usually used for the biosynthesis of NAD . NICOTINAMIDE_RIBOSE can be hydrolyzed to form NIACINAMIDE by EC-3.2.2.3 RXN-8441 and NIACINAMIDE can be hydrolyzed to NIACINE by EC-3.5.1.19 (which is not present in humans) NICOTINAMID-RXN Eukaryotes and prokaryotes produce NAD de novo from TRP and L-ASPARTATE, respectively, by pathways that bypasses vitamin B3 compounds and instead proceed via NICOTINATE_NUCLEOTIDE (see NADSYN-PWY and PYRIDNUCSYN-PWY). Vitamin B3 compounds are used in NAD salvage pathways such as PWY-5381 and PWY3O-4106 . In populations with a tryptophan-poor diet the NAD de novo biosynthesis pathway is not sufficient to produce the required NAD, making the salvage pathways that rely on vitamin B3 compounds the main source of NAD. Under these conditions a difficiency of vitamin B3 compounds can result in the disease pellagra.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 6 reaction(s).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Nicotinamide; Nicotinic acid amide; Niacinamide; Vitamin PP

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (9)

- `is_product_of` --> [[reaction.ecocyc.NMNNUCLEOSID-RXN|reaction.ecocyc.NMNNUCLEOSID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13859|reaction.ecocyc.RXN-13859]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-19919|reaction.ecocyc.RXN-19919]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-22964|reaction.ecocyc.RXN-22964]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6445|reaction.ecocyc.RXN0-6445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.NICOTINAMID-RXN|reaction.ecocyc.NICOTINAMID-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7092|reaction.ecocyc.RXN0-7092]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00153`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
