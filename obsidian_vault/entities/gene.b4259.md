---
entity_id: "gene.b4259"
entity_type: "gene"
name: "holC"
source_database: "NCBI RefSeq"
source_id: "gene-b4259"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4259"
  - "holC"
---

# holC

`gene.b4259`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4259`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

holC (gene.b4259) is a gene entity. It encodes holC (protein.P28905). Encoded protein function: FUNCTION: Part of the beta sliding clamp loading complex, which hydrolyzes ATP to load the beta clamp onto primed DNA to form the DNA replication pre-initiation complex (PubMed:2040637). DNA polymerase III is a complex, multichain enzyme responsible for most of the replicative synthesis in bacteria. This DNA polymerase also exhibits 3' to 5' exonuclease activity. Genetically identified as involved in the repair of replication forks and tolerance of the chain-terminating nucleoside analog 3' AZT (PubMed:26544712, PubMed:33582602, PubMed:34181484). This subunit may stabilize YoaA and/or stimulate the helicase activity of YoaA (PubMed:36509145). {ECO:0000269|PubMed:2040637, ECO:0000269|PubMed:26544712, ECO:0000269|PubMed:33582602, ECO:0000269|PubMed:34181484, ECO:0000269|PubMed:36509145}. EcoCyc product frame: EG11413-MONOMER. Genomic coordinates: 4483837-4484280. EcoCyc protein note: HolC is the χ subunit of the χ-ψ dimer. χ has more recently been found to form a complex with G6992-MONOMER in vitro. The YoaA-χ dimer has DNA-dependent helicase activity and requires a 5' single-stranded overhang or ssDNA gap for DNA unwinding; YoaA-χ unwinds DNA with a 5' flap and various types of damaged DNA (see )...

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03430` Mismatch repair (KEGG)
- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28905|protein.P28905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=holC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013948,ECOCYC:EG11413,GeneID:948787`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4483837-4484280:-; feature_type=gene
