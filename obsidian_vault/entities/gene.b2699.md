---
entity_id: "gene.b2699"
entity_type: "gene"
name: "recA"
source_database: "NCBI RefSeq"
source_id: "gene-b2699"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2699"
  - "recA"
---

# recA

`gene.b2699`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2699`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recA (gene.b2699) is a gene entity. It encodes recA (protein.P0A7G6). Encoded protein function: FUNCTION: Required for homologous recombination and the bypass of mutagenic DNA lesions by the SOS response. Catalyzes ATP-driven homologous pairing and strand exchange of DNA molecules necessary for DNA recombinational repair. Catalyzes the hydrolysis of ATP in the presence of single-stranded DNA, the ATP-dependent uptake of single-stranded DNA by duplex DNA, and the ATP-dependent hybridization of homologous single-stranded DNAs. The SOS response controls an apoptotic-like death (ALD) induced (in the absence of the mazE-mazF toxin-antitoxin module) in response to DNA damaging agents that is mediated by RecA and LexA (PubMed:22412352). Decreased expression suppresses a double radD-recG deletion (PubMed:32644157). {ECO:0000269|PubMed:22412352, ECO:0000269|PubMed:26845522, ECO:0000269|PubMed:32644157, ECO:0000269|PubMed:35150260, ECO:0000269|PubMed:7608206, ECO:0000269|PubMed:9230304}.; FUNCTION: Mutations in this gene were selected in directed evolution experiments for resistance to intense ionizing radiation (3000 Gy). {ECO:0000269|PubMed:24596148}. EcoCyc product frame: EG10823-MONOMER. EcoCyc synonyms: zab, umuB, tif, lexB, recH, rnmB, srf. Genomic coordinates: 2822708-2823769...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7G6|protein.P0A7G6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=recA; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=recA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008876,ECOCYC:EG10823,GeneID:947170`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2822708-2823769:-; feature_type=gene
