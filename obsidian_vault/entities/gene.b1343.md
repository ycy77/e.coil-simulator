---
entity_id: "gene.b1343"
entity_type: "gene"
name: "dbpA"
source_database: "NCBI RefSeq"
source_id: "gene-b1343"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1343"
  - "dbpA"
---

# dbpA

`gene.b1343`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1343`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dbpA (gene.b1343) is a gene entity. It encodes dbpA (protein.P21693). Encoded protein function: FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit. Has an RNA-dependent ATPase activity, which is specific for 23S rRNA, and a 3' to 5' RNA helicase activity that uses the energy of ATP hydrolysis to destabilize and unwind short rRNA duplexes. Requires a single-stranded RNA loading site on the 3' side of the substrate helix. {ECO:0000255|HAMAP-Rule:MF_00965, ECO:0000269|PubMed:11350034, ECO:0000269|PubMed:11574482, ECO:0000269|PubMed:15910005, ECO:0000269|PubMed:18237742, ECO:0000269|PubMed:19734347, ECO:0000269|PubMed:20160110, ECO:0000269|PubMed:8253085, ECO:0000269|PubMed:9016593, ECO:0000269|PubMed:9836593}. EcoCyc product frame: EG10210-MONOMER. EcoCyc synonyms: rhlC. Genomic coordinates: 1409511-1410884. EcoCyc protein note: DbpA is a 3'->5' RNA helicase that plays a role in the late stage of biogenesis of the 50S subunit of the ribosome . DbpA interacts with 23S rRNA and exhibits RNA-dependent ATPase activity that shows specificity for 23S rRNA molecules that are not incorporated within the ribosome . Footprinting of DbpA protein on a fragment of 23S rRNA indicates binding at multiple sites , but the primary binding site appears to be hairpin 92 of the 23S rRNA, which is part of the peptidyltransferase center of the ribosome...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21693|protein.P21693]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004511,ECOCYC:EG10210,GeneID:947153`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1409511-1410884:+; feature_type=gene
