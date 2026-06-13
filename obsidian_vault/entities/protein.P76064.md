---
entity_id: "protein.P76064"
entity_type: "protein"
name: "ydaT"
source_database: "UniProt"
source_id: "P76064"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydaT b1358 JW1353"
---

# ydaT

`protein.P76064`

## Static

- Type: `protein`
- Source: `UniProt:P76064`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that causes a severe detrimental growth effect and reduces cell viability (PubMed:38153127). When expressed, it alters expression of a variety of bacterial regulons normally controlled by the transcriptional regulatory protein RcsA, resulting in deficient lipopolysaccharide biosynthesis and cell division (PubMed:38153127). YdaT has no effect on Rac prophage excision (PubMed:38153127). Overexpression of ydaST reduces growth and leads to loss of cell viability (PubMed:29205228). May contribute to toxicity and morphological defects (PubMed:29205229). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}. This Rac prophage G6682 gene was first identified in TAX-562 K-12 as a putative homolog of the λ phage cII lysogenic regulatory gene and is next to G6681, possibly as part of the same operon . YdaT appears to regulate lipopolysaccharide biosynthesis and cell division genes . The ydaST locus was computationally predicted to encode a toxin/antitoxin (TA) pair . However, no evidence for this function was found in a study aimed at validating and characterizing new TA loci in E. coli K-12 . A ΔydaT mutant has aggravating genetic interactions with genes involved in DNA recombination...

## Annotation

FUNCTION: Transcriptional regulator that causes a severe detrimental growth effect and reduces cell viability (PubMed:38153127). When expressed, it alters expression of a variety of bacterial regulons normally controlled by the transcriptional regulatory protein RcsA, resulting in deficient lipopolysaccharide biosynthesis and cell division (PubMed:38153127). YdaT has no effect on Rac prophage excision (PubMed:38153127). Overexpression of ydaST reduces growth and leads to loss of cell viability (PubMed:29205228). May contribute to toxicity and morphological defects (PubMed:29205229). {ECO:0000269|PubMed:29205228, ECO:0000269|PubMed:29205229, ECO:0000269|PubMed:38153127}.

## Outgoing Edges (1)

- `activates` --> [[gene.b1951|gene.b1951]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b1358|gene.b1358]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76064`
- `KEGG:ecj:JW1353;eco:b1358;ecoc:C3026_07945;`
- `GeneID:86946546;945924;`
- `GO:GO:0043093`

## Notes

Transcriptional regulator YdaT
