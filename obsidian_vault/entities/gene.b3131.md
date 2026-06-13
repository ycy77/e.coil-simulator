---
entity_id: "gene.b3131"
entity_type: "gene"
name: "agaR"
source_database: "NCBI RefSeq"
source_id: "gene-b3131"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3131"
  - "agaR"
---

# agaR

`gene.b3131`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3131`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

agaR (gene.b3131) is a gene entity. It encodes agaR (protein.P0ACK2). Encoded protein function: FUNCTION: Probable repressor for the aga operon for N-acetyl galactosamine transport and metabolism. EcoCyc product frame: G7630-MONOMER. EcoCyc synonyms: yhaW. Genomic coordinates: 3277856-3278665. EcoCyc protein note: "N-acetylgalactosamine repressor," AgaR, negatively controls the expression of the aga gene cluster, which is involved in transport and catabolism of N-acetylgalactosamine and d-galactosamine . It is negatively autoregulated and coordinately represses transcription of the divergent agaZVWEFA operon, which is related to transport and degradation of N-acetylgalactosamine . This repressor responds to N-acetylgalactosamine and d-galactosamine in the medium. As a member of the DeoR/GlpR family of transcriptional regulators , AgaR features an N-terminal domain containing a helix-turn-helix motif and a C-terminal domain that includes the key residues involved in co-inducer recognition and oligomerization . In accordance with other helix-turn-helix DNA-binding repressors, AgaR may bind to DNA as a tetramer. Although AgaR represses transcription, it appears to be able to stabilize the RNApol but causes a slow rate of promoter escape...

## Biological Role

Repressed by agaR (protein.P0ACK2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACK2|protein.P0ACK2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=agaR; function=+
- `represses` <-- [[protein.P0ACK2|protein.P0ACK2]] `RegulonDB` `S` - regulator=AgaR; target=agaR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010291,ECOCYC:G7630,GeneID:947636`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3277856-3278665:-; feature_type=gene
