---
entity_id: "gene.b0464"
entity_type: "gene"
name: "acrR"
source_database: "NCBI RefSeq"
source_id: "gene-b0464"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0464"
  - "acrR"
---

# acrR

`gene.b0464`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0464`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrR (gene.b0464) is a gene entity. It encodes acrR (protein.P0ACS9). Encoded protein function: FUNCTION: Potential regulator protein for the acrAB genes. EcoCyc product frame: EG12116-MONOMER. EcoCyc synonyms: ybaH. Genomic coordinates: 485761-486408. EcoCyc protein note: The "acriflavine resistance regulator," AcrR, is classified in the nodulation-resistance division family and regulates the expression of genes involved in multidrug transport . It appears to be involved in resistance to ciprofloxacin , cefuroxime, gentamicin, and pyocyanin . This protein also regulates genes that contend with polyamine toxicity . In addition, AcrR acts as a global repressor for the mar-sox-rob regulon . Consistent with a broader in vivo principle observed for many transcription factors (including AcrR), TF action can primarily stabilize RNAP at promoters even when the net outcome is repression; accordingly, AcrR-dependent fold-changes scale approximately with the reciprocal of promoter constitutive (basal) activity and can buffer promoter-to-promoter variability, so AcrR-regulated promoters tend to converge toward more similar expression levels across diverse promoter contexts and perturbations...

## Biological Role

Repressed by acrR (protein.P0ACS9), yneJ (protein.P77309). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACS9|protein.P0ACS9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=acrR; function=+
- `represses` <-- [[protein.P0ACS9|protein.P0ACS9]] `RegulonDB` `C` - regulator=AcrR; target=acrR; function=-
- `represses` <-- [[protein.P77309|protein.P77309]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001608,ECOCYC:EG12116,GeneID:945516`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:485761-486408:+; feature_type=gene
