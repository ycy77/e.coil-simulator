---
entity_id: "gene.b2115"
entity_type: "gene"
name: "yehF"
source_database: "NCBI RefSeq"
source_id: "gene-b2115"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2115"
  - "yehF"
---

# yehF

`gene.b2115`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2115`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yehF (gene.b2115) is a gene entity. It encodes yehF (protein.P33345). Encoded protein function: FUNCTION: Has been implicated in selenate reduction; a mini-Tn10 insertion mutant in 'molR', (which was mapped to 47.3 centisomes i.e. this locus), is defective in the reduction of selenate. {ECO:0000269|PubMed:12480890}. EcoCyc product frame: EG11992-MONOMER. EcoCyc synonyms: molR_1, sosF, dinO. Genomic coordinates: 2196474-2197298. EcoCyc protein note: Expression of yehF appears to be regulated by LexA . A mini-Tn10 insertion mutant in "molR" is defective in the reduction of selenate . In E. coli K-12, the yehFGH open reading frames may in fact represent a single gene that is interrupted by a frameshift mutation. However, the size of the yehF mRNA, ~ 1 kb, is consistent with encoding the "interrupted" N-terminal 274 amino acid gene product of yehF . The molR gene has been assigned to this region, although in the original publication on molR , the gene was mapped between metC and argG at ~65 min. A molR mutant is defective in utilization of molybdate; it is thought to regulate the synthesis of ModE, a transcription factor regulating the expression of a molybdate-specific transporter .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33345|protein.P33345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yehF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006997,ECOCYC:EG11992,GeneID:946650`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2196474-2197298:+; feature_type=gene
