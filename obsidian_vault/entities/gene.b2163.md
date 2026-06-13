---
entity_id: "gene.b2163"
entity_type: "gene"
name: "yeiL"
source_database: "NCBI RefSeq"
source_id: "gene-b2163"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2163"
  - "yeiL"
---

# yeiL

`gene.b2163`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2163`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiL (gene.b2163) is a gene entity. It encodes yeiL (protein.P0A9E9). Encoded protein function: FUNCTION: Transcription regulator involved in mid-term, stationary-phase viability under nitrogen starvation. Might control expression of the salvage pathways or in some other way repress the recycling of nucleobases to nucleic acids and enhance their use as general nitrogen sources during nitrogen-limited growth. {ECO:0000269|PubMed:11101674}. EcoCyc product frame: EG12031-MONOMER. Genomic coordinates: 2255355-2256014. EcoCyc protein note: The genes regulated by the YeiL transcriptional activator have not been identified yet, but it has been proposed that this protein might regulate genes involved in post-exponential-phase nitrogen starvation. A gene encoding a potential nucleoside hydrolase and transcribed divergently from yeiL has also been suggested to be subject to YeiL regulation . Inhibition of yeiL expression by CRISPRi reduced cellular fitness under treatment with the antibiotic carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . YeiL, the third member of the CRP/FNR family, has the main structural elements conserved in Crp and Fnr, such as a sensory domain, an α-helix that serves as a dimer interface, and a DNA-recognition helix also found in Fnr. However, the specific residues in the helix for DNA binding are not conserved...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9E9|protein.P0A9E9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007160,ECOCYC:EG12031,GeneID:946670`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2255355-2256014:+; feature_type=gene
