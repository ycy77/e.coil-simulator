---
entity_id: "gene.b0160"
entity_type: "gene"
name: "dgt"
source_database: "NCBI RefSeq"
source_id: "gene-b0160"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0160"
  - "dgt"
---

# dgt

`gene.b0160`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0160`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgt (gene.b0160) is a gene entity. It encodes dgt (protein.P15723). Encoded protein function: FUNCTION: dGTPase preferentially hydrolyzes dGTP over the other canonical NTPs. {ECO:0000255|HAMAP-Rule:MF_00030, ECO:0000269|PubMed:2826481}. EcoCyc product frame: DGTPTRIPHYDRO-MONOMER. EcoCyc synonyms: optA. Genomic coordinates: 179237-180754. EcoCyc protein note: Deoxyguanosinetriphosphate triphosphohydrolase (dGTPase, Dgt) is a unique nucleoside triphosphatase which specifically hydrolyzes dGTP to deoxyguanosine and inorganic tripolyphosphate . Possible physiological roles of the enzyme have only recently been elucidated. Dgt may be involved in replication fidelity via its effect on the cellular pool of dGTP . The level of Dgt expression correlates with the ability of cells to salvage thymine in the absence of functional de novo biosynthesis in a thyA mutant, presumably due to its effect on the intracellular deoxyribose-1-phosphate pool . dGTPase is able to bind single-stranded DNA with relatively high affinity . Crystal structures of the enzyme have been solved . Although dGTPase was thought to be a homotetramer based on a prior measurement of its native molecular weight , the crystal structure showed a homohexameric conformation. Subunits with bound ssDNA show significant conformational changes, including in the active site...

## Biological Role

Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15723|protein.P15723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000548,ECOCYC:EG10225,GeneID:947177`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:179237-180754:+; feature_type=gene
