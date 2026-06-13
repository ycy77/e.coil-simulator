---
entity_id: "complex.ecocyc.CPLX0-3461"
entity_type: "complex"
name: "ribonuclease E"
source_database: "EcoCyc"
source_id: "CPLX0-3461"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RNase E"
  - "Rne"
---

# ribonuclease E

`complex.ecocyc.CPLX0-3461`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-3461`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21513|protein.P21513]]

## Enriched Summary

Ribonuclease E (RNase E) is a single-strand-specific endonuclease that is essential for viability. It processes rRNA, tRNA and other RNAs, is involved in plasmid and phage stability and is part of the degradosome, a multienzyme complex involved in mRNA degradation. RNase E is involved in processing and cleavage of several rRNAs. It processes the 9S rRNA precursor to yield the mature 5S rRNA by cleaving quite near the 5' end and downstream from the 3' end of the final product . RNase E also participates in the 5' maturation of 16S rRNA from its 17S precursor, as well as being able to cleave single-stranded regions within mature 16S and 23S rRNAs . RNase E initiates the processing of both poly- and monicistronic tRNA transcripts, including those within rRNA transcripts, by cleaving within a few nucleotides of the mature 3' CCA terminus, thus allowing RNase P and other 3' to 5' exonucleases to complete tRNA maturation . RNase E similarly cleaves at the 3' CCA terminus of the ssrA RNA precursor to yield its final form . RNase E may also be involved in processing of the 5' leader of precursor tRNAs . Maturation of the three proline tRNAs utilizes RNase E to exonucleolytically remove the Rho-independent transcription terminator on the primary transcripts...

## Biological Role

Catalyzes 3.1.26.12-RXN (reaction.ecocyc.3.1.26.12-RXN), RXN-24136 (reaction.ecocyc.RXN-24136), endoribonuclease (reaction.ecocyc.RXN-24137), endoribonuclease (reaction.ecocyc.RXN0-6478), RXN0-6485 (reaction.ecocyc.RXN0-6485), RXN0-6521 (reaction.ecocyc.RXN0-6521), RXN0-6522 (reaction.ecocyc.RXN0-6522), RXN0-7479 (reaction.ecocyc.RXN0-7479). Component of RapZ-GlmZ-RnaseE (complex.ecocyc.CPLX0-10097), degradosome (complex.ecocyc.CPLX0-2381). Bound by Magnesium cation (molecule.C00305).

## Annotation

Ribonuclease E (RNase E) is a single-strand-specific endonuclease that is essential for viability. It processes rRNA, tRNA and other RNAs, is involved in plasmid and phage stability and is part of the degradosome, a multienzyme complex involved in mRNA degradation. RNase E is involved in processing and cleavage of several rRNAs. It processes the 9S rRNA precursor to yield the mature 5S rRNA by cleaving quite near the 5' end and downstream from the 3' end of the final product . RNase E also participates in the 5' maturation of 16S rRNA from its 17S precursor, as well as being able to cleave single-stranded regions within mature 16S and 23S rRNAs . RNase E initiates the processing of both poly- and monicistronic tRNA transcripts, including those within rRNA transcripts, by cleaving within a few nucleotides of the mature 3' CCA terminus, thus allowing RNase P and other 3' to 5' exonucleases to complete tRNA maturation . RNase E similarly cleaves at the 3' CCA terminus of the ssrA RNA precursor to yield its final form . RNase E may also be involved in processing of the 5' leader of precursor tRNAs . Maturation of the three proline tRNAs utilizes RNase E to exonucleolytically remove the Rho-independent transcription terminator on the primary transcripts . The RNase E activity requires the C nucleotide at the 5' end of the mature uncharged tRNA; when the 5' end C nucleotide is modified, other nucleases can carry out the 3' maturation reaction . See PWY0-1628 and PWY0-1625 as well as individual tRNA processing pathways. RNase E carries out the 3' processing of M1 mRNA, which codes for the catalytic subunit of RNase P . Other mRNA processing substrates include the cell division inhibitor DicF, the RNA polymerase sigma70 activity modulator 6S RNA, the polycistronic histidine ope

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.3.1.26.12-RXN|reaction.ecocyc.3.1.26.12-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24136|reaction.ecocyc.RXN-24136]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-24137|reaction.ecocyc.RXN-24137]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6478|reaction.ecocyc.RXN0-6478]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6485|reaction.ecocyc.RXN0-6485]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6521|reaction.ecocyc.RXN0-6521]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6522|reaction.ecocyc.RXN0-6522]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7479|reaction.ecocyc.RXN0-7479]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-10097|complex.ecocyc.CPLX0-10097]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P21513|protein.P21513]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-3461`
- `QSPROTEOME:QS00183261`

## Notes

4*protein.P21513
