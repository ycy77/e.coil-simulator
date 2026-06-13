---
entity_id: "gene.b0112"
entity_type: "gene"
name: "aroP"
source_database: "NCBI RefSeq"
source_id: "gene-b0112"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0112"
  - "aroP"
---

# aroP

`gene.b0112`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0112`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroP (gene.b0112) is a gene entity. It encodes aroP (protein.P15993). Encoded protein function: FUNCTION: Permease that is involved in the active transport across the cytoplasmic membrane of all three aromatic amino acids, phenylalanine, tyrosine and tryptophan. {ECO:0000269|PubMed:10735864, ECO:0000269|PubMed:4919744, ECO:0000269|PubMed:9150230}. EcoCyc product frame: AROP-MONOMER. EcoCyc synonyms: aroR. Genomic coordinates: 120178-121551. EcoCyc protein note: AroP is an aromatic amino acid permease that is a member of the APC Superfamily of transporters . AroP is referred to as the general aromatic amino acid permease because it is responsible for the transport of all three aromatic amino acids, phenylalanine, tyrosine, and tryptophan, across the inner membrane . Based on the hydrophobicity profile and distribution of charged amino acid residues, AroP was shown to have 12 membrane-spanning regions connected by hydrophilic loops . This topographical model is very similar to that reported for the PheP permease, a phenylalanine-specific transporter, which has 61% amino acid sequence identity with the AroP permease. However, despite their high degree of sequence similarity, the substrate specificities and affinities of the AroP and PheP permeases differ . AroP transports each of the aromatic amino acids with a Km of less than 1 μM...

## Biological Role

Repressed by tyrR (protein.P07604), glaR (protein.P37338). Activated by ArgR-L-arginine DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-228), DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), rpoD (protein.P00579), argR (protein.P0A6D0), fnr (protein.P0A9E5), cra (protein.P0ACP1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15993|protein.P15993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroP; function=+
- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=aroP; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aroP; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=aroP; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=aroP; function=-
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=aroP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000384,ECOCYC:EG10084,GeneID:946018`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:120178-121551:-; feature_type=gene
