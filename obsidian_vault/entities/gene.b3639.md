---
entity_id: "gene.b3639"
entity_type: "gene"
name: "dfp"
source_database: "NCBI RefSeq"
source_id: "gene-b3639"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3639"
  - "dfp"
---

# dfp

`gene.b3639`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3639`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dfp (gene.b3639) is a gene entity. It encodes coaBC (protein.P0ABQ0). Encoded protein function: FUNCTION: Catalyzes two sequential steps in the biosynthesis of coenzyme A. In the first step cysteine is conjugated to 4'-phosphopantothenate to form 4-phosphopantothenoylcysteine (PubMed:11278255, PubMed:12140293, PubMed:14686929). In the second step the latter compound is decarboxylated to form 4'-phosphopantotheine (PubMed:10922366, PubMed:11358972). {ECO:0000269|PubMed:10922366, ECO:0000269|PubMed:11278255, ECO:0000269|PubMed:11358972, ECO:0000269|PubMed:12140293, ECO:0000269|PubMed:14686929}. EcoCyc product frame: EG10004-MONOMER. EcoCyc synonyms: coaBC. Genomic coordinates: 3812731-3813951. EcoCyc protein note: The dfp (coaBC) gene encodes an enzyme with two domains, each catalyzing one of two sequential reactions in the coenzyme A biosynthetic pathway . The C-terminal ("CoaB") domain of the protein confers phosphopantothenoylcysteine synthetase activity . When expressed separately, the CoaB domain forms dimers in solution. Point mutants in conserved residues have been generated and analyzed, and the existence of a 4'-phosphopantothenoyl-CMP intermediate of the two half reactions has been confirmed . Crystal structures of this domain have been solved, and a reaction mechanism has been proposed . Small molecule inhibitors have been designed and tested...

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABQ0|protein.P0ABQ0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011896,ECOCYC:EG10004,GeneID:949047`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3812731-3813951:+; feature_type=gene
