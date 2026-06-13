---
entity_id: "complex.ecocyc.CPLX0-7426"
entity_type: "complex"
name: "all-trans-octaprenyl-diphosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-7426"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# all-trans-octaprenyl-diphosphate synthase

`complex.ecocyc.CPLX0-7426`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7426`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AD57|protein.P0AD57]]

## Enriched Summary

Octaprenyl diphosphate (OPP) synthase catalyzes the condensation reactions resulting in the formation of OPP, the isoprenoid side chain of UBIQUINONE-8. To generate OPP, five isopentenyl diphosphate molecules are sequentially added to farnesyl diphosphate with trans stereochemistry . Residues that are important for determination of isoprenoid chain length have been identified by mutagenesis. Dimerization of the enzyme appears to play a role in chain length determination . Various detergents enhance the activity of the enzyme, which is thought to be limited by slow product release. Steady-state and pre-steady-state experiments were performed to obtain kinetic data . ispB is essential for growth in E. coli . In comparative studies of reaction mechanisms, E. coli octaprenyl diphosphate synthase, a trans-prenyltransferase, was found to use a sequential ionization-condensation-elimination mechanism involving a farnesyl carbocation intermediate. In contrast, undecaprenyl diphosphate synthase, a cis-prenyltransferase that utilizes the same substrate, was found to use a concerted mechanism . Subsequent site-directed mutagenesis studies probed the roles of active site amino acids in the catalytic mechanism of IspB . A preliminary X-ray diffraction analysis of the E. coli enzyme at 2.2 Å resolution has been reported. The crystal contained one homodimer per asymmetric unit . In an E...

## Biological Role

Catalyzes RXN-8992 (reaction.ecocyc.RXN-8992). Bound by Magnesium cation (molecule.C00305).

## Annotation

Octaprenyl diphosphate (OPP) synthase catalyzes the condensation reactions resulting in the formation of OPP, the isoprenoid side chain of UBIQUINONE-8. To generate OPP, five isopentenyl diphosphate molecules are sequentially added to farnesyl diphosphate with trans stereochemistry . Residues that are important for determination of isoprenoid chain length have been identified by mutagenesis. Dimerization of the enzyme appears to play a role in chain length determination . Various detergents enhance the activity of the enzyme, which is thought to be limited by slow product release. Steady-state and pre-steady-state experiments were performed to obtain kinetic data . ispB is essential for growth in E. coli . In comparative studies of reaction mechanisms, E. coli octaprenyl diphosphate synthase, a trans-prenyltransferase, was found to use a sequential ionization-condensation-elimination mechanism involving a farnesyl carbocation intermediate. In contrast, undecaprenyl diphosphate synthase, a cis-prenyltransferase that utilizes the same substrate, was found to use a concerted mechanism . Subsequent site-directed mutagenesis studies probed the roles of active site amino acids in the catalytic mechanism of IspB . A preliminary X-ray diffraction analysis of the E. coli enzyme at 2.2 Å resolution has been reported. The crystal contained one homodimer per asymmetric unit . In an E. coli strain engineered to produce coenzyme Q10, deletion of endogenous ispB and use of a heterologous dps gene expression system for overexpression of decaprenyl diphosphate synthase enhanced coenzyme Q10 production . Expression of the Schizosaccharomyces pombe genes dlp1 and dps1 encoding heteromeric decaprenyl diphosphate synthase in an E. coli strain containing an ispBR321A mutation resulted in rec

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-8992|reaction.ecocyc.RXN-8992]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AD57|protein.P0AD57]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7426`
- `QSPROTEOME:QS00181989`

## Notes

2*protein.P0AD57
