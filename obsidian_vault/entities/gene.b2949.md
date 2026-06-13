---
entity_id: "gene.b2949"
entity_type: "gene"
name: "yqgF"
source_database: "NCBI RefSeq"
source_id: "gene-b2949"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2949"
  - "yqgF"
---

# yqgF

`gene.b2949`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2949`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqgF (gene.b2949) is a gene entity. It encodes yqgF (protein.P0A8I1). Encoded protein function: FUNCTION: Involved in the processing of the 5'-end of pre-16S rRNA during 70S ribosome maturation (processing does not occur on total cellular RNA off the ribosome); may be a nuclease (PubMed:25545592). A temperature-sensitive yqgF mutant no longer grows when Rho or NusA are overproduced, and has reduced transcription of genes encoded downstream of Rho terminators; transcription increases again in the presence of the Rho inhibitor bicylomycin (PubMed:22353788). {ECO:0000269|PubMed:22353788, ECO:0000269|PubMed:25545592}. EcoCyc product frame: G7525-MONOMER. Genomic coordinates: 3093500-3093916. EcoCyc protein note: YqgF is an essential , broadly conserved protein in bacteria . The YqgF family of proteins exhibits similarity to the RuvC family of RNase H fold-containing proteins and may function as Holliday junction resolvases (HJRs) . YqgF is monomeric in solution in contrast to all known HJRs which form dimers . Genetic interaction screening suggests that YqgF functions during DNA damage repair . Purified YqgF has metal-dependent 3' to 5' exonuclease activity on ssDNA, cleaves ssRNA and RNA/DNA hybrids and binds to ssRNA, ssDNA, and DNA recombination intermediates (Holliday junction, replication fork and flap substrates)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8I1|protein.P0A8I1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009672,ECOCYC:G7525,GeneID:947439`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3093500-3093916:+; feature_type=gene
