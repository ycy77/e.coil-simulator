---
entity_id: "gene.b1927"
entity_type: "gene"
name: "amyA"
source_database: "NCBI RefSeq"
source_id: "gene-b1927"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1927"
  - "amyA"
---

# amyA

`gene.b1927`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1927`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amyA (gene.b1927) is a gene entity. It encodes amyA (protein.P26612). Encoded protein function: Cytoplasmic alpha-amylase (EC 3.2.1.1) (1,4-alpha-D-glucan glucanohydrolase) EcoCyc product frame: ALPHA-AMYL-CYTO-MONOMER. EcoCyc synonyms: yedC. Genomic coordinates: 2006156-2007643. EcoCyc protein note: AmyA is a cytoplasmic α-amylase. Alpha-Amyloses α-Amylose, a linear α-glucan, is the most effective substrate in vitro; Starch starch and CPD-7043 amylopectin, a lightly branched α-glucan, can serve as good substrates, while the highly branched α-glucan Glycogens glycogen is a poor substrate. Linear oligomeric α-glucans of six or more glucose moieties are good substrates of AmyA . The physiological role of AmyA is uncertain. Although under experimental conditions glycogen is a poor substrate for the enzyme, it is the most likely natural substrate since it is the only polysaccharide present in appreciable amounts in the cytoplasm. It has been hypothesized that in the absence of exogenous oligosaccharides that could act as primers for glycogen synthesis, the cytoplasmic amylase might provide oligosaccharides through catabolism of existing cellular glycogen, which would then act as the source of primers for the synthesis of more molecules of glycogen . AmyA is one of two α-amylases present in E. coli. The second enzyme, ALPHA-AMYL-PERI-MONOMER "MalS", is periplasmic.

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26612|protein.P26612]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006414,ECOCYC:EG11387,GeneID:946434`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2006156-2007643:+; feature_type=gene
