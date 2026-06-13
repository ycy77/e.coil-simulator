---
entity_id: "gene.b0849"
entity_type: "gene"
name: "grxA"
source_database: "NCBI RefSeq"
source_id: "gene-b0849"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0849"
  - "grxA"
---

# grxA

`gene.b0849`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0849`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

grxA (gene.b0849) is a gene entity. It encodes grxA (protein.P68688). Encoded protein function: FUNCTION: The disulfide bond functions as an electron carrier in the glutathione-dependent synthesis of deoxyribonucleotides by the enzyme ribonucleotide reductase. In addition, it is also involved in reducing some disulfide bonds in a coupled system with glutathione reductase. EcoCyc product frame: GLUTAREDOXIN-MONOMER. EcoCyc synonyms: grx. Genomic coordinates: 890496-890753. EcoCyc protein note: The oxidized form of Grx1 appears to be in a weak monomer-dimer equilibrium . For an extensive summary on Grx1, please see RED-GLUTAREDOXIN. Reviews: EcoCyc protein note: General InformationGlutaredoxins are ubiquitous proteins that catalyze the reduction of disulfides. Glutaredoxins are similar to thioredoxins; both are usually small (9-12 kDa), and both are capable of catalyzing thiol-disulfide exchange reactions. Representatives of at least one of these two protein families have been found in all organisms studied, indicating that proteins of this type are essential for cellular functions. A main difference between the two is the mechanism for their reduction. Glutaredoxins are generally reduced by the compound GLUTATHIONE (GSH), while thioredoxins are reduced by the specific flavoenzyme THIOREDOXIN-REDUCT-NADPH-CPLX...

## Biological Role

Activated by oxyR (protein.P0ACQ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68688|protein.P68688]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=grxA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002893,ECOCYC:EG10417,GeneID:945479`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:890496-890753:-; feature_type=gene
