---
entity_id: "gene.b4068"
entity_type: "gene"
name: "yjcH"
source_database: "NCBI RefSeq"
source_id: "gene-b4068"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4068"
  - "yjcH"
---

# yjcH

`gene.b4068`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4068`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjcH (gene.b4068) is a gene entity. It encodes yjcH (protein.P0AF54). Encoded protein function: Inner membrane protein YjcH EcoCyc product frame: YJCH-MONOMER. Genomic coordinates: 4284899-4285213. EcoCyc protein note: yjcH is cotranscribed with the acs and actP genes, which encode proteins involved in acetate dissimilation and transport . High-throughput identification of mutant phenotypes under multiple experimental conditions showed a similar fitness pattern of yjcH and actP mutants ; the authors suggests that YjcH may be required for activity of the ActP transporter .

## Biological Role

Repressed by fis (protein.P0A6R3), rob (protein.P0ACI0). Activated by crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF54|protein.P0AF54]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=yjcH; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yjcH; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=yjcH; function=-
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013330,ECOCYC:EG11943,GeneID:948574`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4284899-4285213:-; feature_type=gene
