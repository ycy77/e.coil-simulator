---
entity_id: "gene.b1091"
entity_type: "gene"
name: "fabH"
source_database: "NCBI RefSeq"
source_id: "gene-b1091"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1091"
  - "fabH"
---

# fabH

`gene.b1091`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1091`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabH (gene.b1091) is a gene entity. It encodes fabH (protein.P0A6R0). Encoded protein function: FUNCTION: Catalyzes the condensation reaction of fatty acid synthesis by the addition to an acyl acceptor of two carbons from malonyl-ACP. Catalyzes the first condensation reaction which initiates fatty acid synthesis and may therefore play a role in governing the total rate of fatty acid production. Possesses both acetoacetyl-ACP synthase and acetyl transacylase activities. Has some substrate specificity for acetyl-CoA. Its substrate specificity determines the biosynthesis of straight-chain of fatty acids instead of branched-chain (PubMed:10629181, PubMed:7592873, PubMed:8631920, PubMed:8910376). Can also use propionyl-CoA, with lower efficiency (PubMed:10629181, PubMed:8631920). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8631920, ECO:0000269|PubMed:8910376}. EcoCyc product frame: FABH-MONOMER. Genomic coordinates: 1148759-1149712.

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6R0|protein.P0A6R0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fabH; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=fabH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003696,ECOCYC:EG10277,GeneID:946003`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1148759-1149712:+; feature_type=gene
