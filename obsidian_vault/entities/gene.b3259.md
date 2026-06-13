---
entity_id: "gene.b3259"
entity_type: "gene"
name: "prmA"
source_database: "NCBI RefSeq"
source_id: "gene-b3259"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3259"
  - "prmA"
---

# prmA

`gene.b3259`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3259`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prmA (gene.b3259) is a gene entity. It encodes prmA (protein.P0A8T1). Encoded protein function: FUNCTION: Methylates ribosomal protein L11. {ECO:0000255|HAMAP-Rule:MF_00735, ECO:0000269|PubMed:372746, ECO:0000269|PubMed:7715456}. EcoCyc product frame: EG11497-MONOMER. EcoCyc synonyms: yhdI, prm-1. Genomic coordinates: 3409070-3409951. EcoCyc protein note: PrmA is the methyltransferase responsible for the multiple methylation of EG10872-MONOMER. Free L11 is a better substrate than assembled 50S ribosomal subunits . prmA mutants are deficient in the methylation of ribosomal protein L11 . A strain containing a prmA null mutation is viable and shows no growth defect, indicating that lack of methylation of L11 does not affect its function in the ribosome . PrmA: "protein methylation A"

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8T1|protein.P0A8T1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=prmA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010697,ECOCYC:EG11497,GeneID:947708`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3409070-3409951:+; feature_type=gene
