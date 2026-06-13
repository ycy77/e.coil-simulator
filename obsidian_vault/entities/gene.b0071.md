---
entity_id: "gene.b0071"
entity_type: "gene"
name: "leuD"
source_database: "NCBI RefSeq"
source_id: "gene-b0071"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0071"
  - "leuD"
---

# leuD

`gene.b0071`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0071`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

leuD (gene.b0071) is a gene entity. It encodes leuD (protein.P30126). Encoded protein function: FUNCTION: Catalyzes the isomerization between 2-isopropylmalate and 3-isopropylmalate, via the formation of 2-isopropylmaleate. EcoCyc product frame: LEUD-MONOMER. Genomic coordinates: 78848-79453. EcoCyc protein note: Isopropylmalate (IPM) isomerase catalyzes the second step in leucine biosynthesis, converting 2-isopropylmalate to 3-isopropylmalate. LeuC and LeuD are both required for the activity of IPM isomerase . Based on the IPM isomerase in Salmonella typhimurium and cross-species complementation studies with the Salmonella and S. cerevisiae enzymes, E. coli IPM isomerase is likely to be a protein complex consisting of a 1:1 pairing of the of leuC and leuD gene products .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30126|protein.P30126]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=leuD; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000259,ECOCYC:EG11575,GeneID:945642`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:78848-79453:-; feature_type=gene
