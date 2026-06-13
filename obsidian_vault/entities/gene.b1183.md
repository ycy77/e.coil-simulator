---
entity_id: "gene.b1183"
entity_type: "gene"
name: "umuD"
source_database: "NCBI RefSeq"
source_id: "gene-b1183"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1183"
  - "umuD"
---

# umuD

`gene.b1183`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1183`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

umuD (gene.b1183) is a gene entity. It encodes umuD (protein.P0AG11). Encoded protein function: FUNCTION: Involved in UV protection and mutation. Poorly processive, error-prone DNA polymerase involved in translesion repair (PubMed:10801133). Essential for induced (or SOS) mutagenesis. Able to replicate DNA across DNA lesions (thymine photodimers and abasic sites, called translesion synthesis) in the presence of activated RecA; efficiency is maximal in the presence of the beta sliding-clamp and clamp-loading complex of DNA polymerase III plus single-stranded binding protein (SSB) (PubMed:10801133). RecA and to a lesser extent the beta clamp-complex may target Pol V to replication complexes stalled at DNA template lesions (PubMed:10801133). {ECO:0000269|PubMed:10801133}. EcoCyc product frame: EG11057-MONOMER. Genomic coordinates: 1230767-1231186. EcoCyc protein note: Following induction of the SOS response, UmuD is proteolytically processed into UmuD' in a cleavage reaction that depends on activated RecA . UmuD has sequence similarity with LexA, which is also cleaved in a RecA-mediated fashion . This cleavage to produce UmuD' is required for UV mutagenesis and inclusion in the final Polymerase V (Pol V) protein complex . RecA does not actually cleave UmuD, instead somehow promoting cleavage of one member of an UmuD pair by its dimerization partner...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG11|protein.P0AG11]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=umuD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003974,ECOCYC:EG11057,GeneID:945746`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1230767-1231186:+; feature_type=gene
