---
entity_id: "gene.b0147"
entity_type: "gene"
name: "thpR"
source_database: "NCBI RefSeq"
source_id: "gene-b0147"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0147"
  - "thpR"
---

# thpR

`gene.b0147`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0147`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thpR (gene.b0147) is a gene entity. It encodes thpR (protein.P37025). Encoded protein function: FUNCTION: Hydrolyzes RNA 2',3'-cyclic phosphodiester to an RNA 2'-phosphomonoester (PubMed:25239919). In vitro, can also ligate 5' and 3' half-tRNA molecules with 2',3'-cyclic phosphate and 5'-hydroxyl termini, respectively, to the product containing the 2'-5' phosphodiester linkage. This reaction does not require ATP and is reversible (PubMed:6347395, PubMed:8940112). {ECO:0000269|PubMed:25239919, ECO:0000269|PubMed:6347395, ECO:0000269|PubMed:8940112}. EcoCyc product frame: EG12330-MONOMER. EcoCyc synonyms: yadP, ligT. Genomic coordinates: 161501-162031. EcoCyc protein note: ThpR belongs to the family of two-histidine (2H) phosphoesterase enzymes and has been shown to be an "end healing" cyclic phosphodiesterase (CPDase) that hydrolyzes RNA 2',3'-cyclic phosphodiesters . Biophysical characterization of ThpR and comparison to two other cyclic nucleotide phosphodiesterases from yeast and Arabidopsis has been reported. ThpR appears to exist as a monomer in solution . A crystal structure of ThpR in complex with 2'-AMP has been solved at 2 Å resolution, implicating His43 as a general acid catalyst and His125 as a general base catalyst. Arg130 may have a role in stabilizing the transition state...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37025|protein.P37025]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000505,ECOCYC:EG12330,GeneID:944848`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:161501-162031:-; feature_type=gene
