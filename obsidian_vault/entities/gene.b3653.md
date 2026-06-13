---
entity_id: "gene.b3653"
entity_type: "gene"
name: "gltS"
source_database: "NCBI RefSeq"
source_id: "gene-b3653"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3653"
  - "gltS"
---

# gltS

`gene.b3653`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3653`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gltS (gene.b3653) is a gene entity. It encodes gltS (protein.P0AER8). Encoded protein function: FUNCTION: Catalyzes the sodium-dependent, binding-protein-independent transport of glutamate. {ECO:0000255|HAMAP-Rule:MF_02062, ECO:0000269|PubMed:2537813, ECO:0000269|PubMed:336628, ECO:0000269|PubMed:8596452}. EcoCyc product frame: GLTS-MONOMER. EcoCyc synonyms: gltC. Genomic coordinates: 3827460-3828665. EcoCyc protein note: E. coli contains four transporters for the uptake of glutamate (GltIJKL, GltP, GltS, and GadC). GltS accounts for approximately 25% of the total wild-type transport velocity of glutamate in aerobic growth with succinate and 40 mM NaCl . The membrane topology of GltS has been studied using PhoA and LacZ fusions to identify transmembrane segments and cytoplasmic and periplasmic domains . It was also studied using cysteine accessibility experiments of single-cysteine mutants . Both studies predict 10 transmembrane segments for the protein but differ slightly in their positions. GltS is a sodium dependent glutamate transporter which is specific for D- and L-glutamate. E. coli K12 cannot grow on glutamate as a sole carbon and nitrogen source. Selection of mutants which can grow on glutamate (Glt+) are typically due to mutations which overexpress either the GltS or GltP glutamate transporters...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AER8|protein.P0AER8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011941,ECOCYC:EG10406,GeneID:948166`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3827460-3828665:-; feature_type=gene
