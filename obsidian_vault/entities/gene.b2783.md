---
entity_id: "gene.b2783"
entity_type: "gene"
name: "mazE"
source_database: "NCBI RefSeq"
source_id: "gene-b2783"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2783"
  - "mazE"
---

# mazE

`gene.b2783`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2783`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mazE (gene.b2783) is a gene entity. It encodes mazE (protein.P0AE72). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Labile antitoxin that binds to the MazF endoribonuclease toxin and neutralizes its endoribonuclease activity. Is considered to be an 'addiction' molecule as the cell dies in its absence. Toxicity results when the levels of MazE decrease in the cell, leading to mRNA degradation. This effect can be rescued by expression of MazE, but after 6 hours in rich medium the overexpression of MazF leads to programmed cell death. Cell growth and viability are not affected when MazF and MazE are coexpressed. Both MazE and MazE-MazF bind to the promoter region of the mazE-mazF operon to inhibit their own transcription (PubMed:8650219). There are 3 operators to which MazE binds (PubMed:12533537). MazE has higher affinity for promoter DNA in the presence of MazF (PubMed:25564525). {ECO:0000269|PubMed:11071896, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:12533537, ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:21419338, ECO:0000269|PubMed:25564525, ECO:0000269|PubMed:8650219}.; FUNCTION: Cell death governed by the MazE-MazF and DinJ-YafQ TA systems seems to play a role in biofilm formation, while MazE-MazF is also implicated in cell death in liquid media. {ECO:0000269|PubMed:15576778, ECO:0000269|PubMed:19707553}...

## Biological Role

Repressed by mazE (protein.P0AE72), hipB (protein.P23873). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE72|protein.P0AE72]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=mazE; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=mazE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=mazE; function=+
- `represses` <-- [[protein.P0AE72|protein.P0AE72]] `RegulonDB` `S` - regulator=MazE; target=mazE; function=-
- `represses` <-- [[protein.P23873|protein.P23873]] `RegulonDB` `S` - regulator=HipB; target=mazE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009122,ECOCYC:EG10571,GeneID:947245`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2911091-2911339:-; feature_type=gene
