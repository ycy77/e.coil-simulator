---
entity_id: "gene.b3786"
entity_type: "gene"
name: "wecB"
source_database: "NCBI RefSeq"
source_id: "gene-b3786"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3786"
  - "wecB"
---

# wecB

`gene.b3786`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3786`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecB (gene.b3786) is a gene entity. It encodes wecB (protein.P27828). Encoded protein function: FUNCTION: Catalyzes the reversible epimerization at C-2 of UDP-N-acetylglucosamine (UDP-GlcNAc) and thereby provides bacteria with UDP-N-acetylmannosamine (UDP-ManNAc), the activated donor of ManNAc residues. Also involved in bacteriophage N4 adsorption. {ECO:0000269|PubMed:15210128, ECO:0000269|PubMed:7559340, ECO:0000269|PubMed:8170390, ECO:0000269|PubMed:8226648, ECO:0000269|Ref.9}. EcoCyc product frame: UDPGLCNACEPIM-MONOMER. EcoCyc synonyms: yifF, nfrC, rffE, mnaA. Genomic coordinates: 3970133-3971263. EcoCyc protein note: UDP-N-acetylmannosaminuronate (UDP-ManNAcUA) is one of the building blocks for the cell surface polysaccharide enterobacterial common antigen (ECA). UDP-N-acetylglucosamine 2-epimerase catalyzes the first step in UDP-ManNAcUA biosynthesis, the reversible epimerization at the C-2 position between UDP-N-acetylglucosamine (UDP-GlcNAc) and UDP-N-acetylmannosamine (UDP-ManNAc) . Enzymatic activity requires the presence of UDP-GlcNAc as an activator . UDP-ManNAc synthesized by WecB is proposed to be the precursor for biosynthesis of a novel surface glycan that is required for bacteriophage N4 infection . Experiments with the BASEL collection of bacteriophages that infect E. coli showed that certain families of phages depend on the presence of WecB for infectivity...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27828|protein.P27828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012372,ECOCYC:EG11451,GeneID:944789`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3970133-3971263:+; feature_type=gene
