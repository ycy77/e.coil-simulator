---
entity_id: "gene.b0220"
entity_type: "gene"
name: "ivy"
source_database: "NCBI RefSeq"
source_id: "gene-b0220"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0220"
  - "ivy"
---

# ivy

`gene.b0220`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0220`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ivy (gene.b0220) is a gene entity. It encodes ivy (protein.P0AD59). Encoded protein function: FUNCTION: Strong inhibitor of lysozyme C. EcoCyc product frame: G6104-MONOMER. EcoCyc synonyms: ykfE. Genomic coordinates: 240343-240816. EcoCyc protein note: Ivy acts as a homodimer that specifically binds and inhibits vertebrate C-type lysozyme, behaving like a slow tight binding inhibitor with a Ki of about 1 nM . Overproduction of Ivy stabilises a highly unstable MBP mutant; purified Ivy inhibits the aggregation of lactate dehydrogenase . Ivy has a signal peptide that is cleaved from the mature protein . Crystal structures of Ivy alone and in complex with hen egg white lysozyme have been solved, and site-directed mutagenesis confirms the importance of the His60 residue for inhibition . ivy is highly expressed during exponential and stationary phase . An ivy null mutant does not show increased sensitivity to hen egg white lysozyme due to protection of the peptidoglycan layer by the outer membrane. However, under conditions that permeabilize the outer membrane, such as high pressure or lactoferrin treatment or in a tolB mutant background , an ivy null mutant is sensitized to lysozyme. Ivy: "inhibitor of vertebrate lysozyme"

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD59|protein.P0AD59]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ivy; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000740,ECOCYC:G6104,GeneID:946530`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:240343-240816:+; feature_type=gene
