---
entity_id: "gene.b2801"
entity_type: "gene"
name: "fucP"
source_database: "NCBI RefSeq"
source_id: "gene-b2801"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2801"
  - "fucP"
---

# fucP

`gene.b2801`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2801`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucP (gene.b2801) is a gene entity. It encodes fucP (protein.P11551). Encoded protein function: FUNCTION: Mediates the uptake of L-fucose across the boundary membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2829831, PubMed:8052131). Can also transport L-galactose and D-arabinose, but at reduced rates compared with L-fucose. Is not able to transport L-rhamnose and L-arabinose (PubMed:2829831). Binds D-arabinose with the highest affinity, followed by L-fucose, and then by L-galactose (PubMed:9826601). {ECO:0000269|PubMed:2829831, ECO:0000269|PubMed:8052131, ECO:0000269|PubMed:9826601}. EcoCyc product frame: FUCP-MONOMER. Genomic coordinates: 2934235-2935551. EcoCyc protein note: FucP is an L-fucose/proton symporter responsible for the uptake of L-fucose. Imported fucose is metabolised to dihydroxyacetone phosphate and L-lactaldehyde by the action of FucI, FucK and FucA. FucP is a member of the major facilitator superfamily (MFS) of transporters . FucP has been overexpressed to a high level and shown in whole cells to mediate L-fucose/proton symport . L-fucose transport in membrane vesicles is inhibited by protonophores and ionophores . L-galactose, D-arabinose, and fructose have also been shown to be substrates, but unlike L-fucose, they do not act as inducers...

## Biological Role

Repressed by spf (gene.b3864). Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11551|protein.P11551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=fucP; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucP; function=+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=fucP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009187,ECOCYC:EG10352,GeneID:947487`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2934235-2935551:+; feature_type=gene
