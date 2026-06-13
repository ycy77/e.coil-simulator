---
entity_id: "gene.b3610"
entity_type: "gene"
name: "grxC"
source_database: "NCBI RefSeq"
source_id: "gene-b3610"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3610"
  - "grxC"
---

# grxC

`gene.b3610`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3610`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

grxC (gene.b3610) is a gene entity. It encodes grxC (protein.P0AC62). Encoded protein function: FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase. EcoCyc product frame: OX-GLUTAREDOXIN-C. EcoCyc synonyms: yibM. Genomic coordinates: 3784191-3784442. EcoCyc protein note: General InformationGlutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides. Glutaredoxins are similar to thioredoxins; both are usually small (9-12 kDa), and both are capable of catalyzing thiol-disulfide exchange reactions. Representatives of at least one of these two protein families have been found in all organisms studied, indicating that proteins of this type are essential for cellular functions. A main difference between the two is the mechanism for their reduction. Glutaredoxins are generally reduced by the compound GLUTATHIONE (GSH), while thioredoxins are reduced by the specific flavoenzyme THIOREDOXIN-REDUCT-NADPH-CPLX. While thioredoxins are found to be general reductants of protein disulfides, glutaredoxins are better at reducing mixed disulfides between proteins (or low molecular weight thiol-containing compounds) and GSH...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC62|protein.P0AC62]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=grxC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011801,ECOCYC:EG12294,GeneID:948132`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3784191-3784442:-; feature_type=gene
