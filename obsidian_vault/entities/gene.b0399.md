---
entity_id: "gene.b0399"
entity_type: "gene"
name: "phoB"
source_database: "NCBI RefSeq"
source_id: "gene-b0399"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0399"
  - "phoB"
---

# phoB

`gene.b0399`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0399`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoB (gene.b0399) is a gene entity. It encodes phoB (protein.P0AFJ5). Encoded protein function: FUNCTION: This protein is a positive regulator for the phosphate regulon. Transcription of this operon is positively regulated by PhoB and PhoR when phosphate is limited. EcoCyc product frame: PHOSPHO-PHOB. EcoCyc synonyms: phoRc, phoT. Genomic coordinates: 417142-417831. EcoCyc protein note: PhoB is a dual transcription regulator that activates expression of the Pho regulon in response to environmental Pi. The Pho regulon includes operons and genes whose products are involved in phosphorus uptake and metabolism . Expression of the periplasmic binding proteins for peptide transport, OppA and DppA, is repressed by PhoB . In a proteomic analysis under phosphate-limiting conditions, it was found that up to 400 proteins are differentially expressed . PhoB is also involved in bacterial virulence of pathogenic Escherichia coli . PhoB also regulates genes involved in the stimulation of cell persister resuscitation . Inhibition of phoB expression by CRISPRi enhanced cellular fitness under treatment with the antibiotic pyocyanin . PhoB is a response regulator and belongs to the two-component system PhoR/PhoB. Under phosphate-limited conditions, the inner membrane sensor kinase PhoR autophosphorylates. Subsequent transfer of the phosphate group to PhoB results in activation of PhoB...

## Biological Role

Repressed by nac (protein.Q47005). Activated by phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFJ5|protein.P0AFJ5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=phoB; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=phoB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001389,ECOCYC:EG10728,GeneID:945046`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:417142-417831:+; feature_type=gene
