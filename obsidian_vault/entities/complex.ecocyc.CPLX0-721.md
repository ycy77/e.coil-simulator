---
entity_id: "complex.ecocyc.CPLX0-721"
entity_type: "complex"
name: "2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-721"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase

`complex.ecocyc.CPLX0-721`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-721`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P62617|protein.P62617]]

## Enriched Summary

2C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (IspF) is involved in the fifth step of the methylerythritol phosphate pathway. IspF catalyzes the Mn2+- or Mg2+-dependent conversion of 2-phospho-4-(cytidine 5'diphospho)-2-C-methyl-D-erythritol into 2-C-methyl-D-erythritol-2,4-cyclodiphosphate . Substantial structural research has been done on IspF. Crystal structures of IspF on its own and bound to subtrates reveal that it is a trimer, with a central hydrophobic cavity and three active sites located between the subunits. One Zn2+ is bound at each active site . IspF binds various isoprenoid compounds, downstream products derived from the methylerythritol phosphate pathway, in its hydrophobic central cavity. The isoprenoids DELTA3-ISOPENTENYL-PP/CPD-4211, GERANYL-PP, and FARNESYL-PP appear bound to IspF in a 1:4:2 ratio . Although Arg-142 in each IspF monomer forms a hydrophobic bond with the diphosphate group in the bound isoprenoid, these arginines are not required for isoprenoid binding . IspF is not regulated by the downstream metabolites by negative feedback inhibition. 2C-methyl-D-erythritol 4-phosphate (MEP), the first committed MEP pathway intermediate, activates and sustains IspF activity. IspF-MEP complex is inhibited by farnesyl diphosphate . ispF is an essential gene...

## Biological Role

Catalyzes RXN0-302 (reaction.ecocyc.RXN0-302). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

2C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (IspF) is involved in the fifth step of the methylerythritol phosphate pathway. IspF catalyzes the Mn2+- or Mg2+-dependent conversion of 2-phospho-4-(cytidine 5'diphospho)-2-C-methyl-D-erythritol into 2-C-methyl-D-erythritol-2,4-cyclodiphosphate . Substantial structural research has been done on IspF. Crystal structures of IspF on its own and bound to subtrates reveal that it is a trimer, with a central hydrophobic cavity and three active sites located between the subunits. One Zn2+ is bound at each active site . IspF binds various isoprenoid compounds, downstream products derived from the methylerythritol phosphate pathway, in its hydrophobic central cavity. The isoprenoids DELTA3-ISOPENTENYL-PP/CPD-4211, GERANYL-PP, and FARNESYL-PP appear bound to IspF in a 1:4:2 ratio . Although Arg-142 in each IspF monomer forms a hydrophobic bond with the diphosphate group in the bound isoprenoid, these arginines are not required for isoprenoid binding . IspF is not regulated by the downstream metabolites by negative feedback inhibition. 2C-methyl-D-erythritol 4-phosphate (MEP), the first committed MEP pathway intermediate, activates and sustains IspF activity. IspF-MEP complex is inhibited by farnesyl diphosphate . ispF is an essential gene . Loss of IspF function leads to growth defects, filamentous growth, and a sensitivity to antibiotics that target the cell wall . Since the enzymes of the methylerythritol pathway are not found in humans, these enzymes have attracted interest for its potential as anti-infective drug targets. Both computational and high-throughput experimental methods have been used to attempt to identify inhibitors of IspF |CITS [19320487][17081012]|.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-302|reaction.ecocyc.RXN0-302]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P62617|protein.P62617]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:CPLX0-721`
- `QSPROTEOME:QS00151831`

## Notes

3*protein.P62617
