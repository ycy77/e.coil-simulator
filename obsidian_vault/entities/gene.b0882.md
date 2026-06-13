---
entity_id: "gene.b0882"
entity_type: "gene"
name: "clpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0882"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0882"
  - "clpA"
---

# clpA

`gene.b0882`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0882`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clpA (gene.b0882) is a gene entity. It encodes clpA (protein.P0ABH9). Encoded protein function: FUNCTION: ATP-dependent specificity component of the ClpAP protease. It directs the protease to specific substrates. It has unfoldase activity. The primary function of the ClpA-ClpP complex appears to be the degradation of unfolded or abnormal proteins. EcoCyc product frame: EG10156-MONOMER. EcoCyc synonyms: lopD. Genomic coordinates: 923264-925540.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABH9|protein.P0ABH9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=clpA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003001,ECOCYC:EG10156,GeneID:945764`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:923264-925540:+; feature_type=gene
