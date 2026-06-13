---
entity_id: "gene.b3460"
entity_type: "gene"
name: "livJ"
source_database: "NCBI RefSeq"
source_id: "gene-b3460"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3460"
  - "livJ"
---

# livJ

`gene.b3460`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3460`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livJ (gene.b3460) is a gene entity. It encodes livJ (protein.P0AD96). Encoded protein function: FUNCTION: This protein is a component of the leucine, isoleucine, valine, (threonine) transport system, which is one of the two periplasmic binding protein-dependent transport systems of the high-affinity transport of the branched-chain amino acids. EcoCyc product frame: LIVJ-MONOMER. EcoCyc synonyms: hrbD, hrbC, hrbB. Genomic coordinates: 3598555-3599658. EcoCyc protein note: LivJ is the periplasmic binding protein of the LIV-I (LivJHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12 . Early studies suggested that LIV-I served as the entry point for the branched amino acids L-leucine, L-isoleucine, and L-valine and possibly L-alanine, L-threonine and L-serine . The LIV-I system is also able to transport phenylanine and plays a physiologically relevant role in phenylalanine accumulation . LivJ is synthesized as a precursor; a 23 amino acid signal sequence is cleaved upon export to the periplasm . Purified LivJ* binds L-leucine (KD = 0.4 µM), L-isoleucine KD = 0.4 µM) and L-valine (KD = 0.7 µM) (LivJ* denotes a protein that has been engineered with a StyI restriction site added at codon 124). Crystal structures indicate that the protein consists of two globular domains connected by a 3-stranded hinge .

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD96|protein.P0AD96]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livJ; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011299,ECOCYC:EG10539,GeneID:947971`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3598555-3599658:-; feature_type=gene
