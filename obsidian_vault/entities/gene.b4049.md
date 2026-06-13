---
entity_id: "gene.b4049"
entity_type: "gene"
name: "dusA"
source_database: "NCBI RefSeq"
source_id: "gene-b4049"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4049"
  - "dusA"
---

# dusA

`gene.b4049`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4049`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dusA (gene.b4049) is a gene entity. It encodes dusA (protein.P32695). Encoded protein function: FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D), a modified base found in the D-loop of most tRNAs, via the reduction of the C5-C6 double bond in target uridines. Specifically modifies U20 and U20a in tRNAs. {ECO:0000255|HAMAP-Rule:MF_02041, ECO:0000269|PubMed:11983710, ECO:0000269|PubMed:22123979, ECO:0000305|PubMed:25902496}. EcoCyc product frame: EG11932-MONOMER. EcoCyc synonyms: yjbN. Genomic coordinates: 4261669-4262706. EcoCyc protein note: DusA accounts for about half of the 5,6-dihydrouridine modification observed in wild-type cellular tRNA; EG11311-MONOMER (DusB) and EG12022-MONOMER (DusC) together account for the other half. DusA is solely responsible for the 5,6-dihydrouridine modification observed in tRNA2fMet . A dusA dusB dusC triple mutant (Δ3) exhibits a complete lack of 5,6-dihydrouridine modification in cellular tRNA, whereas each single mutant exhibits a partial reduction, compared to wild type . Amino acids that are required for DusA activity have been identified . Using a ΔdusA mutant, the specificity of DusA for dihydrouridylation of nucleotide 20 and 20a was determined in ARG-tRNAs (ICG), ILE-tRNAs (GAU) and LEU-tRNAs (CAG)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32695|protein.P32695]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013258,ECOCYC:EG11932,GeneID:948558`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4261669-4262706:+; feature_type=gene
