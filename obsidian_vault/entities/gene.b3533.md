---
entity_id: "gene.b3533"
entity_type: "gene"
name: "bcsA"
source_database: "NCBI RefSeq"
source_id: "gene-b3533"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3533"
  - "bcsA"
---

# bcsA

`gene.b3533`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3533`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bcsA (gene.b3533) is a gene entity. It encodes bcsA (protein.P37653). Encoded protein function: FUNCTION: Catalytic subunit of cellulose synthase. It polymerizes uridine 5'-diphosphate glucose to cellulose, which is produced as an extracellular component for mechanical and chemical protection at the onset of the stationary phase, when the cells exhibit multicellular behavior (rdar morphotype). Coexpression of cellulose and thin aggregative fimbriae (curli fimbrae or fibers) leads to a hydrophobic network with tightly packed cells embedded in a highly inert matrix that confers cohesion, elasticity and tissue-like properties to colonies (PubMed:24097954). {ECO:0000269|PubMed:11260463, ECO:0000269|PubMed:24097954}. EcoCyc product frame: EG12260-MONOMER. EcoCyc synonyms: yhjP, yhjO. Genomic coordinates: 3692618-3695236. EcoCyc protein note: bcsA has sequence similarity to the gene encoding the catalytic subunit of cellulose synthase from the model cellulose producing organism Acetobacter xylinus ; the protein contains a conserved C-terminal PilZ c-di-GMP binding domain . In E. coli K-12 strains such as W3110 and MG1655, a "domesticating SNP" consists of a point mutation that introduces a stop codon after the first 5 amino acids of the wild-type bcsQ ORF. This domesticating SNP lowers expression of both bcsQ and the downstream bcsA gene...

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37653|protein.P37653]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011547,ECOCYC:EG12260,GeneID:948053`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3692618-3695236:-; feature_type=gene
