---
entity_id: "gene.b1199"
entity_type: "gene"
name: "dhaL"
source_database: "NCBI RefSeq"
source_id: "gene-b1199"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1199"
  - "dhaL"
---

# dhaL

`gene.b1199`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1199`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dhaL (gene.b1199) is a gene entity. It encodes dhaL (protein.P76014). Encoded protein function: FUNCTION: ADP-binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone (PubMed:11350937). DhaL-ADP is converted to DhaL-ATP via a phosphoryl group transfer from DhaM and transmits it to dihydroxyacetone bound to DhaK (PubMed:11350937). DhaL also acts as coactivator of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:15616579). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:15616579). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:15616579). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15616579}. EcoCyc product frame: MONOMER0-1261. EcoCyc synonyms: ysgS, ycgS, dhaK2. Genomic coordinates: 1249125-1249757. EcoCyc protein note: DhaL is similar to the C-terminal half of the ATP-dependent dihydroxyacetone kinase of Citrobacter freundii and eukaryotes . DhaL contains bound ADP which is transiently phosphorylated as a cofactor in the kinase reaction . Crystal structures of the DhaL-ADP complex and the DhaK-DhaL complex have been solved...

## Biological Role

Activated by ygfI (protein.P52044).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76014|protein.P76014]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `S` - regulator=SrsR; target=dhaL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004026,ECOCYC:G6626,GeneID:945748`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1249125-1249757:-; feature_type=gene
