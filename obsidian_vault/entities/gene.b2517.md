---
entity_id: "gene.b2517"
entity_type: "gene"
name: "rlmN"
source_database: "NCBI RefSeq"
source_id: "gene-b2517"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2517"
  - "rlmN"
---

# rlmN

`gene.b2517`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2517`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rlmN (gene.b2517) is a gene entity. It encodes rlmN (protein.P36979). Encoded protein function: FUNCTION: Specifically methylates position 2 of adenine 2503 in 23S rRNA and position 2 of adenine 37 in tRNAs. m2A2503 modification seems to play a crucial role in the proofreading step occurring at the peptidyl transferase center and thus would serve to optimize ribosomal fidelity. Unmodified tRNA is not a suitable substrate for RlmN, which suggests that RlmN works in a late step during tRNA maturation. {ECO:0000269|PubMed:18025251, ECO:0000269|PubMed:21415317, ECO:0000269|PubMed:22891362}. EcoCyc product frame: EG12401-MONOMER. EcoCyc synonyms: yfgB. Genomic coordinates: 2643129-2644283. EcoCyc protein note: RlmN is the methyltransferase responsible for methylation of 23S rRNA at the C2 position of the A2503 nucleotide . The enzyme can utilize free 23S rRNA as the substrate, but not the fully assembled large ribosomal subunit . RlmN is also responsible for methylation of certain tRNAs at the C2 position of A37 . RlmN substrates and modification sites within the substrates have been determined . RlmN belongs to the Cfr/RlmN family of the "radical SAM" superfamily of proteins . The reaction requires two molecules of SAM, one as the methyl group donor, and the second as the source of the 5'-deoxyadenosyl radical...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36979|protein.P36979]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008287,ECOCYC:EG12401,GeneID:946249`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2643129-2644283:-; feature_type=gene
