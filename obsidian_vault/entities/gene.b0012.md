---
entity_id: "gene.b0012"
entity_type: "gene"
name: "mbiA"
source_database: "NCBI RefSeq"
source_id: "gene-b0012"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0012"
  - "mbiA"
---

# mbiA

`gene.b0012`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0012`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mbiA (gene.b0012) is a gene entity. It encodes mbiA (protein.P28697). Encoded protein function: Uncharacterized protein MbiA (Modifier of biofilm) EcoCyc product frame: EG11509-MONOMER. EcoCyc synonyms: htpY, htgA. Genomic coordinates: 10830-11315. EcoCyc protein note: HtgA was thought to play a role in the regulation of the heat shock response. Expression of htgA appeared to be under the control of the heat shock sigma factor σ32 ; however, later experiments did not support this result . Note that all mutagenesis experiments reported in disrupted both htgA and the yaaW ORF on the opposite strand. Experiments using the E. coli O157:H7 EDL933 yaaW and htgA genes, which are more than 98% identical to those of E. coli K-12, are reported in . Point mutants that selectively knock out either yaaW or htgA were constructed and tested. Neither mutant has a heat shock phenotype, and both mutants show somewhat increased biofilm formation in minimal medium at 48 hours . have suggested that the antisense htgA ORF has originated within the yaaW ORF through overprinting and have proposed the term "janolog" to describe such events. MbiA: "modifier of biofilm"

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28697|protein.P28697]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=mbiA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000040,ECOCYC:EG11509,GeneID:948295`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:10830-11315:+; feature_type=gene
