---
entity_id: "gene.b1961"
entity_type: "gene"
name: "dcm"
source_database: "NCBI RefSeq"
source_id: "gene-b1961"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1961"
  - "dcm"
---

# dcm

`gene.b1961`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1961`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcm (gene.b1961) is a gene entity. It encodes dcm (protein.P0AED9). Encoded protein function: FUNCTION: This methylase recognizes the double-stranded sequence 5'-CCWGG-3', methylates C-2 on both strands. {ECO:0000303|PubMed:12654995, ECO:0000305|PubMed:2198248}. EcoCyc product frame: EG10211-MONOMER. EcoCyc synonyms: mec. Genomic coordinates: 2030899-2032317. EcoCyc protein note: Dcm is a DNA cytosine methyltransferase that preferentially methylates sites of sequence 5' C-MeC-T 3' . This modification interferes with cleavage by the EcoRII restriction enzyme , but does not offer the cell full protection from EcoRII . Not all Dcm methylation sites are modified in vivo . The reaction catalyzed by Dcm has been characterized . Methylated cytosines are subject to deamination, which causes mutation of the C to a T, and Dcm and the product of the adjacent gene, Vsr, are associated with a corrective mismatch repair activity, very short patch (VSP) repair . Dcm has also affects transposition by Tn3 . Dcm is non-essential; a dcm mutant is viable . Dcm also has utility as a modification enzyme that interferes with cleavage by several restriction enzymes used in the molecular biology laboratory . Regulation has been described . Dcm: "DNA cytosine methylase" Mec: "5-methyl-cytosine" Reviews:

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AED9|protein.P0AED9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dcm; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006509,ECOCYC:EG10211,GeneID:946479`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2030899-2032317:-; feature_type=gene
