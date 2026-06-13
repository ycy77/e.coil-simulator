---
entity_id: "complex.ecocyc.CPLX0-303"
entity_type: "complex"
name: "fructose-1,6-bisphosphatase 2"
source_database: "EcoCyc"
source_id: "CPLX0-303"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "FBPase II"
  - "fructose-bisphosphatase class II"
---

# fructose-1,6-bisphosphatase 2

`complex.ecocyc.CPLX0-303`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-303`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A9C9|protein.P0A9C9]]

## Enriched Summary

The glpX gene encodes a Type II fructose 1,6-bisphosphatase (FBPase II). Its enzymatic properties are distinct from those of F16B-CPLX "FBPase I" . Crystal structures of free GlpX and GlpX complexed with substrate or inorganic phosphate have been solved; the enzyme forms an elongated dimer in the crystal. A catalytic mechanism has been proposed . When FBPase I is present, FBPase II is not essential for growth; a glpX mutant strain grows normally on gluconeogenic substrates, although increased expression of glpX from a multicopy plasmid complements an Fbp- phenotype . Enzymes with mutations in predicted active site residues have been isolated, and their enzymatic properties have been measured . The glpX gene was initially identified as a gene of unknown function belonging to the glpFKX operon of the glp regulon . GlpX shares only 10% amino acid sequence identity with FBPase I . E. coli also has a second Type II FBPase, CPLX0-7776 "YggF". GlpX has a catalytic efficiency three times higher than YggF, but a lower catalytic efficiency and substrate affinity than Fbp . In metabolic engineering studies, overexpression of glpX enhanced gluconeogenic flux, activating the pentose phosphate pathway and increasing hydrogen yield in strains of E. coli containing a ferredoxin-dependent hydrogenase system...

## Biological Role

Catalyzes F16BDEPHOS-RXN (reaction.ecocyc.F16BDEPHOS-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

The glpX gene encodes a Type II fructose 1,6-bisphosphatase (FBPase II). Its enzymatic properties are distinct from those of F16B-CPLX "FBPase I" . Crystal structures of free GlpX and GlpX complexed with substrate or inorganic phosphate have been solved; the enzyme forms an elongated dimer in the crystal. A catalytic mechanism has been proposed . When FBPase I is present, FBPase II is not essential for growth; a glpX mutant strain grows normally on gluconeogenic substrates, although increased expression of glpX from a multicopy plasmid complements an Fbp- phenotype . Enzymes with mutations in predicted active site residues have been isolated, and their enzymatic properties have been measured . The glpX gene was initially identified as a gene of unknown function belonging to the glpFKX operon of the glp regulon . GlpX shares only 10% amino acid sequence identity with FBPase I . E. coli also has a second Type II FBPase, CPLX0-7776 "YggF". GlpX has a catalytic efficiency three times higher than YggF, but a lower catalytic efficiency and substrate affinity than Fbp . In metabolic engineering studies, overexpression of glpX enhanced gluconeogenic flux, activating the pentose phosphate pathway and increasing hydrogen yield in strains of E. coli containing a ferredoxin-dependent hydrogenase system . Co-overexpression of glpX and tktA improved L-phenylalanine production from glycerol in recombinant E. coli strains . Deletion of glpX strongly increased acrAB expression in wild-type E. coli BW25113, although the cause of the induction remains unclear .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A9C9|protein.P0A9C9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-303`
- `QSPROTEOME:QS00049586`

## Notes

2*protein.P0A9C9
