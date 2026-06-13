---
entity_id: "gene.b2253"
entity_type: "gene"
name: "arnB"
source_database: "NCBI RefSeq"
source_id: "gene-b2253"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2253"
  - "arnB"
---

# arnB

`gene.b2253`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2253`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnB (gene.b2253) is a gene entity. It encodes arnB (protein.P77690). Encoded protein function: FUNCTION: Catalyzes the conversion of UDP-4-keto-arabinose (UDP-Ara4O) to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:12704196}. EcoCyc product frame: G7166-MONOMER. EcoCyc synonyms: pmrH, yfbE. Genomic coordinates: 2365910-2367067. EcoCyc protein note: ArnB is a UDP-L-Ara4O C-4" transaminase that acts in a pathway which modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), causing increased resistance to polymyxin . Structural and biochemical characterization of Salmonella typhimurium ArnB has been performed; crystal structures of the enzyme are presented and discussed with respect to catalysis . Expression of arnB is induced by the presence of FeSO4 (which primarily yields oxidized ferric iron in solution); the effect is dependent on the presence of the BasS-BasR two-component system . Fe(III) promotes transcription of the BasR activated arn operon and polymyxin resistance in E. coli K-12 . Chromosomal expression of the Salmonella typhimurium pmrD gene enables E...

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77690|protein.P77690]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007456,ECOCYC:G7166,GeneID:947375`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2365910-2367067:+; feature_type=gene
