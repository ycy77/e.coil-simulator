---
entity_id: "gene.b0383"
entity_type: "gene"
name: "phoA"
source_database: "NCBI RefSeq"
source_id: "gene-b0383"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0383"
  - "phoA"
---

# phoA

`gene.b0383`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0383`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoA (gene.b0383) is a gene entity. It encodes phoA (protein.P00634). Encoded protein function: Alkaline phosphatase (APase) (EC 3.1.3.1) EcoCyc product frame: ALKAPHOSPHA-MONOMER. EcoCyc synonyms: psiA. Genomic coordinates: 401747-403162. EcoCyc protein note: Alkaline phosphatase is a periplasmic, homodimeric enzyme that catalyses the hydrolysis and transphosphorylation of a wide variety of phosphate monoesters . The reaction proceeds through a phosphoseryl intermediate with the subsequent release of inorganic phosphate and alcohol . The transphosphorylation reaction results in the transfer of a phosphoryl group to the alcohol of acceptors such as Tris or ethanolamine . Alkaline phosphatase is a metalloenzyme, binding two zinc atoms and one magnesium ion per monomer . The amount of alkaline phosphatase is optimal when cells are starved for phosphate - which is the most common environment for E. coli in the human gut - and is much reduced when there is an excess of phosphate . Under conditions of limiting phosphate, alkaline phosphatase accounts for approximately 6% of the total protein synthesized . Alkaline phosphatase occurs in three major forms designated isozymes 1, 2 and 3 whose relative proportions are dependent on the growth conditions...

## Biological Role

Activated by lrp (protein.P0ACJ0), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00634|protein.P00634]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=phoA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001328,ECOCYC:EG10727,GeneID:945041`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:401747-403162:+; feature_type=gene
