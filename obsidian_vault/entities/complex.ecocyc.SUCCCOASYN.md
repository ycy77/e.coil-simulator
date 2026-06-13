---
entity_id: "complex.ecocyc.SUCCCOASYN"
entity_type: "complex"
name: "succinyl-CoA synthetase"
source_database: "EcoCyc"
source_id: "SUCCCOASYN"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# succinyl-CoA synthetase

`complex.ecocyc.SUCCCOASYN`

## Static

- Type: `complex`
- Source: `EcoCyc:SUCCCOASYN`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGE9|protein.P0AGE9]], [[protein.P0A836|protein.P0A836]]

## Enriched Summary

Succinyl-CoA synthetase catalyzes the only reaction of the TCA cycle that employs substrate-level phosphorylation. The reaction is reversible and is thought to proceed in three partial reactions via enzyme-bound succinyl-phosphate and a phosphorylated enzyme intermediate, where a histidine residue of the α subunit is transiently phosphorylated. Many biochemical studies were done with the enzyme purified from E. coli Crooks strain (see citations in the Enzymatic Reaction summary), while mutant enzymes were obtained from the genes of a K-12-derived strain. A hybrid enzyme containing one wild-type and one catalytically inactive α subunit retains significant enzymatic activity, arguing for the presence of two independently active heterodimers . Crystal structures of the enzyme from various E. coli sources have been solved . The α2β2 heterotetramer is composed of two αβ heterodimers . Two possible alternative interpretations of the dimer-dimer interface were resolved by generating site-directed mutants that exist and are catalytically active as αβ heterodimers . Overlap of the sucC and sucD open reading frames suggests translational coupling . A sucCD insertion mutant does not grow aearobically on acetate or α-ketoglutarate or anaerobically on glucose or succinate as carbon sources...

## Biological Role

Catalyzes SUCCCOASYN-RXN (reaction.ecocyc.SUCCCOASYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Succinyl-CoA synthetase catalyzes the only reaction of the TCA cycle that employs substrate-level phosphorylation. The reaction is reversible and is thought to proceed in three partial reactions via enzyme-bound succinyl-phosphate and a phosphorylated enzyme intermediate, where a histidine residue of the α subunit is transiently phosphorylated. Many biochemical studies were done with the enzyme purified from E. coli Crooks strain (see citations in the Enzymatic Reaction summary), while mutant enzymes were obtained from the genes of a K-12-derived strain. A hybrid enzyme containing one wild-type and one catalytically inactive α subunit retains significant enzymatic activity, arguing for the presence of two independently active heterodimers . Crystal structures of the enzyme from various E. coli sources have been solved . The α2β2 heterotetramer is composed of two αβ heterodimers . Two possible alternative interpretations of the dimer-dimer interface were resolved by generating site-directed mutants that exist and are catalytically active as αβ heterodimers . Overlap of the sucC and sucD open reading frames suggests translational coupling . A sucCD insertion mutant does not grow aearobically on acetate or α-ketoglutarate or anaerobically on glucose or succinate as carbon sources. Expression of sucCD is higher under aerobic than anaerobic conditions and is induced by growth on acetate . A sucCD deletion mutant shows higher acetate accumulation and lower biomass formation than wild type on glucose minimal medium and can not re-utilize acetate that is secreted during growth on glucose . sucCD and sucAB are mutually essential. Both sets of genes encode an enzyme that can produce succinyl-CoA, an essential precursor for peptidoglycan biosynthesis; deletion of either set alone

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SUCCCOASYN-RXN|reaction.ecocyc.SUCCCOASYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A836|protein.P0A836]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0AGE9|protein.P0AGE9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:SUCCCOASYN`
- `PDB:1JKJ`
- `PDB:1JLL`
- `PDB:1SCU`
- `PDB:2SCU`
- `PDB:2NUA`
- `PDB:2NU9`
- `PDB:2NU8`
- `PDB:2NU7`
- `QSPROTEOME:QS00173719`

## Notes

2*protein.P0AGE9|2*protein.P0A836
