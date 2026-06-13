---
entity_id: "gene.b3734"
entity_type: "gene"
name: "atpA"
source_database: "NCBI RefSeq"
source_id: "gene-b3734"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3734"
  - "atpA"
---

# atpA

`gene.b3734`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3734`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpA (gene.b3734) is a gene entity. It encodes atpA (protein.P0ABB0). Encoded protein function: FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The alpha chain is a regulatory subunit. EcoCyc product frame: ATPA-MONOMER. EcoCyc synonyms: papA, uncA. Genomic coordinates: 3918316-3919857.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABB0|protein.P0ABB0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpA; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012213,ECOCYC:EG10098,GeneID:948242`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3918316-3919857:-; feature_type=gene
