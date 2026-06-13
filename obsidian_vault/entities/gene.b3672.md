---
entity_id: "gene.b3672"
entity_type: "gene"
name: "ivbL"
source_database: "NCBI RefSeq"
source_id: "gene-b3672"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3672"
  - "ivbL"
---

# ivbL

`gene.b3672`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3672`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ivbL (gene.b3672) is a gene entity. It encodes ivbL (protein.P03061). Encoded protein function: FUNCTION: This protein is involved in control of the biosynthesis of isoleucine, leucine, and valine. EcoCyc product frame: EG11275-MONOMER. Genomic coordinates: 3852890-3852988. EcoCyc protein note: The ilvBN operon leader peptide (IvbL) controls by attenuation the expression of the TU00032 operon, which codes for an enzyme involved in isoleucine and valine biosynthesis. The attenuator region contains both valine and leucine residues and several potential stem-loop structures, yielding negative regulation in response to valine and leucine levels. It also contains regions similar to those found in CRP-dependent promoters, yielding positive regulation in response to cyclic AMP and CRP .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P03061|protein.P03061]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ivbL; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ivbL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012002,ECOCYC:EG11275,GeneID:948181`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3852890-3852988:-; feature_type=gene
