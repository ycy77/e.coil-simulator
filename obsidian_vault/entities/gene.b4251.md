---
entity_id: "gene.b4251"
entity_type: "gene"
name: "bdcR"
source_database: "NCBI RefSeq"
source_id: "gene-b4251"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4251"
  - "bdcR"
---

# bdcR

`gene.b4251`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4251`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bdcR (gene.b4251) is a gene entity. It encodes bdcR (protein.P39334). Encoded protein function: FUNCTION: Negatively regulates expression of bdcA. {ECO:0000269|PubMed:21059164}. EcoCyc product frame: G7882-MONOMER. EcoCyc synonyms: yjgJ. Genomic coordinates: 4474124-4474717. EcoCyc protein note: The BcdR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . BdcR: "biofilm dispersal via c-di-GMP"

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39334|protein.P39334]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=bdcR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013918,ECOCYC:G7882,GeneID:948775`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4474124-4474717:+; feature_type=gene
