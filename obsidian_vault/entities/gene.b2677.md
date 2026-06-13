---
entity_id: "gene.b2677"
entity_type: "gene"
name: "proV"
source_database: "NCBI RefSeq"
source_id: "gene-b2677"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2677"
  - "proV"
---

# proV

`gene.b2677`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2677`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proV (gene.b2677) is a gene entity. It encodes proV (protein.P14175). Encoded protein function: FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}. EcoCyc product frame: PROV-MONOMER. EcoCyc synonyms: osrA, proU. Genomic coordinates: 2804815-2806017. EcoCyc protein note: ProV is the predicted ATP binding subunit of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. ProV contains signature motifs conserved in ATP-binding cassette (ABC) domains . ProV contains a cystathionine β-synthase (CBS) domain which has been implicated in osmosensing (see ) . proV is an experimentally validated antibiotic resistance gene (ARG) .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14175|protein.P14175]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=proV; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=proV; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=proV; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008814,ECOCYC:EG10771,GeneID:947148`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2804815-2806017:+; feature_type=gene
