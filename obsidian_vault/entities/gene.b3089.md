---
entity_id: "gene.b3089"
entity_type: "gene"
name: "sstT"
source_database: "NCBI RefSeq"
source_id: "gene-b3089"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3089"
  - "sstT"
---

# sstT

`gene.b3089`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3089`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sstT (gene.b3089) is a gene entity. It encodes sstT (protein.P0AGE4). Encoded protein function: FUNCTION: Involved in the import of serine and threonine into the cell, with the concomitant import of sodium (symport system). {ECO:0000255|HAMAP-Rule:MF_01582, ECO:0000269|PubMed:12097162, ECO:0000269|PubMed:9852024}. EcoCyc product frame: YGJU-MONOMER. EcoCyc synonyms: ygjU. Genomic coordinates: 3239944-3241188. EcoCyc protein note: Early studies characterized a Na+-dependent serine-threonine transport system in the K-12 derived E. coli strain W3133-2 . Purified His-tagged SstT, reconstituted into liposomes mediates serine uptake which is dependent on an inwardly directed Na+ gradient and membrane potential . Serine transport in reconstituted proteoliposomes is inhibited by L-threonine, but not by other amino acids . In the Transporter Classification Database SstT is a member of the Dicarboxylate/Amino Acid:Cation Symporter (DAACS) Family.

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), arcA (protein.P0A9Q1), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGE4|protein.P0AGE4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=sstT; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=sstT; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010159,ECOCYC:EG12732,GeneID:947605`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3239944-3241188:+; feature_type=gene
