---
entity_id: "gene.b3987"
entity_type: "gene"
name: "rpoB"
source_database: "NCBI RefSeq"
source_id: "gene-b3987"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3987"
  - "rpoB"
---

# rpoB

`gene.b3987`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3987`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoB (gene.b3987) is a gene entity. It encodes rpoB (protein.P0A8V2). Encoded protein function: FUNCTION: DNA-dependent RNA polymerase (RNAP) catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. {ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:24843001}.; FUNCTION: Resistance to the antibiotics salinamide A, salinamide B, rifampicin, streptolydigin, CBR703, myxopyronin, and lipiarmycin can result from mutations in this protein. {ECO:0000269|PubMed:24843001, ECO:0000305|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. EcoCyc product frame: RPOB-MONOMER. EcoCyc synonyms: sdgB, tabD, stv, stl, ftsR, groN, nitB, rif. Genomic coordinates: 4181245-4185273. EcoCyc protein note: Along with its β' partner, the β subunit is integrally involved in the enzymatic function of RNA polymerase. Both the β and β' subunits interact with DNA and may contribute to the polymerase active site . Two conserved areas near the carboxy-terminus of RpoB are required for RNA polymerase assembly...

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8V2|protein.P0A8V2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013041,ECOCYC:EG10894,GeneID:948488`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4181245-4185273:+; feature_type=gene
