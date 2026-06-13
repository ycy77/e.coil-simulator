---
entity_id: "gene.b2820"
entity_type: "gene"
name: "recB"
source_database: "NCBI RefSeq"
source_id: "gene-b2820"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2820"
  - "recB"
---

# recB

`gene.b2820`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2820`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recB (gene.b2820) is a gene entity. It encodes recB (protein.P08394). Encoded protein function: FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. Holoenzyme degrades any linearized DNA that is unable to undergo homologous recombination (PubMed:123277, PubMed:4552016, PubMed:4562392). In the holoenzyme this subunit contributes ATPase, 3'-5' helicase, exonuclease activity and loads RecA onto ssDNA. The RecBC complex requires the RecD subunit for nuclease activity, but can translocate along ssDNA in both directions. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292)...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08394|protein.P08394]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=recB; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=recB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009249,ECOCYC:EG10824,GeneID:947286`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2952461-2956003:-; feature_type=gene
