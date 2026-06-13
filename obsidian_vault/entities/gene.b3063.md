---
entity_id: "gene.b3063"
entity_type: "gene"
name: "ttdT"
source_database: "NCBI RefSeq"
source_id: "gene-b3063"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3063"
  - "ttdT"
---

# ttdT

`gene.b3063`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3063`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ttdT (gene.b3063) is a gene entity. It encodes ttdT (protein.P39414). Encoded protein function: FUNCTION: Catalyzes the uptake of tartrate in exchange for intracellular succinate. Essential for anaerobic L-tartrate fermentation. {ECO:0000269|PubMed:17172328}. EcoCyc product frame: YGJE-MONOMER. EcoCyc synonyms: ygjC, ygjE. Genomic coordinates: 3208024-3209487. EcoCyc protein note: TtdT is a putative tartrate/succinate antiporter belonging to the DASS family of di- and tri-carboxylic acid transporters. ttdT is located in a probable operon with the ttdAB genes encoding L-tartrate dehydratase. In an analogous manner to CitT , under anaerobic conditions TtdT allows the uptake of L-tartrate in exchange for succinate, the end product of tartrate fermentation. In strains lacking anaerobic C4-dicarboxylate antiporters and CitT, TtdT is required for tartrate fermentation as tartrate uptake in ttdT mutants is normal, but tartrate/succinate antiport does not occur . Tartrate is taken up in ttdT mutants by some other mechanism, possibly YeaV or YfaV . ttdABT transcription is controlled by YgiP, a LysR-type transcriptional regulator; tartrate-dependent induction of the ttdABT operon requires YgiP .

## Biological Role

Activated by ttdR (protein.P45463).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39414|protein.P39414]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P45463|protein.P45463]] `RegulonDB` `S` - regulator=Dan; target=ttdT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010056,ECOCYC:EG12393,GeneID:947576`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3208024-3209487:+; feature_type=gene
