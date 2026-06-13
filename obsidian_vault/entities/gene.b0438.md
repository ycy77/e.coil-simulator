---
entity_id: "gene.b0438"
entity_type: "gene"
name: "clpX"
source_database: "NCBI RefSeq"
source_id: "gene-b0438"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0438"
  - "clpX"
---

# clpX

`gene.b0438`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0438`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

clpX (gene.b0438) is a gene entity. It encodes clpX (protein.P0A6H1). Encoded protein function: FUNCTION: ATP-dependent specificity component of the Clp protease. Uses cycles of ATP binding and hydrolysis to unfold proteins and translocate them to the ClpP protease. It directs the protease to specific substrates both with and without the help of adapter proteins such as SspB. Participates in the final steps of RseA-sigma-E degradation, liberating sigma-E to induce the extracytoplasmic-stress response. It may bind to the lambda O substrate protein and present it to the ClpP protease in a form that can be recognized and readily hydrolyzed by ClpP. Can perform chaperone functions in the absence of ClpP. {ECO:0000269|PubMed:12941278, ECO:0000269|PubMed:15371343}. EcoCyc product frame: EG10159-MONOMER. EcoCyc synonyms: lopC. Genomic coordinates: 457426-458700.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6H1|protein.P0A6H1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=clpX; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=clpX; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=clpX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001517,ECOCYC:EG10159,GeneID:945083`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:457426-458700:+; feature_type=gene
