---
entity_id: "molecule.C02823"
entity_type: "small_molecule"
name: "Cyanocobalamin"
source_database: "KEGG"
source_id: "C02823"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Cyanocobalamin"
  - "Cyanocob(III)alamin"
  - "Dicopac"
  - "Vitamin B12 complex"
---

# Cyanocobalamin

`molecule.C02823`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02823`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Cyanocobalamin; Cyanocob(III)alamin; Dicopac; Vitamin B12 complex EcoCyc common name: cyanocob(III)alamin. Cobalamin is the term used for Cobamides attached to a DIMETHYLBENZIMIDAZOLE lower axial ligand of the cobalt ion, without specifying the upper axial ligand. It includes several compounds often referred to as vitamin B12, that differ in the upper axial ligand. The functional forms of the B12 vitamin, CPD-9037 and ADENOSYLCOBALAMIN, include either a methyl group or an 5'-deoxyadenosyl group as their upper axial ligand, respectively. Other forms of cobalamin include CPD0-1256 (or its conjugated acid AQUACOBIIIALAMIN) and CPD-315. CPD0-1256 Hydroxocobalamin is a naturally produced form synthesized by many bacterial species, while CPD-315 is a common semi-synthetic form produced from bacterially-synthesized CPD0-1256. Vitamin B12 pills often contain CPD-315, which is converted to the active forms in the body. The cobalt ion embedded in cobalamin may exist in different charges (+1, +2 or +3), and the different forms of the compound are referred to as COB-I-ALAMIN, CPD-1829 and CPD-17105, respectively. Cyanocob(III)alamin is a CPD-17105 derivative where the CO+3 ion is held in place partly due to an upper cyano group. The cyano group is an artificial ligand, created as a result of the extraction procedure...

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Annotation

KEGG compound: Cyanocobalamin; Cyanocob(III)alamin; Dicopac; Vitamin B12 complex

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco04980` Cobalamin transport and metabolism (KEGG)

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.ETHAMLY-RXN|reaction.ecocyc.ETHAMLY-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02823`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
