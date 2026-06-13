---
entity_id: "gene.b3119"
entity_type: "gene"
name: "tdcR"
source_database: "NCBI RefSeq"
source_id: "gene-b3119"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3119"
  - "tdcR"
---

# tdcR

`gene.b3119`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3119`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdcR (gene.b3119) is a gene entity. It encodes tdcR (protein.P11866). Encoded protein function: FUNCTION: Probable trans-acting positive activator for the tdc operon. EcoCyc product frame: PD03292. Genomic coordinates: 3267380-3267598. EcoCyc protein note: During anaerobiosis, TdcR participates in controlling several genes involved in transport and metabolism of threonine and serine . TdcR has a helix-turn-helix motif that shows 25% and 35% identity to the same motifs of the transcriptional regulators NtrC and Fis, respectively . It appears that due to the fact that the tdcR gene shows poor codon usage and a poor Shine-Dalgarno sequence, it is weakly expressed . tdcR is transcribed alone and is located divergently in the genome from the operon (tdcABCD), whose transcription is activated by TdcR. The first gene of the operon codes for TdcA, a transcriptional regulator that probably interacts with TdcR to activate the transcription of the operon , and these two proteins appear to function together with CRP and IHF, proteins that bend the DNA, for this activation . tdc: "threonine dehydratase" .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11866|protein.P11866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=tdcR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010255,ECOCYC:EG10992,GeneID:944907`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3267380-3267598:+; feature_type=gene
