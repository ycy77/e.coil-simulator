---
entity_id: "gene.b0043"
entity_type: "gene"
name: "fixC"
source_database: "NCBI RefSeq"
source_id: "gene-b0043"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0043"
  - "fixC"
---

# fixC

`gene.b0043`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0043`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fixC (gene.b0043) is a gene entity. It encodes fixC (protein.P68644). Encoded protein function: FUNCTION: Could be part of an electron transfer system required for anaerobic carnitine reduction. EcoCyc product frame: EG11564-MONOMER. EcoCyc synonyms: yaaS. Genomic coordinates: 44180-45466. EcoCyc protein note: The fix operon is co-regulated with the adjacent and divergently transcribed cai operon, suggesting that the gene products may also be involved in anaerobic metabolism of carnitine . The fix operon is expressed under anaerobic conditions in the presence of carnitine or crotonobetaine . Chromosomal insertion mutants in fix genes have a growth defect under anaerobic conditions . Work by was performed with genes from E. coli strain O44 K74, which was isolated from the intestine of a rat after a carnitine rich diet and selected for high carnitine metabolism activity.

## Biological Role

Activated by rpoD (protein.P00579), caiF (protein.P0AE58).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68644|protein.P68644]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fixC; function=+
- `activates` <-- [[protein.P0AE58|protein.P0AE58]] `RegulonDB` `S` - regulator=CaiF; target=fixC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000149,ECOCYC:EG11564,GeneID:948958`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:44180-45466:+; feature_type=gene
