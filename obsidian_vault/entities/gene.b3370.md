---
entity_id: "gene.b3370"
entity_type: "gene"
name: "frlA"
source_database: "NCBI RefSeq"
source_id: "gene-b3370"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3370"
  - "frlA"
---

# frlA

`gene.b3370`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3370`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frlA (gene.b3370) is a gene entity. It encodes frlA (protein.P45539). Encoded protein function: FUNCTION: Is likely involved in the transport of fructoselysine and psicoselysine to the cytoplasm, where they are degraded. {ECO:0000305|PubMed:12147680, ECO:0000305|PubMed:14641112}. EcoCyc product frame: YHFM-MONOMER. EcoCyc synonyms: yhfM. Genomic coordinates: 3499910-3501247. EcoCyc protein note: FrlA is an uncharacterized member of the APC superfamily of amino acid transporters . Based on the activities of FrlB and FrlD, FrlA is suggested to transport fructoselysine, which can be utilized as a carbon source . A frlA mutant is unable to grow on 20mM fructoselysine or psicoselysine as the sole source of carbon . FrlA: "fructoselysine"

## Biological Role

Repressed by frlR (protein.P45544).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45539|protein.P45539]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P45544|protein.P45544]] `RegulonDB` `C` - regulator=FrlR; target=frlA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011019,ECOCYC:EG12908,GeneID:947878`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3499910-3501247:+; feature_type=gene
