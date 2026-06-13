---
entity_id: "gene.b1087"
entity_type: "gene"
name: "yceF"
source_database: "NCBI RefSeq"
source_id: "gene-b1087"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1087"
  - "yceF"
---

# yceF

`gene.b1087`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1087`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yceF (gene.b1087) is a gene entity. It encodes yceF (protein.P0A729). Encoded protein function: FUNCTION: Nucleoside triphosphate pyrophosphatase that hydrolyzes 7-methyl-GTP (m(7)GTP) (PubMed:24210219). May have a dual role in cell division arrest and in preventing the incorporation of modified nucleotides into cellular nucleic acids (PubMed:24210219). {ECO:0000269|PubMed:24210219}. EcoCyc product frame: EG11438-MONOMER. Genomic coordinates: 1146011-1146595. EcoCyc protein note: YceF shows triphosphatase activity with the modified nucleotide 7-methyl-GTP (m7GTP) as a substrate. The authors suggest that the in vivo function of YceF may be to monitor the ribonucleotide pool and prevent unspecific incorporation of modified bases into cellular RNAs . YceF exists as a mixture of monomers and dimers in solution. A crystal structure of the protein has been solved at 1.85 Å resolution . Mutations in predicted active site residues reduce the catalytic activity. The unprotonated Asp69 residue is proposed to function as a general base that produces a nucleophilic hydroxide ion which attacks the α-phosphate of the substrate .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A729|protein.P0A729]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0003678,ECOCYC:EG11438,GeneID:945631`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1146011-1146595:-; feature_type=gene
