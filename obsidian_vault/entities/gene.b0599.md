---
entity_id: "gene.b0599"
entity_type: "gene"
name: "hcxA"
source_database: "NCBI RefSeq"
source_id: "gene-b0599"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0599"
  - "hcxA"
---

# hcxA

`gene.b0599`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0599`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hcxA (gene.b0599) is a gene entity. It encodes hcxA (protein.P45579). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of 2-oxoglutarate and 2-oxobutanoate, leading to the respective 2-hydroxycarboxylate. Cannot use NADH instead of NADPH as a redox partner. Do not catalyze the reverse reactions. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG12692-MONOMER. EcoCyc synonyms: ybdH. Genomic coordinates: 632389-633477. EcoCyc protein note: The NADP-dependent hydroxycarboxylate dehydrogenase activity of HcxA was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . An hcxA null mutant showed strongly repressed swarming motility . HcxA: "hydroxycarboxylic acid dehydrogenase A"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45579|protein.P45579]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002065,ECOCYC:EG12692,GeneID:945212`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:632389-633477:-; feature_type=gene
