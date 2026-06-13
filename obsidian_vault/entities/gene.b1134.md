---
entity_id: "gene.b1134"
entity_type: "gene"
name: "nudJ"
source_database: "NCBI RefSeq"
source_id: "gene-b1134"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1134"
  - "nudJ"
---

# nudJ

`gene.b1134`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1134`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nudJ (gene.b1134) is a gene entity. It encodes nudJ (protein.P0AEI6). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of 4-amino-2-methyl-5-hydroxymethylpyrimidine pyrophosphate (HMP-PP) to 4-amino-2-methyl-5-hydroxymethylpyrimidine phosphate (HMP-P), and hydrolysis of thiamine pyrophosphate (TPP) to thiamine monophosphate (TMP). Can hydrolyze other substrates such as MeO-HMP-PP, CF(3)-HMP-PP and MeO-TPP. Is also a non-specific nucleoside tri- and diphosphatase that releases inorganic orthophosphate. {ECO:0000269|PubMed:15292217, ECO:0000269|PubMed:16766526}. EcoCyc product frame: G6580-MONOMER. EcoCyc synonyms: ymfB. Genomic coordinates: 1193827-1194288. EcoCyc protein note: The nudJ gene product is a member of the Nudix hydrolase superfamily. Unlike the other Nudix nucleoside triphosphatases in E. coli, the product of the reaction is phosphate instead of pyrophosphate. NudJ is a promiscuous enzyme with no preference for deoxyribose or ribose, and nucleoside di- and tri-phosphates serve as substrates equally. The enzyme is a monomer in solution . NudJ also contributes to the production of dimethylallyl phosphate, which is the substrate for UBIX-MONOMER UbiX-catalyzed generation of the prFMN cofactor in ubiquinone biosynthesis . Crystal structures of NudJ have been solved...

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEI6|protein.P0AEI6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003818,ECOCYC:G6580,GeneID:945689`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1193827-1194288:-; feature_type=gene
