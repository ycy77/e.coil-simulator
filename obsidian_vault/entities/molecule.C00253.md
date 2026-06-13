---
entity_id: "molecule.C00253"
entity_type: "small_molecule"
name: "Nicotinate"
source_database: "KEGG"
source_id: "C00253"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nicotinate"
  - "Nicotinic acid"
  - "Niacin"
  - "3-Pyridinecarboxylic acid"
---

# Nicotinate

`molecule.C00253`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00253`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nicotinate; Nicotinic acid; Niacin; 3-Pyridinecarboxylic acid NIACINE "Nicotinate" (niacin, 3-pyridinecarboxylate) is a carboxylic derivative of PYRIDINE that is found in nature as part of pyridine cofactors (e.g., NAD and NADP) and alkaloids (e.g., NICOTINE and CPD-12317). Nicotinate is one of three forms of vitamin B3: NIACINE, NIACINAMIDE, and NICOTINAMIDE_RIBOSE "nicotinamide riboside" [more accurately named 1-(β-D ribofuranosyl)nicotinamide]. These three forms are interchangeable, and are usually used for the biosynthesis of NAD . NICOTINAMIDE_RIBOSE can be converted to NIACINAMIDE by EC-3.2.2.3 RXN-8441 and NIACINAMIDE can be hydrolyzed to NIACINE by EC-3.5.1.19 (which is not present in humans) NICOTINAMID-RXN Eukaryotes and prokaryotes produce NAD de novo from TRP and L-ASPARTATE, respectively, by pathways that bypasses vitamin B3 compounds and instead proceed via NICOTINATE_NUCLEOTIDE (see NADSYN-PWY and PYRIDNUCSYN-PWY). Vitamin B3 compounds are used in NAD salvage pathways such as PWY-5381 and PWY3O-4106 . In populations with a tryptophan-poor diet the NAD de novo biosynthesis pathway is not sufficient to produce the required NAD, making the salvage pathways that rely on vitamin B3 compounds the main source of NAD. Under these conditions a difficiency of vitamin B3 compounds can result in the disease pellagra.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Nicotinate; Nicotinic acid; Niacin; 3-Pyridinecarboxylic acid

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R01724|reaction.R01724]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` --> [[reaction.R04148|reaction.R04148]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_product_of` --> [[reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN|reaction.ecocyc.DMBPPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.NICOTINAMID-RXN|reaction.ecocyc.NICOTINAMID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN|reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00253`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
