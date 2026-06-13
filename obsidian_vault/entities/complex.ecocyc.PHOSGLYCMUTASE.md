---
entity_id: "complex.ecocyc.PHOSGLYCMUTASE"
entity_type: "complex"
name: "2,3-bisphosphoglycerate-dependent phosphoglycerate mutase"
source_database: "EcoCyc"
source_id: "PHOSGLYCMUTASE"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "BPG-dependent PGAM1"
  - "PGAM 1"
  - "dPGM"
---

# 2,3-bisphosphoglycerate-dependent phosphoglycerate mutase

`complex.ecocyc.PHOSGLYCMUTASE`

## Static

- Type: `complex`
- Source: `EcoCyc:PHOSGLYCMUTASE`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P62707|protein.P62707]]

## Enriched Summary

E. coli contains both a 2,3-bisphosphoglyerate-dependent (dPGM, GpmA) and a cofactor-independent (iPGM, GpmM) phosphoglycerate mutase. The dPGM enzyme has significantly higher specific activity . Differential inhibition by vanadate allowed independent measurement of both enzymes during the E. coli growth cycle . The kinetic properties of the enzymes of the glycolysis pathway have been measured in an in vivo-like assay medium . GpmA is prone to non-enzymatic acetylation of K100. Acetylation at this position inhibits the enzyme activity by interfering with substrate binding, and can occur in vivo under physiological conditions favoring acetyl phosphate production . Crystal structures of the enzyme have been solved at 1.25 Å and 1.3 Å resolution. The active site His10 residue is phosphorylated in approximately 1/4 of the polypeptides in the structure and may represent the active form of the enzyme . The crystal structure of the enzyme in complex with the inhibitor vanadate resembles that of the inactive dephosphorylated dPGM of Saccharomyces cerevisiae . A proteomics approach identified GpmA as an ATP-binding protein whose thermodynamic stability is increased in the presence of ATP . During equilibrium unfolding in the absence of ATP, GpmA forms a partially unfolded, monomeric intermediate . Active site residues are involved in ATP binding...

## Biological Role

Catalyzes RXN-15513 (reaction.ecocyc.RXN-15513). Bound by 2,3-Bisphospho-D-glycerate (molecule.C01159).

## Annotation

E. coli contains both a 2,3-bisphosphoglyerate-dependent (dPGM, GpmA) and a cofactor-independent (iPGM, GpmM) phosphoglycerate mutase. The dPGM enzyme has significantly higher specific activity . Differential inhibition by vanadate allowed independent measurement of both enzymes during the E. coli growth cycle . The kinetic properties of the enzymes of the glycolysis pathway have been measured in an in vivo-like assay medium . GpmA is prone to non-enzymatic acetylation of K100. Acetylation at this position inhibits the enzyme activity by interfering with substrate binding, and can occur in vivo under physiological conditions favoring acetyl phosphate production . Crystal structures of the enzyme have been solved at 1.25 Å and 1.3 Å resolution. The active site His10 residue is phosphorylated in approximately 1/4 of the polypeptides in the structure and may represent the active form of the enzyme . The crystal structure of the enzyme in complex with the inhibitor vanadate resembles that of the inactive dephosphorylated dPGM of Saccharomyces cerevisiae . A proteomics approach identified GpmA as an ATP-binding protein whose thermodynamic stability is increased in the presence of ATP . During equilibrium unfolding in the absence of ATP, GpmA forms a partially unfolded, monomeric intermediate . Active site residues are involved in ATP binding. A structural model for cooperativity between folding of the active site and dimerization has been proposed and tested . A gpmA deletion strain shows a growth lag in minimal medium, which may be due to a delay in exiting stationary phase. This phenotype can be rescued by expression of either gpmA or gpmM from a medium-copy plasmid. A gpmA gpmM double mutant strain does not appear to be viable . Transcription of gpmA is regulated by Fur .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15513|reaction.ecocyc.RXN-15513]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C01159|molecule.C01159]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P62707|protein.P62707]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PHOSGLYCMUTASE`
- `QSPROTEOME:QS00197419`

## Notes

2*protein.P62707
