---
entity_id: "complex.ecocyc.ASPKINIII-CPLX"
entity_type: "complex"
name: "aspartate kinase III"
source_database: "EcoCyc"
source_id: "ASPKINIII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "aspartokinase III"
  - "lysine-sensitive aspartokinase 3"
---

# aspartate kinase III

`complex.ecocyc.ASPKINIII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPKINIII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P08660|protein.P08660]]

## Enriched Summary

Aspartokinase III (LysC) is one of three aspartokinase activities catalyzing the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine. Aspartokinase III catalyzes the ATP-dependent phosphorylation of L-aspartate to yield L-aspartyl-4-phosphate . The enzyme from E. coli B has also been purified and characterized . Aspartokinase III consists of a dimer of LysC monomers. In the presence of lysine, it can instead adopt an inactive tetrameric conformation . Structures have been determined for both this inactive tetrameric form of LysC and for the active dimer bound to aspartate and ADP, to 2.8 Å and 2.5 Å resolution, respectively. Each individual LysC monomer has an amino-terminal catalytic domain (residues 3-291) and a carboxy-terminal regulatory domain (residues 300-349) . The entire region of residues 318-352 is involved in feedback regulation by lysine, as is Glu-250 . In the catalytic domain, Lys-8 and Asp-202 are important for enzyme function . A number of cis-dominant aspartokinase III mutants have been discovered . lysC gene expression is repressed by lysine, partially relieved from that repression by arginine, and derepressed substantially by combined methionine and threonine . Despite this regulation, the lysC promoter has no apparent attenuator sequence . Differential gene expression profiling of a lysC knockout strain of E...

## Biological Role

Catalyzes ASPARTATEKIN-RXN (reaction.ecocyc.ASPARTATEKIN-RXN).

## Annotation

Aspartokinase III (LysC) is one of three aspartokinase activities catalyzing the first step in the biosynthesis of lysine and homoserine, and indirectly methionine and threonine. Aspartokinase III catalyzes the ATP-dependent phosphorylation of L-aspartate to yield L-aspartyl-4-phosphate . The enzyme from E. coli B has also been purified and characterized . Aspartokinase III consists of a dimer of LysC monomers. In the presence of lysine, it can instead adopt an inactive tetrameric conformation . Structures have been determined for both this inactive tetrameric form of LysC and for the active dimer bound to aspartate and ADP, to 2.8 Å and 2.5 Å resolution, respectively. Each individual LysC monomer has an amino-terminal catalytic domain (residues 3-291) and a carboxy-terminal regulatory domain (residues 300-349) . The entire region of residues 318-352 is involved in feedback regulation by lysine, as is Glu-250 . In the catalytic domain, Lys-8 and Asp-202 are important for enzyme function . A number of cis-dominant aspartokinase III mutants have been discovered . lysC gene expression is repressed by lysine, partially relieved from that repression by arginine, and derepressed substantially by combined methionine and threonine . Despite this regulation, the lysC promoter has no apparent attenuator sequence . Differential gene expression profiling of a lysC knockout strain of E. coli K-12 W3110 in comparison with wild-type revealed effects on the expression of a number of different genes, mostly associated with amino acid biosynthesis and transport . An inhibitory effect of the lysine analog antibiotic S-(2-aminoethyl)-L-cysteine (AEC) on LysC activity was shown using E. coli strains expressing a promoterless lysC gene from a hybrid plasmid using a lac promoter . Later work

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P08660|protein.P08660]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ASPKINIII-CPLX`
- `QSPROTEOME:QS00183231`

## Notes

2*protein.P08660
