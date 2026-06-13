---
entity_id: "gene.b0930"
entity_type: "gene"
name: "asnS"
source_database: "NCBI RefSeq"
source_id: "gene-b0930"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0930"
  - "asnS"
---

# asnS

`gene.b0930`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0930`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

asnS (gene.b0930) is a gene entity. It encodes asnS (protein.P0A8M0). Encoded protein function: Asparagine--tRNA ligase (EC 6.1.1.22) (Asparaginyl-tRNA synthetase) (AsnRS) EcoCyc product frame: ASNS-MONOMER. EcoCyc synonyms: lcs, tss. Genomic coordinates: 987585-988985. EcoCyc protein note: Asparagine—tRNA ligase (AsnRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. AsnRS belongs to the Class IIb aminoacyl-tRNA synthetases . AsnRS is a dimer in solution . Analysis of mutants suggests that the Y426 residue is involved in ATP binding ; a P231L mutation, which is located in the conserved motif 2 of class II aminoacyl-tRNA synthetases, leads to increases in the Km for asparagine and ATP . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E. coli has found that the required kcat values are on average 7.6-fold higher than those measured in vitro . Tss: "temperature-sensitive" AsnS: "asparaginyl-tRNA synthetase" Review:

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8M0|protein.P0A8M0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003162,ECOCYC:EG10094,GeneID:945555`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:987585-988985:-; feature_type=gene
