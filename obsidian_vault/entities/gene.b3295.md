---
entity_id: "gene.b3295"
entity_type: "gene"
name: "rpoA"
source_database: "NCBI RefSeq"
source_id: "gene-b3295"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3295"
  - "rpoA"
---

# rpoA

`gene.b3295`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3295`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpoA (gene.b3295) is a gene entity. It encodes rpoA (protein.P0A7Z4). Encoded protein function: FUNCTION: DNA-dependent RNA polymerase (RNAP) catalyzes the transcription of DNA into RNA using the four ribonucleoside triphosphates as substrates. This subunit plays an important role in subunit assembly since its dimerization is the first step in the sequential assembly of subunits to form the holoenzyme. {ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:24843001}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNAP. It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. {ECO:0000269|PubMed:32871103}. EcoCyc product frame: EG10893-MONOMER. EcoCyc synonyms: pez, phs, sez. Genomic coordinates: 3440040-3441029. EcoCyc protein note: RpoA is the α subunit of the RNA polymerase core enzyme. It consists of two domains connected by a flexible linker. The RpoA amino-terminus is both necessary and sufficient for dimerization of RpoA and subsequent assembly of the RNA polymerase core complex . The amino-terminus has been analyzed both by NMR and via a 2.5 Å resolution crystal structure...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03020` RNA polymerase (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7Z4|protein.P0A7Z4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpoA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010802,ECOCYC:EG10893,GeneID:947794`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3440040-3441029:-; feature_type=gene
