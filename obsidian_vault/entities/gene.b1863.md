---
entity_id: "gene.b1863"
entity_type: "gene"
name: "ruvC"
source_database: "NCBI RefSeq"
source_id: "gene-b1863"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1863"
  - "ruvC"
---

# ruvC

`gene.b1863`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1863`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ruvC (gene.b1863) is a gene entity. It encodes ruvC (protein.P0A814). Encoded protein function: FUNCTION: The RuvA-RuvB-RuvC complex processes Holliday junctions during genetic recombination and DNA repair (PubMed:6374379). Endonuclease that resolves Holliday junction (HJ) intermediates. Cleaves cruciform DNA by making single-stranded nicks across the junction at symmetrical positions within the homologous arms, leaving a 5'-phosphate and a 3'-hydroxyl group; requires a central core of homology in the junction (PubMed:10471285, PubMed:1661673, PubMed:1758493, PubMed:1829835, PubMed:36000732, PubMed:8001122, PubMed:8106500, PubMed:8195150, PubMed:9000618, PubMed:9135161, PubMed:9160752). The consensus cleavage sequence is 5'-(A/T)TT(C>G/A)-3'. Cleavage occurs on the 3'-side of the TT dinucleotide at the point of strand exchange, although there is some flexibility in the position cleaved (PubMed:10471285, PubMed:8001122, PubMed:8195150, PubMed:9135161). The cleavage reactions can be uncoupled; incision requires the presence of two consensus cleavage sequences, although they do not have to be identical (PubMed:9135161). The presence of a 5'-phosphate in a half-cut site accelerates cleavage of the second site, ensuring the second cleavage occurs within the lifetime of a single RuvC-HJ complex (PubMed:19399178)...

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A814|protein.P0A814]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006215,ECOCYC:EG10925,GeneID:946378`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1946855-1947376:-; feature_type=gene
