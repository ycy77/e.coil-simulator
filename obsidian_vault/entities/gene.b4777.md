---
entity_id: "gene.b4777"
entity_type: "gene"
name: "mdtU"
source_database: "NCBI RefSeq"
source_id: "gene-b4777"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4777"
  - "mdtU"
---

# mdtU

`gene.b4777`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4777`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mdtU (gene.b4777) is a gene entity. It encodes ydgV (protein.P0DSF5). Encoded protein function: Protein YdgV EcoCyc product frame: MONOMER0-4489. EcoCyc synonyms: ydgV. Genomic coordinates: 1673608-1673709. EcoCyc protein note: MdtU was identified as a previously unannotated small protein; it is expressed in both exponential and stationary phase in rich media . Transcription of mdtUJI is induced by spermidine at pH 9; translation of MdtU is required for spermidine-mediated expression of MdtJ. Rho-dependent transcription termination between the MdtU and MdtJ coding regions was discovered by RNA 3' end mapping . MdtU: "Mdt upstream ORF"

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0DSF5|protein.P0DSF5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mdtU; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=mdtU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0285779,ECOCYC:G0-17023,GeneID:63925638`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1673608-1673709:-; feature_type=gene
