---
entity_id: "gene.b1692"
entity_type: "gene"
name: "ydiB"
source_database: "NCBI RefSeq"
source_id: "gene-b1692"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1692"
  - "ydiB"
---

# ydiB

`gene.b1692`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1692`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydiB (gene.b1692) is a gene entity. It encodes ydiB (protein.P0A6D5). Encoded protein function: FUNCTION: The actual biological function of YdiB remains unclear, nor is it known whether 3-dehydroshikimate or quinate represents the natural substrate. Catalyzes the reversible NAD-dependent reduction of both 3-dehydroshikimate (DHSA) and 3-dehydroquinate to yield shikimate (SA) and quinate, respectively. It can use both NAD or NADP for catalysis, however it has higher catalytic efficiency with NAD. {ECO:0000255|HAMAP-Rule:MF_01578, ECO:0000269|PubMed:12624088, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:15596430}. EcoCyc product frame: EG11234-MONOMER. Genomic coordinates: 1773789-1774655. EcoCyc protein note: YdiB was identified as a quinate/shikimate dehydrogenase. The low catalytic efficiency of YdiB with both quinate and shikimate suggests that neither may be the physiological substrate . Wild-type E. coli is not known to synthesize quinate or to use it as a source of carbon. Phylogenomic analysis of the shikimate dehydrogenase family showed that the two enzymes encoded in E. coli, AROE-MONOMER AroE and YdiB, belong to different subclasses; the authors suggested that YdiB was acquired by horizontal gene transfer. Common and subclass-specific catalytic residues and substrate binding motifs were identified . YdiB can use both NAD+ or NADP+ as a cosubstrate for catalysis...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6D5|protein.P0A6D5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydiB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005651,ECOCYC:EG11234,GeneID:946200`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1773789-1774655:+; feature_type=gene
