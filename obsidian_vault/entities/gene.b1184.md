---
entity_id: "gene.b1184"
entity_type: "gene"
name: "umuC"
source_database: "NCBI RefSeq"
source_id: "gene-b1184"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1184"
  - "umuC"
---

# umuC

`gene.b1184`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1184`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

umuC (gene.b1184) is a gene entity. It encodes umuC (protein.P04152). Encoded protein function: FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}. EcoCyc product frame: EG11056-MONOMER. EcoCyc synonyms: uvm. Genomic coordinates: 1231186-1232454. EcoCyc protein note: UmuC is a DNA polymerase specialized for trans-lesion synthesis (TLS) in E. coli K-12 . UmuC requires UmuD', RecA and SSB for TLS in vitro UmuC is degraded by the Lon protease, limiting total UmuC abundance . Most, but not all UV-induced mutation requires functional UmuC . Loss of umuC results in UV sensitivity and difficulty repairing daughter strand gaps, but not double-strand breaks . UmuC is required for some spontaneous base-pair substitutions...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04152|protein.P04152]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=umuC; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=umuC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003977,ECOCYC:EG11056,GeneID:946359`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1231186-1232454:+; feature_type=gene
