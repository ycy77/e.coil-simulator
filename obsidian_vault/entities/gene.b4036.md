---
entity_id: "gene.b4036"
entity_type: "gene"
name: "lamB"
source_database: "NCBI RefSeq"
source_id: "gene-b4036"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4036"
  - "lamB"
---

# lamB

`gene.b4036`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4036`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lamB (gene.b4036) is a gene entity. It encodes lamB (protein.P02943). Encoded protein function: FUNCTION: Involved in the transport of maltose and maltodextrins (PubMed:11742115, PubMed:2832377, PubMed:3301537, PubMed:7824948, PubMed:8805519, PubMed:9299337). Indispensable for translocation of maltodextrins (alpha 1-4 linked polyglucosyls) containing more than three glucosyl moieties. A hydrophobic path ('greasy slide') of aromatic residues serves to guide and select the sugars for transport through the channel (PubMed:11742115, PubMed:7824948, PubMed:8805519, PubMed:9299337). Also acts as a receptor for several bacteriophages including lambda (PubMed:4201774). Binds maltosaccharides; when LamB binds starch in soft agar, it inhibits motility (PubMed:2832377). {ECO:0000269|PubMed:11742115, ECO:0000269|PubMed:2832377, ECO:0000269|PubMed:3301537, ECO:0000269|PubMed:4201774, ECO:0000269|PubMed:7824948, ECO:0000269|PubMed:8805519, ECO:0000269|PubMed:9299337}. EcoCyc product frame: EG10528-MONOMER. EcoCyc synonyms: malL, malB. Genomic coordinates: 4247971-4249311.

## Biological Role

Activated by malT (protein.P06993), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02943|protein.P02943]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P06993|protein.P06993]] `RegulonDB` `C` - regulator=MalT; target=lamB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=lamB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013218,ECOCYC:EG10528,GeneID:948548`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4247971-4249311:+; feature_type=gene
