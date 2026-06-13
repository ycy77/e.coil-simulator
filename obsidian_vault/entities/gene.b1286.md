---
entity_id: "gene.b1286"
entity_type: "gene"
name: "rnb"
source_database: "NCBI RefSeq"
source_id: "gene-b1286"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1286"
  - "rnb"
---

# rnb

`gene.b1286`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1286`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rnb (gene.b1286) is a gene entity. It encodes rnb (protein.P30850). Encoded protein function: FUNCTION: Involved in mRNA degradation. Hydrolyzes single-stranded polyribonucleotides processively in the 3' to 5' direction (PubMed:11948193). RNases 2 and R (rnr) contribute to rRNA degradation during starvation, while RNase R and PNPase (pnp) are the major contributors to quality control of rRNA during steady state growth (PubMed:21135037). This RNase is required to decrease expression of RNase PH (rnp) at 42 degrees Celsius during starvation, which in turn represses rRNA degradation (PubMed:28625967). {ECO:0000269|PubMed:11948193, ECO:0000269|PubMed:21135037, ECO:0000269|PubMed:28625967}. EcoCyc product frame: EG11620-MONOMER. Genomic coordinates: 1346978-1348912. EcoCyc protein note: Ribonuclease II (RNase II) is a single-strand-specific exoribonuclease that cleaves RNA processively from the 3' end to produce ribonucleoside 5'-monophosphates. It has roles in the maturation, turnover and quality control of different RNA types. RNase II is one of six exonucleases (RNase II, RNase D, RNase BN, RNase T, RNase PH and PNPase) that can process tRNA and is responsible for the first step in the conversion of precursor tyrosine tRNA to its final form . It has been shown in vitro to cleave long 3' tRNA sequences to yield 2-4 nucleotide intermediates for subsequent processing...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30850|protein.P30850]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rnb; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004320,ECOCYC:EG11620,GeneID:945864`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1346978-1348912:-; feature_type=gene
