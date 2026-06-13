---
entity_id: "gene.b2744"
entity_type: "gene"
name: "umpG"
source_database: "NCBI RefSeq"
source_id: "gene-b2744"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2744"
  - "umpG"
---

# umpG

`gene.b2744`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2744`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

umpG (gene.b2744) is a gene entity. It encodes surE (protein.P0A840). Encoded protein function: FUNCTION: Nucleotidase with a broad substrate specificity as it can dephosphorylate various ribo- and deoxyribonucleoside 5'-monophosphates and ribonucleoside 3'-monophosphates with highest affinity to 3'-AMP (PubMed:15489502). Also hydrolyzes polyphosphate (exopolyphosphatase activity) with the preference for short-chain-length substrates (P20-25) (PubMed:15489502). Might be involved in the regulation of dNTP and NTP pools, and in the turnover of 3'-mononucleotides produced by numerous intracellular RNases (T1, T2, and F) during the degradation of various RNAs (PubMed:15489502). Also plays a significant physiological role in stress-response and is required for the survival of E.coli in stationary growth phase (PubMed:15489502). {ECO:0000269|PubMed:15489502, ECO:0000303|PubMed:15489502}. EcoCyc product frame: EG11817-MONOMER. EcoCyc synonyms: ygbC, surE. Genomic coordinates: 2869513-2870274. EcoCyc protein note: UmpG (SurE) is a phosphatase with broad substrate specificity. It efficiently hydrolyzes purine and pyrimidine ribonucleotides and deoxyribonucleotides, and polyphosphate. UmpG and its homologs are widely distributed among bacteria, archaea and eukaryotes . The enzyme was found to participate in the degradation of "overflow" UMP nucleotides...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A840|protein.P0A840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=umpG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009008,ECOCYC:EG11817,GeneID:947211`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2869513-2870274:-; feature_type=gene
