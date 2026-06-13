---
entity_id: "gene.b2684"
entity_type: "gene"
name: "mprA"
source_database: "NCBI RefSeq"
source_id: "gene-b2684"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2684"
  - "mprA"
---

# mprA

`gene.b2684`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2684`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mprA (gene.b2684) is a gene entity. It encodes mprA (protein.P0ACR9). Encoded protein function: FUNCTION: Negative regulator of the multidrug operon mprA-emrAB (emrRAB) (PubMed:10991887, PubMed:31633764, PubMed:7730261). Binds directly to a promoter in its own operon mprA-emrAB; binding is inhibited by probable inducers of the operon, some of which are also substrates of the efflux pump EmrAB-TolC (PubMed:10991887). {ECO:0000269|PubMed:10991887, ECO:0000269|PubMed:31633764, ECO:0000269|PubMed:7730261}. EcoCyc product frame: EG10603-MONOMER. EcoCyc synonyms: emrR. Genomic coordinates: 2810770-2811300.

## Biological Role

Repressed by mprA (protein.P0ACR9). Activated by Putrescine (molecule.C00134), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACR9|protein.P0ACR9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[molecule.C00134|molecule.C00134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Translation
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mprA; function=+
- `represses` <-- [[protein.P0ACR9|protein.P0ACR9]] `RegulonDB` `S` - regulator=MprA; target=mprA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008834,ECOCYC:EG10603,GeneID:945282`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2810770-2811300:+; feature_type=gene
