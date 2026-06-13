---
entity_id: "complex.ecocyc.CPLX0-8581"
entity_type: "complex"
name: "ATP-dependent helicase/uracil glycosylase Lhr"
source_database: "EcoCyc"
source_id: "CPLX0-8581"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ATP-dependent helicase Lhr"
---

# ATP-dependent helicase/uracil glycosylase Lhr

`complex.ecocyc.CPLX0-8581`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8581`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P30015|protein.P30015]]

## Enriched Summary

Lhr is an ATP-dependent helicase and can translocate 3' to 5' on single-stranded DNA; it is also a uracil-DNA glycosylase, contributing to DNA repair . The helicase is more active on DNA:RNA duplexes than on DNA:DNA duplexes and requires a ssDNA 3' end for loading. In vitro, purified Lhr has divalent cation-dependent ATPase activity that is not dependent on an added nucleic acid . Lhr is a large protein with conserved motifs from helicase superfamily II . The Mycobacterium smegmatis Lhr homolog was first to be characterized as an ATP-dependent 3'-to-5' DNA translocase and helicase . Purified Lhr has a homooligomeric quarternary structure; the C-terminal domain appears to be responsible for homooligomerization. A cryo-EM structure of the homologous M. smegmatis Lhr C-terminal domain shows a homotetramer . Mutagenesis of the putative metal-binding motif (D179A-E180A) eliminates ATPase activity of Lhr, while a W620A mutant can hydrolyze ATP, but only has residual helicase activity . Mutational studies pinpointed Asp-1536 in the C-terminal domain as essential to the uracil-DNA glycosylase activity; it was also found to be functionally separate from the helicase activity . lhr insertion mutants have no obvious growth defect . Mutations in lhr are synergistic with mutations in radA for sensitivity to the DNA damaging agent azidothymidine...

## Biological Role

Catalyzes ATPASE-RXN (reaction.ecocyc.ATPASE-RXN), RXN0-2584 (reaction.ecocyc.RXN0-2584), RXN0-7388 (reaction.ecocyc.RXN0-7388). Bound by Ca2+ (molecule.ecocyc.CA_2).

## Annotation

Lhr is an ATP-dependent helicase and can translocate 3' to 5' on single-stranded DNA; it is also a uracil-DNA glycosylase, contributing to DNA repair . The helicase is more active on DNA:RNA duplexes than on DNA:DNA duplexes and requires a ssDNA 3' end for loading. In vitro, purified Lhr has divalent cation-dependent ATPase activity that is not dependent on an added nucleic acid . Lhr is a large protein with conserved motifs from helicase superfamily II . The Mycobacterium smegmatis Lhr homolog was first to be characterized as an ATP-dependent 3'-to-5' DNA translocase and helicase . Purified Lhr has a homooligomeric quarternary structure; the C-terminal domain appears to be responsible for homooligomerization. A cryo-EM structure of the homologous M. smegmatis Lhr C-terminal domain shows a homotetramer . Mutagenesis of the putative metal-binding motif (D179A-E180A) eliminates ATPase activity of Lhr, while a W620A mutant can hydrolyze ATP, but only has residual helicase activity . Mutational studies pinpointed Asp-1536 in the C-terminal domain as essential to the uracil-DNA glycosylase activity; it was also found to be functionally separate from the helicase activity . lhr insertion mutants have no obvious growth defect . Mutations in lhr are synergistic with mutations in radA for sensitivity to the DNA damaging agent azidothymidine . When lhr is deleted, cells are more sensitive to oxidative stress from hydrogen peroxide and azidothymidine . lhr appears to be poorly expressed under typical growth conditions . Lhr: long helicase related

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ATPASE-RXN|reaction.ecocyc.ATPASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-2584|reaction.ecocyc.RXN0-2584]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7388|reaction.ecocyc.RXN0-7388]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P30015|protein.P30015]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-8581`

## Notes

4*protein.P30015
