---
entity_id: "gene.b2679"
entity_type: "gene"
name: "proX"
source_database: "NCBI RefSeq"
source_id: "gene-b2679"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2679"
  - "proX"
---

# proX

`gene.b2679`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2679`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proX (gene.b2679) is a gene entity. It encodes proX (protein.P0AFM2). Encoded protein function: FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake. Binds glycine betaine and proline betaine with high affinity. {ECO:0000269|PubMed:14612446, ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450}. EcoCyc product frame: PROX-MONOMER. EcoCyc synonyms: osrA, proU. Genomic coordinates: 2807132-2808124. EcoCyc protein note: ProX is the periplasmic binding protein of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. Purified ProX consists of two globular domains connected through a hinge region; a ligand binding site is located in a cleft between the two domains and three tryptophan residues are directly implicated in binding quaternary ammonium groups .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFM2|protein.P0AFM2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=proX; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=proX; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=proX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008818,ECOCYC:EG10773,GeneID:947165`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2807132-2808124:+; feature_type=gene
