---
entity_id: "complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX"
entity_type: "complex"
name: "cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase"
source_database: "EcoCyc"
source_id: "CYSTATHIONINE-BETA-LYASE-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cystathionine β-lyase / L-cysteine desulfhydrase / alanine racemase

`complex.ecocyc.CYSTATHIONINE-BETA-LYASE-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CYSTATHIONINE-BETA-LYASE-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P06721|protein.P06721]]

## Enriched Summary

Cystathionine β-lyase (CBL, MetC) catalyzes the cleavage of cystathionine to homocysteine in the L-methionine biosynthesis pathway . MetC is a member of the γ-family of PLP-dependent enzymes . It cleaves Cβ-S bonds of a variety of substrates. Crystal structures of CBL have been solved . The enzyme is composed of four identical subunits that contain one molecule each of PLP (pyridoxal 5'-phosphate) as a cofactor, transiently bound at the active site through a Schiff base with lysine 210 . A reaction mechanism has been proposed . Site-directed mutagenesis studies have suggested that the active site residues R58, W340 and R372 are interacting with the substrate L-cystathionine . Additional mutants in conserved residues have identified Y238 as a determinant for substrate specificity and S339 as a determinant of reaction specificity . Conformational changes in CBL have also been probed by site-directed mutagenesis of six tryptophan residues using kinetic and biophysical techniques. The results suggested that Trp188 is a useful probe of active site changes . Coregulation (repression by methionine) of cystathionine β-lyase (MetC) and cysteine desulfhydrase (CD) activities suggested that the same enzyme was able to catalyze both the CBL and the CD reactions . Purification and analysis of a ΔmetC mutant confirmed that MetC also exhibits CD activity in E. coli...

## Biological Role

Catalyzes ALARACECAT-RXN (reaction.ecocyc.ALARACECAT-RXN), CYSTATHIONINE-BETA-LYASE-RXN (reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN), LCYSDESULF-RXN (reaction.ecocyc.LCYSDESULF-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Cystathionine β-lyase (CBL, MetC) catalyzes the cleavage of cystathionine to homocysteine in the L-methionine biosynthesis pathway . MetC is a member of the γ-family of PLP-dependent enzymes . It cleaves Cβ-S bonds of a variety of substrates. Crystal structures of CBL have been solved . The enzyme is composed of four identical subunits that contain one molecule each of PLP (pyridoxal 5'-phosphate) as a cofactor, transiently bound at the active site through a Schiff base with lysine 210 . A reaction mechanism has been proposed . Site-directed mutagenesis studies have suggested that the active site residues R58, W340 and R372 are interacting with the substrate L-cystathionine . Additional mutants in conserved residues have identified Y238 as a determinant for substrate specificity and S339 as a determinant of reaction specificity . Conformational changes in CBL have also been probed by site-directed mutagenesis of six tryptophan residues using kinetic and biophysical techniques. The results suggested that Trp188 is a useful probe of active site changes . Coregulation (repression by methionine) of cystathionine β-lyase (MetC) and cysteine desulfhydrase (CD) activities suggested that the same enzyme was able to catalyze both the CBL and the CD reactions . Purification and analysis of a ΔmetC mutant confirmed that MetC also exhibits CD activity in E. coli. The reaction of CBL involves cleavage of the carbon-sulfide bond of cystathionine (βC-S lyase), just as in CD. In addition to metC, disruption of tnaA, cysK, cysM and malY significantly decreases CD activity and is effective for overproduction of L-cysteine . MetC shares 31% identity and 36% overall amino acid sequence similarity with cystathionine γ-synthase (MetB), suggesting a common evolutionary origin . The determinan

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ALARACECAT-RXN|reaction.ecocyc.ALARACECAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN|reaction.ecocyc.CYSTATHIONINE-BETA-LYASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.LCYSDESULF-RXN|reaction.ecocyc.LCYSDESULF-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06721|protein.P06721]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CYSTATHIONINE-BETA-LYASE-CPLX`
- `QSPROTEOME:QS00207051`

## Notes

4*protein.P06721
