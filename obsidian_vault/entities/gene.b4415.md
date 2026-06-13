---
entity_id: "gene.b4415"
entity_type: "gene"
name: "hokE"
source_database: "NCBI RefSeq"
source_id: "gene-b4415"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4415"
  - "hokE"
---

# hokE

`gene.b4415`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4415`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hokE (gene.b4415) is a gene entity. It encodes hokE (protein.P77091). Encoded protein function: FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system; if it expressed it could be neutralized by antisense antitoxin RNA SokE. {ECO:0000305|PubMed:10361310}. EcoCyc product frame: MONOMER0-1581. EcoCyc synonyms: ybdY. Genomic coordinates: 607836-607988. EcoCyc protein note: Sequence analysis indicates that the hokE gene is a homolog of the hok (host killing) gene which is responsible for mediating plasmid stabilization by post-segregational killing (PSK) in plasmid R1. hok encodes a stable mRNA whose translation is inhibited by a less stable mRNA encoded by sok. The stable mRNA encodes a toxic polypeptide. The hokE system is inactive probably due to insertion of the insertion element IS186 21 bp downstream of the hokE gene. Sequence analysis shows that after the removal of the IS186 element sequence, the hokE system contains regulatory elements described for the hok/sok system from plasmid R1, including a fold-back inhibition element (fbi), a translational activation element (tac), a promoter, an overlapping open reading frame named mokE, and an antisense RNA complementary to the hokE mRNA leader in the mokE reading frame...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77091|protein.P77091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0047279,ECOCYC:G0-9582,GeneID:2847715`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:607836-607988:+; feature_type=gene
