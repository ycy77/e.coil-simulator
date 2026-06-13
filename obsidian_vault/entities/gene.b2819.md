---
entity_id: "gene.b2819"
entity_type: "gene"
name: "recD"
source_database: "NCBI RefSeq"
source_id: "gene-b2819"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2819"
  - "recD"
---

# recD

`gene.b2819`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2819`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recD (gene.b2819) is a gene entity. It encodes recD (protein.P04993). Encoded protein function: FUNCTION: A helicase/nuclease that prepares dsDNA breaks (DSB) for recombinational DNA repair. Binds to DSBs and unwinds DNA via a rapid (>1 kb/second) and highly processive (>30 kb) ATP-dependent bidirectional helicase. Unwinds dsDNA until it encounters a Chi (crossover hotspot instigator, 5'-GCTGGTGG-3') sequence from the 3' direction. Cuts ssDNA a few nucleotides 3' to Chi site, by nicking one strand or switching the strand degraded (depending on the reaction conditions). The properties and activities of the enzyme are changed at Chi. The Chi-altered holoenzyme produces a long 3'-ssDNA overhang which facilitates RecA-binding to the ssDNA for homologous DNA recombination and repair. In the holoenzyme this subunit contributes ssDNA-dependent ATPase and fast 5'-3' helicase activity. When added to pre-assembled RecBC greatly stimulates nuclease activity and augments holoenzyme processivity. Negatively regulates the RecA-loading ability of RecBCD. The RecBCD complex does not unwind G-quadruplex DNA (PubMed:9765292)...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P04993|protein.P04993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=recD; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `C` - regulator=LexA; target=recD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009247,ECOCYC:EG10826,GeneID:947287`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2950635-2952461:-; feature_type=gene
