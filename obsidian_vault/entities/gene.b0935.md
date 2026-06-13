---
entity_id: "gene.b0935"
entity_type: "gene"
name: "ssuD"
source_database: "NCBI RefSeq"
source_id: "gene-b0935"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0935"
  - "ssuD"
---

# ssuD

`gene.b0935`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0935`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssuD (gene.b0935) is a gene entity. It encodes ssuD (protein.P80645). Encoded protein function: FUNCTION: Involved in desulfonation of aliphatic sulfonates. Catalyzes the conversion of pentanesulfonate to sulfite and pentaldehyde and is able to desulfonate a wide range of sulfonated substrates including C-2 to C-10 unsubstituted linear alkanesulfonates, substituted ethanesulfonic acids and sulfonated buffers. {ECO:0000269|PubMed:10480865}. EcoCyc product frame: MONOMER-162. EcoCyc synonyms: ssi6, ycbN. Genomic coordinates: 994843-995988. EcoCyc protein note: E. coli can utilize alkanesulfonates as a sulfur source for growth. The ssuD gene encodes an FMNH2-dependent alkanesulfonate monooxygenase with a broad substrate range. It was reported that the enzyme is able to desulfonate C-2 to C-10 unsubstituted alkanesulfonates, substituted ethanesulfonic acids, N-phenyltaurine, 4-phenyl-1-butanesulfonate and certain sulfonated buffers. The best substrates for the monooxygenase were CPD0-2546, CPD0-2547 and CPD0-1957 . High expression levels of ssuD and a relatively longer lag period appear to be required for the utilization of short-carbon-chain sulfonates, taurine, methanesulfonate and L-cysteate, in tauD cynN double mutants; however whether SsuD directly cleaves taurine is not known...

## Biological Role

Repressed by cysB (protein.P0A9F3). Activated by rpoD (protein.P00579), cbl (protein.Q47083).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P80645|protein.P80645]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssuD; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=ssuD; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=ssuD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003178,ECOCYC:G6477,GeneID:945557`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:994843-995988:-; feature_type=gene
