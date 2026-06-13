---
entity_id: "gene.b1714"
entity_type: "gene"
name: "pheS"
source_database: "NCBI RefSeq"
source_id: "gene-b1714"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1714"
  - "pheS"
---

# pheS

`gene.b1714`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1714`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pheS (gene.b1714) is a gene entity. It encodes pheS (protein.P08312). Encoded protein function: Phenylalanine--tRNA ligase alpha subunit (EC 6.1.1.20) (Phenylalanyl-tRNA synthetase alpha subunit) (PheRS) EcoCyc product frame: PHES-MONOMER. EcoCyc synonyms: phe-act. Genomic coordinates: 1797959-1798942. EcoCyc protein note: The α subunit of PheRS (also called PheTS) contains the phenylalanine binding site within the conserved motif 2 and motif 3 of the protein . It interacts with the 3'-adenosine of tRNAPhe . Isolated α subunits exist primarily as dimers . The pheS5 mutant allele (leading to a G98D change in amino acid sequence) causes temperature-sensitive PheRS activity . Intragenic supressors of the pheS5 mutation have been isolated and analyzed . The temperature-sensitive fitA76 and fit95 mutants related to pheS and pheT, respectively, have been genetically characterized . There is a general discrepancy between kcat values of aminoacyl-tRNA synthetases that were measured in vitro and values that were calculated as needed to support measured growth rates . Modeling of these parameters in E. coli has found that the required kcat values are on average 7.6-fold higher than those measured in vitro . Reviews:

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08312|protein.P08312]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005722,ECOCYC:EG10709,GeneID:946223`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1797959-1798942:-; feature_type=gene
