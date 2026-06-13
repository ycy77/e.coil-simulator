---
entity_id: "gene.b2615"
entity_type: "gene"
name: "nadK"
source_database: "NCBI RefSeq"
source_id: "gene-b2615"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2615"
  - "nadK"
---

# nadK

`gene.b2615`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2615`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nadK (gene.b2615) is a gene entity. It encodes nadK (protein.P0A7B3). Encoded protein function: FUNCTION: Involved in the regulation of the intracellular balance of NAD and NADP, and is a key enzyme in the biosynthesis of NADP. Catalyzes specifically the phosphorylation on 2'-hydroxyl of the adenosine moiety of NAD to yield NADP. It can use ATP and other nucleoside triphosphates (UTP, CTP, GTP, dATP, TTP) as phosphoryl donors, while nucleoside mono- or diphosphates and poly(P) cannot. {ECO:0000255|HAMAP-Rule:MF_00361, ECO:0000269|PubMed:11488932, ECO:0000269|PubMed:15855156, ECO:0000269|PubMed:3025169}. EcoCyc product frame: MONOMER0-541. EcoCyc synonyms: yfjE, yfjB. Genomic coordinates: 2750831-2751709. EcoCyc protein note: NAD kinase appears to be an allosteric enzyme, with activity tightly coupled to the NADPH/NADP+ and NADH/NAD+ ratios present in the cell. That suggests that NAD kinase may play an important role in the regulation of NADP turnover and size of the NADP pool . nadK is likely essential for growth . Site-directed mutagenesis studies of the E. coli enzyme showed that a R175G mutation relaxed the strict NAD substrate specificity of the enzyme, resulting in a low level of ATP-dependent NADH kinase activity . Structure-function relationships in NAD kinases from archaea, bacteria (including E. coli) and eukaryotes have been reviewed .

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7B3|protein.P0A7B3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008603,ECOCYC:EG12192,GeneID:947092`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2750831-2751709:+; feature_type=gene
