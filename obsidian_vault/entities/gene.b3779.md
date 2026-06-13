---
entity_id: "gene.b3779"
entity_type: "gene"
name: "gpp"
source_database: "NCBI RefSeq"
source_id: "gene-b3779"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3779"
  - "gpp"
---

# gpp

`gene.b3779`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3779`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpp (gene.b3779) is a gene entity. It encodes gppA (protein.P25552). Encoded protein function: FUNCTION: Catalyzes the conversion of pppGpp to ppGpp. Guanosine pentaphosphate (pppGpp) is a cytoplasmic signaling molecule which together with ppGpp controls the 'stringent response', an adaptive process that allows bacteria to respond to amino acid starvation, resulting in the coordinated regulation of numerous cellular activities (PubMed:6130093, PubMed:8394006). In vitro, can hydrolyze pppGp (PubMed:6130093). Also has exopolyphosphatase activity, catalyzing the release of orthophosphate by processive hydrolysis of the phosphoanyhydride bonds of polyphosphate chains (1000 residues) (PubMed:8394006). {ECO:0000269|PubMed:6130093, ECO:0000269|PubMed:8394006}. EcoCyc product frame: PPPGPPHYDRO-MONOMER. EcoCyc synonyms: gppA. Genomic coordinates: 3962745-3964229.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25552|protein.P25552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012347,ECOCYC:EG10413,GeneID:948291`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3962745-3964229:-; feature_type=gene
