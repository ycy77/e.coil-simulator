---
entity_id: "complex.ecocyc.DXPREDISOM-CPLX"
entity_type: "complex"
name: "1-deoxy-D-xylulose 5-phosphate reductoisomerase"
source_database: "EcoCyc"
source_id: "DXPREDISOM-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 1-deoxy-D-xylulose 5-phosphate reductoisomerase

`complex.ecocyc.DXPREDISOM-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DXPREDISOM-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P45568|protein.P45568]]

## Enriched Summary

1-deoxy-D-xylulose 5-phosphate reductoisomerase (Dxr) is involved in the first committed step in the methylerythritol phosphate pathway of isoprenoid biosynthesis. Dxr catalyzes the conversion of 1-deoxy-D-xylulose 5-phosphate (DXP) into the dedicated MEP pathway intermediate 2-C-methyl-D-erythritol-4-phosphate (MEP). This reaction is NADPH-dependent, and required a bivalent metal cofactor . This is a two-step reaction. The first step is a non-reductive, NADPH-dependent rearrangement that generates MEP. This is followed by an NADPH-dependent reduction of this intermediate to generate the final product . This reaction appears to depend on one or more of Dxr's histidines . Based on the stereospecificity of the reaction, Dxr is a class B dehydrogenase . Different mechanisms for the DXR catalyzed reaction have been proposed and investigated . A number of structures have been determined for Dxr. A crystal structure of the dimer to 2.5 Å resolution shows that the Dxr connective domain is responsible for dimerization and contains the bulk of the enzyme's active site . A crystal structure of Dxr complexed with NADPH and a sulfur ion to 2.2 Å resolution shows that a flexible loop covers the active site . Crystal structures of Dxr both unbound and bound to the inhibitor and antimalarial drug fosmidomycin show that drug binding causes a substantial conformational change...

## Biological Role

Catalyzes DXPREDISOM-RXN (reaction.ecocyc.DXPREDISOM-RXN). Bound by NADPH (molecule.C00005), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

1-deoxy-D-xylulose 5-phosphate reductoisomerase (Dxr) is involved in the first committed step in the methylerythritol phosphate pathway of isoprenoid biosynthesis. Dxr catalyzes the conversion of 1-deoxy-D-xylulose 5-phosphate (DXP) into the dedicated MEP pathway intermediate 2-C-methyl-D-erythritol-4-phosphate (MEP). This reaction is NADPH-dependent, and required a bivalent metal cofactor . This is a two-step reaction. The first step is a non-reductive, NADPH-dependent rearrangement that generates MEP. This is followed by an NADPH-dependent reduction of this intermediate to generate the final product . This reaction appears to depend on one or more of Dxr's histidines . Based on the stereospecificity of the reaction, Dxr is a class B dehydrogenase . Different mechanisms for the DXR catalyzed reaction have been proposed and investigated . A number of structures have been determined for Dxr. A crystal structure of the dimer to 2.5 Å resolution shows that the Dxr connective domain is responsible for dimerization and contains the bulk of the enzyme's active site . A crystal structure of Dxr complexed with NADPH and a sulfur ion to 2.2 Å resolution shows that a flexible loop covers the active site . Crystal structures of Dxr both unbound and bound to the inhibitor and antimalarial drug fosmidomycin show that drug binding causes a substantial conformational change . Crystal structures of Dxr bound to bisphonates indicate that these compounds bind the same site as fosmidomycin . dxr deficient mutants required 2-C-methylerythritol, a free alcohol for MEP, for growth and survival . Analysis of dxr-deficient mutants identified Glu231 to play an important role in the conversion of DXP to MEP . Depletion of Dxr was found to generate reactive oxygen species (ROS), inducing oxidativ

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DXPREDISOM-RXN|reaction.ecocyc.DXPREDISOM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P45568|protein.P45568]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DXPREDISOM-CPLX`
- `QSPROTEOME:QS00185173`

## Notes

2*protein.P45568
