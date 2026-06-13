---
entity_id: "gene.b0195"
entity_type: "gene"
name: "trmO"
source_database: "NCBI RefSeq"
source_id: "gene-b0195"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0195"
  - "trmO"
---

# trmO

`gene.b0195`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0195`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmO (gene.b0195) is a gene entity. It encodes trmO (protein.P28634). Encoded protein function: FUNCTION: S-adenosyl-L-methionine-dependent methyltransferase responsible for the addition of the methyl group in the formation of N6-methyl-N6-threonylcarbamoyladenosine at position 37 (m(6)t(6)A37) of the tRNA anticodon loop of tRNA(Thr)(GGU) that read codons starting with adenosine (PubMed:25063302, PubMed:9537379). The methyl group of m(6)t(6)A37 appears to slightly improve the efficiency of the tRNA decoding ability (PubMed:25063302, PubMed:9537379). {ECO:0000269|PubMed:25063302, ECO:0000269|PubMed:9537379}. EcoCyc product frame: EG11503-MONOMER. EcoCyc synonyms: tsaA, yaeB. Genomic coordinates: 218887-219594. EcoCyc protein note: tRNA m6t6A37 methyltransferase (TrmO) catalyzes methylation of N6 of the A37 nucleotide adjacent to the anticodon of tRNAs thrT-tRNA and thrV-tRNA. The presence of the N6-threonylcarbamoyl modification at A37 is required for activity of the enzyme . TrmO is able to discriminate between the four Thr-specific tRNAs in E. coli, only modifying the ACY-specific tRNAs containing the GGU anticodon. The major specificity determinants within these tRNAs are C31-G39 and G34 . TrmO is the founding member of a novel class of SAM-dependent methyltransferases...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28634|protein.P28634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000661,ECOCYC:EG11503,GeneID:949112`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:218887-219594:-; feature_type=gene
