---
entity_id: "gene.b1338"
entity_type: "gene"
name: "abgA"
source_database: "NCBI RefSeq"
source_id: "gene-b1338"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1338"
  - "abgA"
---

# abgA

`gene.b1338`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1338`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abgA (gene.b1338) is a gene entity. It encodes abgA (protein.P77357). Encoded protein function: FUNCTION: Component of the p-aminobenzoyl-glutamate hydrolase multicomponent enzyme system which catalyzes the cleavage of p-aminobenzoyl-glutamate (PABA-GLU) to form p-aminobenzoate (PABA) and glutamate. AbgAB does not degrade dipeptides and the physiological role of abgABT should be clarified. {ECO:0000269|PubMed:17307853, ECO:0000269|PubMed:20190044}. EcoCyc product frame: G6670-MONOMER. EcoCyc synonyms: ydaJ. Genomic coordinates: 1403255-1404565. EcoCyc protein note: Transcription of the potential abgABT operon may be regulated by the predicted transcriptional regulator AbgR . AbgA: "p-aminobenzoyl-glutamate utilization"

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77357|protein.P77357]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=abgA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004493,ECOCYC:G6670,GeneID:945742`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1403255-1404565:-; feature_type=gene
