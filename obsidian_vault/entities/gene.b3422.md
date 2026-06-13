---
entity_id: "gene.b3422"
entity_type: "gene"
name: "rtcR"
source_database: "NCBI RefSeq"
source_id: "gene-b3422"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3422"
  - "rtcR"
---

# rtcR

`gene.b3422`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3422`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rtcR (gene.b3422) is a gene entity. It encodes rtcR (protein.P38035). Encoded protein function: FUNCTION: Transcriptional repressor of the rtcAB genes. Interacts with sigma-54. {ECO:0000269|PubMed:9738023}. EcoCyc product frame: EG12356-MONOMER. EcoCyc synonyms: yhgB. Genomic coordinates: 3558268-3559866. EcoCyc protein note: RtcR , "RNA terminal phosphate cyclase regulator," regulates the expression of genes involved in the ATP-dependent conversion of a 3'-phosphate at the end of RNA to 2',3'-cyclic phosphodiester . RtcR belongs to the group of σ54-dependent transcriptional regulators, which contain three domains: the sensory domain located in the N terminus, the central domain involved in ATP hydrolysis and interaction with σ54, and the C-terminal domain, which contains a helix-turn-helix motif. Although the C-terminal domain and the central domain from RtcR are similar to those of other members of this group, its N-terminal domain is not . The rtcR gene is transcribed divergently from the genes it regulates .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38035|protein.P38035]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011174,ECOCYC:EG12356,GeneID:947928`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3558268-3559866:+; feature_type=gene
