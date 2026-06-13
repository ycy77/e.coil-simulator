---
entity_id: "gene.b1348"
entity_type: "gene"
name: "ralR"
source_database: "NCBI RefSeq"
source_id: "gene-b1348"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1348"
  - "ralR"
---

# ralR

`gene.b1348`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1348`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ralR (gene.b1348) is a gene entity. It encodes ralR (protein.P33229). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system. Upon overexpression inhibits growth and reduces colony-forming units in both the presence and absence of the Rac prophage, cells become filamentous. Has deoxyribonuclease activity (probably endonucleolytic), does not digest RNA. Its toxic effects are neutralized by sRNA antitoxin RalA, which is encoded in trans on the opposite DNA strand (PubMed:24748661). Has RAL-like activity (PubMed:7476171). {ECO:0000269|PubMed:24748661, ECO:0000269|PubMed:7476171}. EcoCyc product frame: EG11900-MONOMER. EcoCyc synonyms: ydaB, lar. Genomic coordinates: 1413733-1413927. EcoCyc protein note: RalR (Lar) is the toxin of the RalRA type I toxin-antitoxin system. RalR is a non-specific DNA endonuclease that cleaves both methylated and unmethylated DNA. A RalR mutant with reduced toxicity also has lost endonuclease activity . Overexpression of RalR inhibits growth. In the presence of the small RNA RalA, the level of RalR protein expressed from a plasmid is decreased . Growth of a ΔralR or ΔralRA mutant is more severely inhibited by fosfomycin than wild type . ralR is part of the lambdoid prophage Rac...

## Biological Role

Repressed by ralA (gene.b4714).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33229|protein.P33229]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4714|gene.b4714]] `RegulonDB` `S` - regulator=RalA; target=ralR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004524,ECOCYC:EG11900,GeneID:945914`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1413733-1413927:-; feature_type=gene
