---
entity_id: "protein.P0A9J0"
entity_type: "protein"
name: "rng"
source_database: "UniProt"
source_id: "P0A9J0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:22509045, ECO:0000305|PubMed:14622423}. Cell inner membrane {ECO:0000269|PubMed:22509045}; Peripheral membrane protein {ECO:0000305|PubMed:22509045}. Cytoplasm, cytoskeleton {ECO:0000303|PubMed:8300545}. Note=Possible cytoskeletal location is upon overproduction. {ECO:0000303|PubMed:8300545}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rng cafA orfF yhdF b3247 JW3216"
---

# rng

`protein.P0A9J0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9J0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:22509045, ECO:0000305|PubMed:14622423}. Cell inner membrane {ECO:0000269|PubMed:22509045}; Peripheral membrane protein {ECO:0000305|PubMed:22509045}. Cytoplasm, cytoskeleton {ECO:0000303|PubMed:8300545}. Note=Possible cytoskeletal location is upon overproduction. {ECO:0000303|PubMed:8300545}.

## Enriched Summary

FUNCTION: An endonuclease that acts in the processing of the 5'-end of precursors of 16S rRNA, generates a precursor with 3 extra nucleotides at its 5'-end (which is matured by Rnm) (PubMed:10329633, PubMed:10362534, PubMed:10722715, PubMed:20176963, PubMed:24489121, PubMed:26694614, PubMed:32343306). It prefers 5'-monophosphorylated over 5'-OH or 5'-triphosphorylated substrates and cleaves single-stranded sites rich in A and U residues; contributes to RNA turnover (PubMed:10722715, PubMed:10762247, PubMed:11380618, PubMed:12450135, PubMed:18078441, PubMed:21717341). 5'-monophosphate-assisted cleavage requires at least 2 and preferably 3 or more unpaired 5'-terminal nucleotides for cleavage. The optimal spacing between the 5' end and the scissile phosphate appears to be 6 nucleotides. Any sequence of unpaired nucleotides at the 5'-end is tolerated (PubMed:26694614). Processes the 5'-end precursors of 23S rRNA (PubMed:21717341). Participates in processing of tRNA(Pro) (proK and proM) (PubMed:27288443). Also involved in metabolism of some mRNAs (PubMed:11380618, PubMed:12450135, PubMed:18078441). Cells overproducing this protein form chains of cell with cytoplasmic axial filaments (PubMed:8300545). Could be involved in chromosome segregation and cell division...

## Biological Role

Component of RNase G (complex.ecocyc.CPLX0-1621).

## Annotation

FUNCTION: An endonuclease that acts in the processing of the 5'-end of precursors of 16S rRNA, generates a precursor with 3 extra nucleotides at its 5'-end (which is matured by Rnm) (PubMed:10329633, PubMed:10362534, PubMed:10722715, PubMed:20176963, PubMed:24489121, PubMed:26694614, PubMed:32343306). It prefers 5'-monophosphorylated over 5'-OH or 5'-triphosphorylated substrates and cleaves single-stranded sites rich in A and U residues; contributes to RNA turnover (PubMed:10722715, PubMed:10762247, PubMed:11380618, PubMed:12450135, PubMed:18078441, PubMed:21717341). 5'-monophosphate-assisted cleavage requires at least 2 and preferably 3 or more unpaired 5'-terminal nucleotides for cleavage. The optimal spacing between the 5' end and the scissile phosphate appears to be 6 nucleotides. Any sequence of unpaired nucleotides at the 5'-end is tolerated (PubMed:26694614). Processes the 5'-end precursors of 23S rRNA (PubMed:21717341). Participates in processing of tRNA(Pro) (proK and proM) (PubMed:27288443). Also involved in metabolism of some mRNAs (PubMed:11380618, PubMed:12450135, PubMed:18078441). Cells overproducing this protein form chains of cell with cytoplasmic axial filaments (PubMed:8300545). Could be involved in chromosome segregation and cell division. It may be one of the components of the cytoplasmic axial filaments bundles, or merely regulate the formation of this structure (Probable). {ECO:0000269|PubMed:10329633, ECO:0000269|PubMed:10362534, ECO:0000269|PubMed:10722715, ECO:0000269|PubMed:10762247, ECO:0000269|PubMed:11380618, ECO:0000269|PubMed:12450135, ECO:0000269|PubMed:18078441, ECO:0000269|PubMed:20176963, ECO:0000269|PubMed:21717341, ECO:0000269|PubMed:24489121, ECO:0000269|PubMed:26694614, ECO:0000269|PubMed:27288443, ECO:0000269|PubMed:32343306, ECO:0000269|PubMed:8300545, ECO:0000305|PubMed:8300545}.; FUNCTION: Confers adaptive resistance to aminoglycoside antibiotics through modulation of 16S rRNA processing. {ECO:0000269|PubMed:24489121}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1621|complex.ecocyc.CPLX0-1621]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3247|gene.b3247]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9J0`
- `KEGG:ecj:JW3216;eco:b3247;ecoc:C3026_17655;`
- `GeneID:86862365;93778739;947744;`
- `GO:GO:0000049; GO:0004521; GO:0004540; GO:0005737; GO:0005856; GO:0005886; GO:0006364; GO:0008033; GO:0016787; GO:0019843; GO:0030490; GO:0042803; GO:0046872; GO:0051301`
- `EC:3.1.26.-`

## Notes

Ribonuclease G (RNase G) (EC 3.1.26.-) (Cytoplasmic axial filament protein) (CafA protein)
