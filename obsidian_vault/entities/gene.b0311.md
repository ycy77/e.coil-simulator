---
entity_id: "gene.b0311"
entity_type: "gene"
name: "betA"
source_database: "NCBI RefSeq"
source_id: "gene-b0311"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0311"
  - "betA"
---

# betA

`gene.b0311`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0311`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

betA (gene.b0311) is a gene entity. It encodes betA (protein.P17444). Encoded protein function: FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the oxidation of choline to betaine aldehyde and betaine aldehyde to glycine betaine at the same rate. {ECO:0000255|HAMAP-Rule:MF_00750, ECO:0000269|PubMed:3512525, ECO:0000269|PubMed:3512526}. EcoCyc product frame: CHD-MONOMER. Genomic coordinates: 325577-327247. EcoCyc protein note: Choline dehydrogenase (CHD) catalyzes the first step in the biosynthesis of the osmoprotectant glycine betaine from choline. CHD is associated with the membrane, is electron transfer-linked and oxygen dependent . Based on sequence similarity, BetA was predicted to be a hydroxynitrile lyase . A betA mutant does not grow at high osmotic strength in the presence of choline, but is able to grow when the media is supplemented with glycine betaine . Expression of the bet operon is regulated by oxygen, choline, osmotic stress, and temperature . High-purity CHD proteins were obtained with the copolymer styrene maleic acid (SMA) and with the sugar surfactant n-Dodecyl-β-d-Maltopyranoside (DDM). Structural and enzymatic analysis found the CHD formed a trimer and could oxidize choline to betaine aldehyde but not further to betaine. Mutant analysis found H473 to play a critical role in the catalytic activity of CHD...

## Biological Role

Repressed by arcA (protein.P0A9Q1), betI (protein.P17446).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17444|protein.P17444]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=betA; function=-
- `represses` <-- [[protein.P17446|protein.P17446]] `RegulonDB` `C` - regulator=BetI; target=betA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001070,ECOCYC:EG10109,GeneID:945716`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:325577-327247:-; feature_type=gene
