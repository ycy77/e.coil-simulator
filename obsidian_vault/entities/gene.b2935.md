---
entity_id: "gene.b2935"
entity_type: "gene"
name: "tktA"
source_database: "NCBI RefSeq"
source_id: "gene-b2935"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2935"
  - "tktA"
---

# tktA

`gene.b2935`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2935`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tktA (gene.b2935) is a gene entity. It encodes tktA (protein.P27302). Encoded protein function: FUNCTION: Catalyzes the transfer of a two-carbon ketol group from a ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor thiamine pyrophosphate. Thus, catalyzes the reversible transfer of a two-carbon ketol group from sedoheptulose-7-phosphate to glyceraldehyde-3-phosphate, producing xylulose-5-phosphate and ribose-5-phosphate. {ECO:0000269|PubMed:17914867, ECO:0000269|PubMed:7607225}. EcoCyc product frame: TRANSKETOI-MONOMER. EcoCyc synonyms: tkt. Genomic coordinates: 3079644-3081635. EcoCyc protein note: Transketolase catalyzes the reversible transfer of a ketol group between several donor and acceptor substrates. This key enzyme is a reversible link between glycolysis and the pentose phosphate pathway. The enzyme is involved in the catabolism of pentose sugars, the formation of D-ribose 5-phosphate, and the provision of D-erythrose 4-phosphate, a precursor of aromatic amino acids and PLP . E. coli contains two transketolase isozymes, TktA and TktB. TktA is responsible for the major transketolase activity . In addition to its function in central carbon metabolism, transketolase appears to also have an unexpected role in chromosome structure; a tktA mutant affects chromosome topology...

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27302|protein.P27302]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009625,ECOCYC:EG11427,GeneID:947420`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3079644-3081635:-; feature_type=gene
