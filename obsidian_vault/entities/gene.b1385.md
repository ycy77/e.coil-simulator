---
entity_id: "gene.b1385"
entity_type: "gene"
name: "feaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1385"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1385"
  - "feaB"
---

# feaB

`gene.b1385`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1385`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

feaB (gene.b1385) is a gene entity. It encodes feaB (protein.P80668). Encoded protein function: FUNCTION: Acts almost equally well on phenylacetaldehyde, 4-hydroxyphenylacetaldehyde and 3,4-dihydroxyphenylacetaldehyde. EcoCyc product frame: PHENDEHYD-MONOMER. EcoCyc synonyms: ydbG, padA. Genomic coordinates: 1447519-1449018.

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), feaR (protein.Q47129).

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P80668|protein.P80668]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=feaB; function=+
- `activates` <-- [[protein.Q47129|protein.Q47129]] `RegulonDB` `C` - regulator=FeaR; target=feaB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=feaB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004637,ECOCYC:G7961,GeneID:945933`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1447519-1449018:+; feature_type=gene
