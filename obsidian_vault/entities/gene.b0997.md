---
entity_id: "gene.b0997"
entity_type: "gene"
name: "torA"
source_database: "NCBI RefSeq"
source_id: "gene-b0997"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0997"
  - "torA"
---

# torA

`gene.b0997`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0997`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

torA (gene.b0997) is a gene entity. It encodes torA (protein.P33225). Encoded protein function: FUNCTION: Reduces trimethylamine-N-oxide (TMAO) into trimethylamine; an anaerobic reaction coupled to energy-yielding reactions. {ECO:0000269|PubMed:30945846, ECO:0000269|PubMed:39769096}. EcoCyc product frame: TORA-MONOMER. Genomic coordinates: 1059256-1061802. EcoCyc protein note: torA encodes an inducible trimethylamine N-oxide reductase. The enzyme functions as a terminal reductase during anaerobic respiration on TMAO - early work was done using E. coli K-10 . TorA contains the site of TMAO reduction and the CPD-15873 . The presence of the GMP nucleotides is crucial for the insertion of the cofactor into the apo enzyme . Purified TorA cannot reduce sulfoxides (including dimethylsulfoxide - DMSO) and has high specificity for the two N-oxides - TMAO and 4 methylmorpholine-N-oxide . There is some evidence that TorA can exist as both a dimer and a monomer . A 39 amino acid signal peptide is cleaved . Tor A receives electrons from the membrane bound cytochrome c menaquinol dehydrogenase TorC EG12195-MONOMER "TorD" is the dedicated chaperone of TorA; TorD is involved in the protection and maturation of TorA . torC, torA and torD form an operon which is regulated by the PWY0-1506 "TorTSR two component system"...

## Biological Role

Repressed by nac (protein.Q47005). Activated by torR (protein.P38684).

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33225|protein.P33225]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P38684|protein.P38684]] `RegulonDB` `S` - regulator=TorR; target=torA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=torA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003372,ECOCYC:EG11814,GeneID:946267`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1059256-1061802:+; feature_type=gene
