---
entity_id: "complex.ecocyc.CPLX0-7957"
entity_type: "complex"
name: "selenide, water dikinase"
source_database: "EcoCyc"
source_id: "CPLX0-7957"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# selenide, water dikinase

`complex.ecocyc.CPLX0-7957`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7957`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P16456|protein.P16456]]

## Enriched Summary

Selenide, water dikinase (SelD) catalyzes the reaction that produces selenophosphate, the selenium donor for the biosynthesis of selenocysteine and modification of thiouridine to selenouridine in certain tRNAs . The enzyme is a dimer in solution and a crystal structure, with a Kd of 170 nM . The Cys17 , Lys20 , and Asn87 residues are essential for SelD catalytic activity. A crystal structure of the C17S mutant apoenzyme has been solved, showing a set of conserved aspartate residues that are involved in Mg2+ binding and are required for catalytic activity. A reaction mechanism has been proposed . SelD contains an unidentified chromophore . SelD forms a ternary complex with the EG10941-MONOMER SelA-L-seryl-SEC-tRNAs tRNASec complex. This interaction involves the N-terminal loop of SelD . Based on a new quantitative top-down proteomics method using iodo-tandem mass tags, two proteoforms of SelD were found to respond differently when grown in glucose as compared to acetate, pointing to possible different functions . The CsdA, CsdB and IscS proteins can all provide the selenium needed for the reaction . E. coli can utilize external selenocysteine as a source of selenium for biosynthesis of selenophosphate . A selD mutant is defective in both selenocysteine incorporation and seleno-modification of tRNA . Reviews: The publication by Preabrazhenskaya et al. () has been retracted...

## Biological Role

Catalyzes 2.7.9.3-RXN (reaction.ecocyc.2.7.9.3-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Annotation

Selenide, water dikinase (SelD) catalyzes the reaction that produces selenophosphate, the selenium donor for the biosynthesis of selenocysteine and modification of thiouridine to selenouridine in certain tRNAs . The enzyme is a dimer in solution and a crystal structure, with a Kd of 170 nM . The Cys17 , Lys20 , and Asn87 residues are essential for SelD catalytic activity. A crystal structure of the C17S mutant apoenzyme has been solved, showing a set of conserved aspartate residues that are involved in Mg2+ binding and are required for catalytic activity. A reaction mechanism has been proposed . SelD contains an unidentified chromophore . SelD forms a ternary complex with the EG10941-MONOMER SelA-L-seryl-SEC-tRNAs tRNASec complex. This interaction involves the N-terminal loop of SelD . Based on a new quantitative top-down proteomics method using iodo-tandem mass tags, two proteoforms of SelD were found to respond differently when grown in glucose as compared to acetate, pointing to possible different functions . The CsdA, CsdB and IscS proteins can all provide the selenium needed for the reaction . E. coli can utilize external selenocysteine as a source of selenium for biosynthesis of selenophosphate . A selD mutant is defective in both selenocysteine incorporation and seleno-modification of tRNA . Reviews: The publication by Preabrazhenskaya et al. () has been retracted .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.9.3-RXN|reaction.ecocyc.2.7.9.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P16456|protein.P16456]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7957`
- `QSPROTEOME:QS00188501`

## Notes

2*protein.P16456
