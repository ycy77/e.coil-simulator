---
entity_id: "gene.b1096"
entity_type: "gene"
name: "pabC"
source_database: "NCBI RefSeq"
source_id: "gene-b1096"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1096"
  - "pabC"
---

# pabC

`gene.b1096`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1096`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pabC (gene.b1096) is a gene entity. It encodes pabC (protein.P28305). Encoded protein function: FUNCTION: Involved in the biosynthesis of p-aminobenzoate (PABA), a precursor of tetrahydrofolate. Converts 4-amino-4-deoxychorismate into 4-aminobenzoate (PABA) and pyruvate. {ECO:0000269|PubMed:1644759, ECO:0000269|PubMed:2251281}. EcoCyc product frame: ADCLY-MONOMER. Genomic coordinates: 1153300-1154109.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28305|protein.P28305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=pabC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003709,ECOCYC:EG11493,GeneID:946647`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1153300-1154109:+; feature_type=gene
