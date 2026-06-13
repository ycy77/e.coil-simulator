---
entity_id: "gene.b3812"
entity_type: "gene"
name: "yigB"
source_database: "NCBI RefSeq"
source_id: "gene-b3812"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3812"
  - "yigB"
---

# yigB

`gene.b3812`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3812`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yigB (gene.b3812) is a gene entity. It encodes yigB (protein.P0ADP0). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of 5-amino-6-(5-phospho-D-ribitylamino)uracil, and thus could be involved in the riboflavin biosynthesis pathway (PubMed:24123841). Is also able to dephosphorylate flavin mononucleotide (FMN) and other phosphoric acid esters (PubMed:16990279, PubMed:24123841). YigB is important for the formation of dormant persister cells (PubMed:18519731). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:24123841}. EcoCyc product frame: EG11202-MONOMER. Genomic coordinates: 3997183-3997899. EcoCyc protein note: The identity of the enzyme(s) catalyzing the dephosphorylation of CPD-1086 in the riboflavin biosynthesis pathway was long unknown . have now shown that at least two enzymes, YigB and YbjI, can catalyze this reaction. YigB was initially identified as an FMN phosphatase that belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . yigB is important for formation of dormant persister cells; overexpression of yigB leads to increased tolerance to ofloxacin . Deletion of yigB alone does not result in riboflavin auxotrophy .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADP0|protein.P0ADP0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yigB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012450,ECOCYC:EG11202,GeneID:948357`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3997183-3997899:+; feature_type=gene
