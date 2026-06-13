---
entity_id: "complex.ecocyc.PC00033"
entity_type: "complex"
name: "DNA-binding transcriptional repressor PurR"
source_database: "EcoCyc"
source_id: "PC00033"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PurR"
---

# DNA-binding transcriptional repressor PurR

`complex.ecocyc.PC00033`

## Static

- Type: `complex`
- Source: `EcoCyc:PC00033`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ACP7|protein.P0ACP7]]

## Enriched Summary

PurR dimer controls several genes involved in purine nucleotide biosynthesis and its own synthesis . This regulator necessarily binds two products of purine metabolism, hypoxanthine and guanine, to induce the conformational change that allows PurR to bind DNA . Inhibition of purR expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or pyocyanin . Based on ChIP-chip, gene expression, and computational analyses, new members of the PurR regulon have been identified . Many genes of the PurR regulon are induced under pH 5.8 . PurR belongs to the GalR/LacI family , and it shows 35%, 33%, and 26% identity with CytR, GalR, and LacI, respectively . As with other members of this group, PurR shows a helix-turn-helix motif in the N-terminal domain for DNA binding and a ligand-binding and dimerization motif in the C-terminal domain that shows similarity with ligand binding sites of periplasmic sugar-binding proteins . The two domains are connected by a hinge sequence that is also important for DNA binding and that can be cleaved by proteases when the protein is not bound to DNA . The members of the GalR/LacI family also have a partial conservation in their DNA-binding motif which has an imperfect dyad symmetry . The nonconserved nucleotides in the motif give specificity to each regulator...

## Biological Role

Component of DNA-binding transcriptional repressor PurR-hypoxanthine (complex.ecocyc.CPLX-123).

## Annotation

PurR dimer controls several genes involved in purine nucleotide biosynthesis and its own synthesis . This regulator necessarily binds two products of purine metabolism, hypoxanthine and guanine, to induce the conformational change that allows PurR to bind DNA . Inhibition of purR expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or pyocyanin . Based on ChIP-chip, gene expression, and computational analyses, new members of the PurR regulon have been identified . Many genes of the PurR regulon are induced under pH 5.8 . PurR belongs to the GalR/LacI family , and it shows 35%, 33%, and 26% identity with CytR, GalR, and LacI, respectively . As with other members of this group, PurR shows a helix-turn-helix motif in the N-terminal domain for DNA binding and a ligand-binding and dimerization motif in the C-terminal domain that shows similarity with ligand binding sites of periplasmic sugar-binding proteins . The two domains are connected by a hinge sequence that is also important for DNA binding and that can be cleaved by proteases when the protein is not bound to DNA . The members of the GalR/LacI family also have a partial conservation in their DNA-binding motif which has an imperfect dyad symmetry . The nonconserved nucleotides in the motif give specificity to each regulator . By using synthetic gene circuits, it was demonstrated that PurR changes its regulatory effect depending on the position of the binding site relative to the promoter . Except for the purR gene and purA, which both have two DNA-binding sites for PurR, all genes regulated by PurR in Escherichia coli have only one DNA-binding motif to bind the regulator . The DNA sequence recognized by PurR is among the most conserved sequences across 2,350 different E. coli

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-123|complex.ecocyc.CPLX-123]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ACP7|protein.P0ACP7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PC00033`
- `QSPROTEOME:QS00163233`

## Notes

2*protein.P0ACP7
