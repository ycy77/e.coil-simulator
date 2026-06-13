---
entity_id: "gene.b2532"
entity_type: "gene"
name: "trmJ"
source_database: "NCBI RefSeq"
source_id: "gene-b2532"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2532"
  - "trmJ"
---

# trmJ

`gene.b2532`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2532`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trmJ (gene.b2532) is a gene entity. It encodes trmJ (protein.P0AE01). Encoded protein function: FUNCTION: Catalyzes the formation of 2'O-methylated cytidine (Cm32) or 2'O-methylated uridine (Um32) at position 32 in tRNA (PubMed:16848900, PubMed:24951554, PubMed:26202969). Can also methylate adenosine or guanosine, even though these nucleosides are rare or absent at position 32 in the anticodon loop of tRNA (PubMed:24951554). {ECO:0000269|PubMed:16848900, ECO:0000269|PubMed:24951554, ECO:0000269|PubMed:26202969}. EcoCyc product frame: G7327-MONOMER. EcoCyc synonyms: yfhQ. Genomic coordinates: 2662583-2663323. EcoCyc protein note: TrmJ is the tRNA:Cm32/Um32 methyltransferase which introduces methyl groups at the 2'-O position of C32 and U32 of several tRNAs in vitro. The tRNAs 2'-O-methylated at the C/U32 position in vivo are glnW-tRNA and glnX-tRNA (at the U32 position), and metZ-tRNA, metY-tRNA, serT-tRNA and trpT-tRNA (at the C32 position) . TrmJ belongs to the SPOUT superfamily of methyltransferases . Sequence analysis suggests that the active sites of TrmH and TrmJ are conserved, and the enzymes may thus use a similar reaction mechanism . TrmJ does not show specificity for the nucleotide at the 32 position and can also methylate tRNAPro(GGG) in vitro...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE01|protein.P0AE01]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008332,ECOCYC:G7327,GeneID:948610`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2662583-2663323:-; feature_type=gene
