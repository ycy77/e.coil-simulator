---
entity_id: "complex.ecocyc.MENF-CPLX"
entity_type: "complex"
name: "isochorismate synthase MenF"
source_database: "EcoCyc"
source_id: "MENF-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# isochorismate synthase MenF

`complex.ecocyc.MENF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MENF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P38051|protein.P38051]]

## Enriched Summary

There are two isochorismate synthase enzymes present in E. coli, encoded by menF and entC. MenF is specific to the menaquinone biosynthetic pathway, while EntC is specific to the enterobactin biosynthetic pathway . Isochorismate synthase activity due to MenF is increased under anaerobiosis, while activity due to EntC is increased by iron limitation . Reports differ on whether or not the reaction catalyzed by MenF is reversible. Crystal structures of MenF have been solved at 2.5 Å and 2 Å resolution . The Lys190 residue has been identified as the catalytic base, and a reaction mechanism involving the nucleophilic attack of a water molecule on the isochorismate ring has been proposed . The active site appears to contain both the required Mg2+ cofactor and a pair of sulfates . An entC single mutant is defective in enterobactin, but not menaquinone biosynthesis , while an entC menF double mutant is defective in both enterobactin and menaquinone biosynthesis . A menF mutant produces only trace amounts of menaquinone unless supplemented with o-succinylbenzoate . Expression of menF from a plasmid rescues the enterobactin biosynthesis defect of an entC mutant . Review: There are two isochorismate synthase enzymes present in E. coli, encoded by menF and entC. MenF is specific to the menaquinone biosynthetic pathway, while EntC is specific to the enterobactin biosynthetic pathway...

## Biological Role

Catalyzes ISOCHORSYN-RXN (reaction.ecocyc.ISOCHORSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

There are two isochorismate synthase enzymes present in E. coli, encoded by menF and entC. MenF is specific to the menaquinone biosynthetic pathway, while EntC is specific to the enterobactin biosynthetic pathway . Isochorismate synthase activity due to MenF is increased under anaerobiosis, while activity due to EntC is increased by iron limitation . Reports differ on whether or not the reaction catalyzed by MenF is reversible. Crystal structures of MenF have been solved at 2.5 Å and 2 Å resolution . The Lys190 residue has been identified as the catalytic base, and a reaction mechanism involving the nucleophilic attack of a water molecule on the isochorismate ring has been proposed . The active site appears to contain both the required Mg2+ cofactor and a pair of sulfates . An entC single mutant is defective in enterobactin, but not menaquinone biosynthesis , while an entC menF double mutant is defective in both enterobactin and menaquinone biosynthesis . A menF mutant produces only trace amounts of menaquinone unless supplemented with o-succinylbenzoate . Expression of menF from a plasmid rescues the enterobactin biosynthesis defect of an entC mutant . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ISOCHORSYN-RXN|reaction.ecocyc.ISOCHORSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P38051|protein.P38051]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:MENF-CPLX`
- `QSPROTEOME:QS00049505`

## Notes

2*protein.P38051
