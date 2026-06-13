---
entity_id: "gene.b1858"
entity_type: "gene"
name: "znuC"
source_database: "NCBI RefSeq"
source_id: "gene-b1858"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1858"
  - "znuC"
---

# znuC

`gene.b1858`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1858`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

znuC (gene.b1858) is a gene entity. It encodes znuC (protein.P0A9X1). Encoded protein function: FUNCTION: Part of the ABC transporter complex ZnuABC involved in zinc import. Responsible for energy coupling to the transport system. {ECO:0000255|HAMAP-Rule:MF_01725, ECO:0000269|PubMed:9680209}. EcoCyc product frame: ZNUC-MONOMER. EcoCyc synonyms: yebM. Genomic coordinates: 1942662-1943417. EcoCyc protein note: znuC encodes the predicted ATP-binding subunit of a high-affinity zinc uptake system ; ZnuC contains sequence motifs conserved in ATP-binding cassette proteins . znuC belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . znu: Zn2+ uptake

## Biological Role

Repressed by zur (protein.P0AC51). Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9X1|protein.P0A9X1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=znuC; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=znuC; function=+
- `represses` <-- [[protein.P0AC51|protein.P0AC51]] `RegulonDB` `S` - regulator=Zur; target=znuC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006198,ECOCYC:G7018,GeneID:946374`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1942662-1943417:+; feature_type=gene
