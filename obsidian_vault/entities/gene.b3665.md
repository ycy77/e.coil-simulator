---
entity_id: "gene.b3665"
entity_type: "gene"
name: "adeD"
source_database: "NCBI RefSeq"
source_id: "gene-b3665"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3665"
  - "adeD"
---

# adeD

`gene.b3665`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3665`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adeD (gene.b3665) is a gene entity. It encodes ade (protein.P31441). Encoded protein function: Adenine deaminase (Adenase) (Adenine aminase) (EC 3.5.4.2) EcoCyc product frame: EG11692-MONOMER. EcoCyc synonyms: adu, yicP, ade. Genomic coordinates: 3843964-3845730. EcoCyc protein note: AdeD is a substrate-specific adenine deaminase . In wild-type cells, levels of adenine deaminase are too low to satisfy the cellular purine requirement . Two metal ions per subunit are required for optimal adenine deaminase activity , and either Mn2+ or Fe2+ can satisfy this metal requirement . The catalytically active Fe/Fe enzyme contains two high-spin ferrous iron ions. Site-directed mutagenesis of His92, His214, His235 and Glu185 result in loss of catalytic activity and metal binding, and certain mutations in His90 result in loss of metal binding . A reaction mechanism has been proposed . Ferrous iron-containing enzyme also has catalase activity; exposure to hydrogen peroxide eventually damages the enzyme by oxygenation of various amino acid residues, and its adenine deaminase activity is concurrently lost. Superoxide formation can also be measured . AdeD expression appears to be induced by the presence of high amounts of adenine in the culture medium . Transcription of ade can be activated by various promoter mutations and is repressed more than 10-fold by the H-NS protein in wild type...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31441|protein.P31441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=adeD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011979,ECOCYC:EG11692,GeneID:948210`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3843964-3845730:+; feature_type=gene
