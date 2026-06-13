---
entity_id: "gene.b0169"
entity_type: "gene"
name: "rpsB"
source_database: "NCBI RefSeq"
source_id: "gene-b0169"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0169"
  - "rpsB"
---

# rpsB

`gene.b0169`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0169`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsB (gene.b0169) is a gene entity. It encodes rpsB (protein.P0A7V0). Encoded protein function: FUNCTION: Required for ribosomal protein bS1 (rpsA) to bind to the 30S subunit. {ECO:0000269|PubMed:12068815}. EcoCyc product frame: EG10901-MONOMER. Genomic coordinates: 189874-190599. EcoCyc protein note: The S2 protein, a component of the 30S subunit of the ribosome, is essential in E. coli . S2 is required for S1 binding to the ribosome . Overexpression of csdA, a DEAD-box RNA helicase, supresses the defect of a temperature-sensitive allele of rpsB by restoring assembly of both S1 and S2 with the ribosome at the non-permissive temperature . Expression of S2 is autoregulated, involving conserved elements located in the 5' UTR of the rpsB-tsf mRNA. Regulation may also involve the S1 protein . Purified S2 protein binds to inorganic polyphosphate (polyP). In the presence of polyP, S2 forms a complex with the Lon protease and is degraded by it . S2 was also shown to crosslink to IF3 . A protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions found that the PEI RpsB-ADHE-MONOMER AdhE may have a previously unknown role in regulating metabolism, in part because the PEI is conserved across many other bacterial taxa...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7V0|protein.P0A7V0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpsB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000575,ECOCYC:EG10901,GeneID:947874`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:189874-190599:+; feature_type=gene
