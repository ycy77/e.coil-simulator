---
entity_id: "gene.b4596"
entity_type: "gene"
name: "yciZ"
source_database: "NCBI RefSeq"
source_id: "gene-b4596"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4596"
  - "yciZ"
---

# yciZ

`gene.b4596`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4596`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciZ (gene.b4596) is a gene entity. It encodes yciZ (protein.A5A614). Encoded protein function: UPF0509 protein YciZ EcoCyc product frame: MONOMER0-2820. EcoCyc synonyms: deoL. Genomic coordinates: 1344436-1344609. EcoCyc protein note: YciZ is a small open reading frame upstream of the predicted transcriptional regulator YciT. The authors of named it a "leader", but no evidence for a regulatory function of YciZ exists. YciZ is expressed at approximately equal levels during exponential growth and stationary phase in rich growth medium . DeoL: "DeoT leader"

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A614|protein.A5A614]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=yciZ; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yciZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0285180,ECOCYC:G0-10591,GeneID:5061509`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1344436-1344609:-; feature_type=gene
