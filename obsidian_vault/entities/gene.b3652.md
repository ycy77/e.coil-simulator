---
entity_id: "gene.b3652"
entity_type: "gene"
name: "recG"
source_database: "NCBI RefSeq"
source_id: "gene-b3652"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3652"
  - "recG"
---

# recG

`gene.b3652`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3652`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recG (gene.b3652) is a gene entity. It encodes recG (protein.P24230). Encoded protein function: FUNCTION: Genetic interactions indicate that RecG or RadD are required for DNA repair in every replication cycle; they function in different pathways, each is essential in the absence of the other (PubMed:32644157). Plays a critical role in recombination and DNA repair (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:9265736, PubMed:10871364, PubMed:32644157). RecG or RadD are required for DNA maintenance in every replication cycle (PubMed:32644157). Helps process Holliday junction (HJ) intermediates to mature products by catalyzing branch migration (PubMed:8428576, PubMed:7957087, PubMed:8127666, PubMed:10871364). Has replication fork regression activity, unwinds stalled or blocked replication forks to make a HJ that can be resolved by RuvC or RusA (PubMed:10778854, PubMed:11459957). Also rewinds unwound dsDNA in an ATP-dependent manner (PubMed:24013402). Has double-stranded (ds)DNA unwinding activity characteristic of a DNA helicase with 3'-5' polarity in vitro on linear dsDNA; branched duplex DNA (Y-DNA) substrates adopt different conformations that influence which of the two arms are unwound (PubMed:7957087)...

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24230|protein.P24230]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011939,ECOCYC:EG10829,GeneID:948162`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3825210-3827291:+; feature_type=gene
