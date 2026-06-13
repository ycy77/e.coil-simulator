---
entity_id: "gene.b3791"
entity_type: "gene"
name: "wecE"
source_database: "NCBI RefSeq"
source_id: "gene-b3791"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3791"
  - "wecE"
---

# wecE

`gene.b3791`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3791`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecE (gene.b3791) is a gene entity. It encodes wecE (protein.P27833). Encoded protein function: FUNCTION: Catalyzes the synthesis of dTDP-4-amino-4,6-dideoxy-D-galactose (dTDP-Fuc4N) from dTDP-4-keto-6-deoxy-D-glucose (dTDP-D-Glc4O) and L-glutamate. {ECO:0000255|HAMAP-Rule:MF_02026, ECO:0000269|PubMed:15271350}. EcoCyc product frame: RFFTRANS-MONOMER. EcoCyc synonyms: rff, fcnA, rffA, yifI. Genomic coordinates: 3975146-3976276. EcoCyc protein note: dTDP-4-dehydro-6-deoxy-D-glucose transaminase is involved in the biosynthesis of enterobacterial common antigen (ECA). This enzyme catalyzes the conversion of dTDP-4-keto-6-deoxy-D-glucose to dTDP-D-thomosamine . Crystal structures of the enzyme have been solved . While gel filtration showed a molecular weight of 180 kDa, suggesting a homotetrameric structure , the crystal structure showed a homodimeric configuration . The conserved active site Lys181 residue forms the internal aldimine with the PLP cofactor. The stereochemical specificity of the enzyme for amination of the C4 stereocenter, forming the C4-R configuration, is determined by a mode of nucleotide binding (a "base flip" mechanism) that differs from that of other C4 sugar aminotransferases and results in reorientation of the sugar moiety...

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27833|protein.P27833]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012384,ECOCYC:EG11456,GeneID:948296`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3975146-3976276:+; feature_type=gene
