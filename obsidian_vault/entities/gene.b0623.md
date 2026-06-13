---
entity_id: "gene.b0623"
entity_type: "gene"
name: "cspE"
source_database: "NCBI RefSeq"
source_id: "gene-b0623"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0623"
  - "cspE"
---

# cspE

`gene.b0623`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0623`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspE (gene.b0623) is a gene entity. It encodes cspE (protein.P0A972). Encoded protein function: Cold shock-like protein CspE (CSP-E) EcoCyc product frame: EG12179-MONOMER. EcoCyc synonyms: gicA, msmC. Genomic coordinates: 657292-657501. EcoCyc protein note: CspE belongs to the cold shock family of proteins and functions as a transcription antiterminator at ρ-independent terminators both in vitro and in vivo . The nucleic acid melting activity of CspE is required for its transcription antitermination activity ; the melting activity of CspE point mutants and wild-type on DNA substrates has been studied. Purified CspE protein binds to poly(A) RNA tails and impedes poly(A)-mediated mRNA decay and internal mRNA cleavage by polynucleotide phosphorylase and RNase E . CspE inhibits the expression of cspA in vitro by increasing pause recognition by RNA polymerase at the cspA "cold box" . Initial results showed that CspE interacts with nascent RNA in an initial transcribing complex and inhibits Q-mediated transcription antitermination at the λ PR' promoter . Although CspE did not appear to interact with free RNA , it was later shown to interact with both RNA and DNA; a consensus sequence for selective RNA binding has been determined using an in vitro selection approach...

## Biological Role

Activated by crp (protein.P0ACJ8), ydiP (protein.P77402).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A972|protein.P0A972]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=cspE; function=+
- `activates` <-- [[protein.P77402|protein.P77402]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002142,ECOCYC:EG12179,GeneID:947024`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:657292-657501:+; feature_type=gene
