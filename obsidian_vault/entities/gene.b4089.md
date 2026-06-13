---
entity_id: "gene.b4089"
entity_type: "gene"
name: "alsR"
source_database: "NCBI RefSeq"
source_id: "gene-b4089"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4089"
  - "alsR"
---

# alsR

`gene.b4089`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4089`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

alsR (gene.b4089) is a gene entity. It encodes rpiR (protein.P0ACS7). Encoded protein function: FUNCTION: Regulatory protein involved in rpiB gene repression. Also involved in als operon repression. {ECO:0000269|PubMed:9401019}. EcoCyc product frame: G7821-MONOMER. EcoCyc synonyms: yjcY, rpiR. Genomic coordinates: 4312101-4312991. EcoCyc protein note: "Allose utilization regulator," AlsR, negatively controls the expression of genes involved in transport and catabolism of D-allose and low-affinity transport of D-ribose . It is negatively autoregulated and coordinately represses transcription of the divergent gene rpiB, encoding an enzyme in the pentose pathway . Synthesis of alsR and rpiB genes is induced when Escherichia coli is grown on D-allose in the absence of glucose. Gene induction occurs when the physiological inducer, D-allose, binds to AlsR, liberating the repression effect caused by this protein . As a member of the RpiR/YebK/YfhH family of transcriptional regulators, AlsR features an N-terminal domain containing a helix-turn-helix motif . Currently, no DNA-binding sites for this regulator have been reported in the literature.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACS7|protein.P0ACS7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=alsR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013400,ECOCYC:G7821,GeneID:948603`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4312101-4312991:-; feature_type=gene
