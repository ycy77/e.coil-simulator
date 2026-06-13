---
entity_id: "gene.b2628"
entity_type: "gene"
name: "abpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2628"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2628"
  - "abpA"
---

# abpA

`gene.b2628`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2628`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

abpA (gene.b2628) is a gene entity. It encodes abpA (protein.P52127). Encoded protein function: FUNCTION: Part of an antiviral system composed of AbpA and AbpB; when both are expressed from a plasmid they confer resistance to phages T2, T4, T7 and lambda but not RB32 or RB69. Resistance is temperature dependent, it can be seen at 30 degrees Celsius but not at 37 or 42 degrees Celsius. The system impairs phage but not bacterial DNA synthesis (shown for T4, T7 and lambda). Partially suppressed by mutations in T4 gene 41, a replicative helicase. {ECO:0000269|PubMed:25224971}. EcoCyc product frame: G7363-MONOMER. EcoCyc synonyms: yfjL. Genomic coordinates: 2763537-2765153. EcoCyc protein note: AbpA together with G7362-MONOMER operate together as a bacteriophage defense system against several types of bacteriophage. AbpAB defense system is activated by phage single-stranded binding (SSB) protein bound to E. coli ssDNA; it is also activated in the absence of phage infections by chemically interrupting E. coli's DNA replication or by deleting DNA repair factors RecB and RecC . Overexpression of AbpA and AbpB together from a plasmid blocks the propagation of T2, T4, T7, and λ family bacteriophages at 30°C, but not 37 or 42°C. The AbpAB proteins impair phage DNA synthesis, but not bacterial DNA synthesis...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52127|protein.P52127]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=abpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0008650,ECOCYC:G7363,GeneID:947110`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2763537-2765153:-; feature_type=gene
