---
entity_id: "gene.b2607"
entity_type: "gene"
name: "trmD"
source_database: "NCBI RefSeq"
source_id: "gene-b2607"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2607"
  - "trmD"
---

# trmD

`gene.b2607`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2607`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmD (gene.b2607) is a gene entity. It encodes trmD (protein.P0A873). Encoded protein function: FUNCTION: Specifically methylates guanosine-37 in various tRNAs. {ECO:0000269|PubMed:14583191}. EcoCyc product frame: EG11023-MONOMER. Genomic coordinates: 2744572-2745339. EcoCyc protein note: tRNA m1G37 methyltransferase (TrmD) catalyzes the addition of a methyl group to G37 of certain tRNAs . Specificity of this activity is controlled by tRNA structure, specifically including the V, T and D side loops and the presence of G36pG37 . TrmD can accomodate both A and G at position 36 in tRNAAsp and tRNAPhe . Analysis of enzyme activity with truncated tRNAs showed that TrmD minimally requires the anticodon loop and a 9 bp stem in vitro, distinguishing the prokaryotic enzymes from the archaeal and eukaryotic Trm5 . The catalytic mechanisms of TrmD- and Trm5-type enzymes differ, and kinetic assays that distinguish their activities have been described . The m1G37 modification of tRNAs contributes to the prevention of +1 frameshift errors during translation, particularly at the second codon of an open reading frame , and is required for translation of the proline-encoding CC[C/U] codons . CC[C/U] codons at codon 2 are overrepresented in ORFs encoding membrane proteins; accordingly, TrmD deficiency results in a variety of membrane-related phenotypes...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A873|protein.P0A873]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trmD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008576,ECOCYC:EG11023,GeneID:947099`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2744572-2745339:-; feature_type=gene
