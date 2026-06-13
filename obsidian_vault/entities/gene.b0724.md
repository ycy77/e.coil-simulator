---
entity_id: "gene.b0724"
entity_type: "gene"
name: "sdhB"
source_database: "NCBI RefSeq"
source_id: "gene-b0724"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0724"
  - "sdhB"
---

# sdhB

`gene.b0724`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0724`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdhB (gene.b0724) is a gene entity. It encodes sdhB (protein.P07014). Encoded protein function: FUNCTION: Two distinct, membrane-bound, FAD-containing enzymes are responsible for the catalysis of fumarate and succinate interconversion; the fumarate reductase is used in anaerobic growth, and the succinate dehydrogenase is used in aerobic growth. EcoCyc product frame: SDH-FE-S. EcoCyc synonyms: dhsB. Genomic coordinates: 757689-758405. EcoCyc protein note: This is one of two catalytic subunits of the four-subunit succinate dehydrogenase (SQR) enzyme. This subunit contains three iron-sulfur clusters: a 2Fe-2S, a 4Fe-4S and a 3Fe-4S. This subunit has 38% identity to the fumarate reductase iron-sulfur cluster subunit, FrdB . The iron-sulfur clusters of this subunit act as electron transfer redox centers, delivering electrons from the FAD cofactor in SdhA to the ubiquinone binding site within the membrane domain . sdhB belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . ArcA appears to repress sdhB gene expression under anaerobiosis. Two putative ArcA binding sites were identified 69, 267 and 330 bp upstream of this gene , but no promoter upstream of it has been identified. Instead, sdhB is transcribed from two promoters: one of them is located usptream of sdhD gene and the other one upstream of sdhC gene...

## Biological Role

Repressed by ryhB (gene.b4451), arcA (protein.P0A9Q1). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), arcA (protein.P0A9Q1).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07014|protein.P07014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhB; function=-+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=sdhB; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002468,ECOCYC:EG10932,GeneID:945300`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:757689-758405:+; feature_type=gene
