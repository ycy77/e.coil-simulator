---
entity_id: "gene.b2113"
entity_type: "gene"
name: "mrp"
source_database: "NCBI RefSeq"
source_id: "gene-b2113"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2113"
  - "mrp"
---

# mrp

`gene.b2113`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2113`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrp (gene.b2113) is a gene entity. It encodes mrp (protein.P0AF08). Encoded protein function: FUNCTION: Binds and transfers iron-sulfur (Fe-S) clusters to target apoproteins. Can hydrolyze ATP. {ECO:0000255|HAMAP-Rule:MF_02040}. EcoCyc product frame: EG10611-MONOMER. Genomic coordinates: 2193059-2194168. EcoCyc protein note: Mrp is a member of the Mrp/Nbp35 subfamily of the P-loop NTPases . The Salmonella typhimurium ortholog, ApbC, is an ATPase that is able to bind and transfer iron-sulfur clusters . Its originally proposed role in thiamine biosynthesis is likely indirect. Mrp: "metG-related protein" (Note: mrp is not related to metG other than by proximity in the genome) Review:

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF08|protein.P0AF08]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mrp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006987,ECOCYC:EG10611,GeneID:946627`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2193059-2194168:-; feature_type=gene
