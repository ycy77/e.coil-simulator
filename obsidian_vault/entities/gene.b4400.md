---
entity_id: "gene.b4400"
entity_type: "gene"
name: "creD"
source_database: "NCBI RefSeq"
source_id: "gene-b4400"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4400"
  - "creD"
---

# creD

`gene.b4400`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4400`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

creD (gene.b4400) is a gene entity. It encodes creD (protein.P08369). Encoded protein function: Inner membrane protein CreD EcoCyc product frame: EG10145-MONOMER. EcoCyc synonyms: refII, cet. Genomic coordinates: 4638178-4639530. EcoCyc protein note: Overexpression of CreD was previously thought to be responsible for tolerance to colicin E2 , but it has since been shown that this phenotype is due to overexpression of the CbrC protein . Over-production of CreD is implicated in a CreBC mediated β-lactam tolerance phenotype . CreD is predicted to be an inner membrane protein with five transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . Transcription of creD is induced by the CreBC two-component system during growth in glucose minimal media (see further ).

## Biological Role

Activated by creB (protein.P08368).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08369|protein.P08369]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P08368|protein.P08368]] `RegulonDB` `S` - regulator=CreB; target=creD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014432,ECOCYC:EG10145,GeneID:948868`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4638178-4639530:+; feature_type=gene
