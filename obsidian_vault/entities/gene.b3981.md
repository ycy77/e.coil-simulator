---
entity_id: "gene.b3981"
entity_type: "gene"
name: "secE"
source_database: "NCBI RefSeq"
source_id: "gene-b3981"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3981"
  - "secE"
---

# secE

`gene.b3981`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3981`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

secE (gene.b3981) is a gene entity. It encodes secE (protein.P0AG96). Encoded protein function: FUNCTION: Essential subunit of the protein translocation channel SecYEG. Clamps together the 2 halves of SecY. May contact the channel plug during translocation. Overexpression of some hybrid proteins has been thought to jam the protein secretion apparatus resulting in cell death; while this may be true it also results in FtsH-mediated degradation of SecY. {ECO:0000269|PubMed:15140892}. EcoCyc product frame: SECE. EcoCyc synonyms: mbrC, prlG. Genomic coordinates: 4177358-4177741. EcoCyc protein note: The SecE inner membrane protein is a component of the heterotrimeric SecYEG preprotein translocase. SecY, SecE and SecG form a stable complex which supports precursor protein translocation in vitro . A cold sensitive SecE mutant (SecEcsE501) accumulates the precursor form of periplasmic and envelope proteins (MBP, LamB and RBP) when grown at the non-permissive temperature ; the SecEcsE501 allele is an alteration to the concensus ribosome binding site that results in decreased expression of secE . SecE is an inner membrane protein with three predicted transmembrane regions . SecE is essential for growth; a truncated SecE (secEΔ7-78) functions effectively in vivo . prl alleles of secE which suppress a variety of signal sequence mutations have been characterized...

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG96|protein.P0AG96]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013023,ECOCYC:EG10939,GeneID:948486`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4177358-4177741:+; feature_type=gene
