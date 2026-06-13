---
entity_id: "gene.b2254"
entity_type: "gene"
name: "arnC"
source_database: "NCBI RefSeq"
source_id: "gene-b2254"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2254"
  - "arnC"
---

# arnC

`gene.b2254`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2254`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnC (gene.b2254) is a gene entity. It encodes arnC (protein.P77757). Encoded protein function: FUNCTION: Catalyzes the transfer of 4-deoxy-4-formamido-L-arabinose from UDP to undecaprenyl phosphate. The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007}. EcoCyc product frame: G7167-MONOMER. EcoCyc synonyms: pmrF, yfbF. Genomic coordinates: 2367071-2368039. EcoCyc protein note: ArnC is an undecaprenyl transferase that acts in a pathway which modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), causing increased resistance to polymyxin . ArnC is an inner membrane protein with two predicted transmembrane domains; the C terminus is located in the cytoplasm . ArnC selectively converts uridine 5'-diphospho-β-(4-deoxy-4-formamido-L-arabinose) (UDP-L-Ara4FN), but not uridine 5'-diphospho-β-(4-amino-4-deoxy-L-arabinose) (UDP-L-Ara4N), to lipid product . ArnC: "L-Ara4N (4-amino-4-deoxy-L-arabinose) biosynthesis" PmrF: "polymyxin resistance" Review:

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77757|protein.P77757]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007458,ECOCYC:G7167,GeneID:945275`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2367071-2368039:+; feature_type=gene
