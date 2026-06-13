---
entity_id: "gene.b0434"
entity_type: "gene"
name: "yajG"
source_database: "NCBI RefSeq"
source_id: "gene-b0434"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0434"
  - "yajG"
---

# yajG

`gene.b0434`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0434`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yajG (gene.b0434) is a gene entity. It encodes yajG (protein.P0ADA5). Encoded protein function: Uncharacterized lipoprotein YajG EcoCyc product frame: EG12182-MONOMER. Genomic coordinates: 453589-454167. EcoCyc protein note: Under anaerobiosis, FNR represses yajG gene expression, but it is not known if this regulation is direct or indirect . The Keio collection yajG mutant is sensitive to lithium (<90% growth at 100mM Li) .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADA5|protein.P0ADA5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yajG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001504,ECOCYC:EG12182,GeneID:945521`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:453589-454167:-; feature_type=gene
