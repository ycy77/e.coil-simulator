---
entity_id: "gene.b4055"
entity_type: "gene"
name: "aphA"
source_database: "NCBI RefSeq"
source_id: "gene-b4055"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4055"
  - "aphA"
---

# aphA

`gene.b4055`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4055`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aphA (gene.b4055) is a gene entity. It encodes aphA (protein.P0AE22). Encoded protein function: FUNCTION: Dephosphorylates several organic phosphate monoesters including 3'- and 5'-nucleotides, 2'-deoxy-5'-nucleotides, pNPP, phenyl phosphate, glycerol 2-phosphate, ribose 5-phosphate, O-phospho-L-amino acids and phytic acid, showing the highest activity with aryl phosphoesters (pNPP, phenyl phosphate and O-phospho-L-tyrosine), and to a lesser extent with 3'- and 5'-nucleotides. No activity toward ATP, phosphodiesters, glycerol-1-phosphate, glucose 1-phosphate, glucose 6-phosphate, NADP, GTP or 3',5'-cAMP, ADP or ATP. Also has a phosphotransferase activity catalyzing the transfer of low-energy phosphate groups from organic phosphate monoesters to free hydroxyl groups of various organic compounds. Capable of transferring phosphate from either pNPP or UMP to adenosine or uridine. Does not exhibit nucleotide phosphomutase activity. {ECO:0000269|PubMed:16297670, ECO:0000269|PubMed:9011040}. EcoCyc product frame: APHA-MONOMER. EcoCyc synonyms: yjbP, hobH. Genomic coordinates: 4269414-4270127. EcoCyc protein note: aphA encodes a periplasmic phosphatase/phosphotransferase that has optimal activity at acidic pH...

## Biological Role

Repressed by DNA-binding transcriptional repressor CytR (complex.ecocyc.CPLX0-7740), lrp (protein.P0ACJ0). Activated by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AE22|protein.P0AE22]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7740|complex.ecocyc.CPLX0-7740]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013283,ECOCYC:EG11934,GeneID:948562`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4269414-4270127:+; feature_type=gene
