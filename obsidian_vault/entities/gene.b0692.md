---
entity_id: "gene.b0692"
entity_type: "gene"
name: "potE"
source_database: "NCBI RefSeq"
source_id: "gene-b0692"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0692"
  - "potE"
---

# potE

`gene.b0692`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0692`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

potE (gene.b0692) is a gene entity. It encodes potE (protein.P0AAF1). Encoded protein function: FUNCTION: Catalyzes both the uptake and excretion of putrescine. The uptake of putrescine is dependent on the membrane potential and the excretion involves putrescine-ornithine antiporter activity. {ECO:0000255|HAMAP-Rule:MF_02073, ECO:0000269|PubMed:1584788, ECO:0000269|PubMed:1939141, ECO:0000269|PubMed:9045651}. EcoCyc product frame: POTE-MONOMER. Genomic coordinates: 716946-718265. EcoCyc protein note: PotE is a putrescine transporter which mediates putrescine efflux by a putrescine:ornithine antiport reaction and putrescine import by proton symport. potE is located in an operon with speF encoding an inducible ornithine decarboxylase; production and excretion of putrescine may be beneficial for growth under acidic conditions (see ). Overexpression of potE in a polyamine-requiring strain increases putrescine uptake . PotE mediated putrescine uptake (measured in a polyamine requiring strain lacking the putrescine uptake systems PotABCD and PotFGHI) is dependent on membrane potential; uptake stimulates growth in the polyamine requiring mutant; uptake is inhibited by carbonyl cyanide m-chlorophenylhydrazone (CCCP), and by high concentrations of ornithine after putrescine accumulates in cells...

## Biological Role

Repressed by ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAF1|protein.P0AAF1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=potE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002360,ECOCYC:EG10753,GeneID:945422`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:716946-718265:-; feature_type=gene
