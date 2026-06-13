---
entity_id: "gene.b3522"
entity_type: "gene"
name: "yhjD"
source_database: "NCBI RefSeq"
source_id: "gene-b3522"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3522"
  - "yhjD"
---

# yhjD

`gene.b3522`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3522`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhjD (gene.b3522) is a gene entity. It encodes yhjD (protein.P37642). Encoded protein function: Inner membrane protein YhjD EcoCyc product frame: EG12248-MONOMER. Genomic coordinates: 3673362-3674375. EcoCyc protein note: YhjD is predicted to be an inner membrane protein with six transmembrane domains; experimental topology analysis suggests the C-terminus is located in the cytoplasm . yhjD shows strong alleviating interactions with components of lptBCFG and aggravating interactions with lptA, lptD and msbA (growth in rich medium at 32°C) . Strains lacking yhjD show signs of defective lipoplysaccharide transport such as periplasmic bodies and membranous projections . YhjD co-purifies with LptB and recombinant YhjD binds to core Lipid A in vitro . A YhjDR134C mutation suppresses the lethality of a G7662 "kdsD" EG10973 "gutQ" double null mutation which impairs (KDO)2-lipidA biosynthesis; this mutation also suppresses the lethal waaA null mutation which impairs the attachment of KDO to lipid IVA . The YhjDR134C mutation makes MsbA dispensable for transport of lipid IVA across the inner membrane . yhjD is a RpoS-dependent gene . Expression of yhjD was reduced by Lrp . Expression of yhjD is induced by treatment with acivicin . In the Transporter Classification Database, YhjD is a member of the putative lipid IV exporter family . yhjD and yihY are paralogous .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37642|protein.P37642]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhjD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011505,ECOCYC:EG12248,GeneID:948033`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3673362-3674375:+; feature_type=gene
