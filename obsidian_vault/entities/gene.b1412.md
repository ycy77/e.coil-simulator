---
entity_id: "gene.b1412"
entity_type: "gene"
name: "azoR"
source_database: "NCBI RefSeq"
source_id: "gene-b1412"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1412"
  - "azoR"
---

# azoR

`gene.b1412`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1412`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

azoR (gene.b1412) is a gene entity. It encodes azoR (protein.P41407). Encoded protein function: FUNCTION: Quinone reductase that provides resistance to thiol-specific stress caused by electrophilic quinones. Can reduce several benzo-, naphtho-, and anthraquinone compounds. {ECO:0000269|PubMed:19666717}.; FUNCTION: Also exhibits azoreductase activity (PubMed:11583992, PubMed:18337254). Catalyzes the reductive cleavage of the azo bond in aromatic azo compounds to the corresponding amines (PubMed:11583992, PubMed:18337254). Can reduce ethyl red, methyl red and p-methyl red, but is not able to convert sulfonated azo dyes (PubMed:11583992, PubMed:18337254, PubMed:23795903). The stoichiometry implies that 2 cycles of the ping-pong mechanism are required for the cleavage of the azo bond (PubMed:11583992). Can also act as a nitroreductase and is able to reduce nitro compounds such as 7-nitrocoumarin-3-carboxylic acid (7NCCA) (PubMed:23795903). {ECO:0000269|PubMed:11583992, ECO:0000269|PubMed:18337254, ECO:0000269|PubMed:23795903}. EcoCyc product frame: G6731-MONOMER. EcoCyc synonyms: acpD. Genomic coordinates: 1482255-1482860. EcoCyc protein note: AzoR is an NADH:quinone oxidoreductase with a role in protection against thiol-specific stress. Purified AzoR is active on a variety of electrophilic quinones...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41407|protein.P41407]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=azoR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004712,ECOCYC:G6731,GeneID:947569`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1482255-1482860:-; feature_type=gene
