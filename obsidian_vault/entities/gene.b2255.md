---
entity_id: "gene.b2255"
entity_type: "gene"
name: "arnA"
source_database: "NCBI RefSeq"
source_id: "gene-b2255"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2255"
  - "arnA"
---

# arnA

`gene.b2255`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2255`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

arnA (gene.b2255) is a gene entity. It encodes arnA (protein.P77398). Encoded protein function: FUNCTION: Bifunctional enzyme that catalyzes the oxidative decarboxylation of UDP-glucuronic acid (UDP-GlcUA) to UDP-4-keto-arabinose (UDP-Ara4O) and the addition of a formyl group to UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N) to form UDP-L-4-formamido-arabinose (UDP-L-Ara4FN). The modified arabinose is attached to lipid A and is required for resistance to polymyxin and cationic antimicrobial peptides. {ECO:0000269|PubMed:11706007, ECO:0000269|PubMed:15491143, ECO:0000269|PubMed:15695810, ECO:0000269|PubMed:15807526}. EcoCyc product frame: G7168-MONOMER. EcoCyc synonyms: SAF, yfbG, pmrI. Genomic coordinates: 2368039-2370021. EcoCyc protein note: ArnA is a bifunctional enzyme that acts within a pathway that modifies lipid A phosphates with 4-amino-4-deoxy-L-arabinose (L-Ara4N), which causes increased resistance to polymyxin . ArnA exhibits UDP-glucuronic acid (UDP-GlcA) C-4"-dehydrogenase and UDP-4-amino-4-deoxy-L-arabinose (UDP-L-Ara4N) formyltransferase activities in vitro . The two activities are separable, and both are required for polymyxin resistance . The N-terminal domain is similar to methionyl-tRNAfMet formyltransferase and catalyzes the N10-formyltetrahydrofolate-dependent formylation of the 4'' amine of UDP-L-Ara4N...

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77398|protein.P77398]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=arnA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007460,ECOCYC:G7168,GeneID:947683`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2368039-2370021:+; feature_type=gene
