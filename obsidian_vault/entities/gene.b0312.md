---
entity_id: "gene.b0312"
entity_type: "gene"
name: "betB"
source_database: "NCBI RefSeq"
source_id: "gene-b0312"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0312"
  - "betB"
---

# betB

`gene.b0312`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0312`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

betB (gene.b0312) is a gene entity. It encodes betB (protein.P17445). Encoded protein function: FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the irreversible oxidation of betaine aldehyde to the corresponding acid. It is highly specific for betaine and has a significantly higher affinity for NAD than for NADP. {ECO:0000255|HAMAP-Rule:MF_00804, ECO:0000269|PubMed:2194570, ECO:0000269|PubMed:3512525}. EcoCyc product frame: BADH-MONOMER. Genomic coordinates: 327261-328733. EcoCyc protein note: Betaine aldehyde dehydrogenase (BADH) catalyzes the second step in the biosynthesis of the osmoprotectant glycine betaine from choline . Expression of the bet operon is regulated by oxygen, choline, osmotic stress, and temperature . Inactivation of six genes encoding aldehyde dehydrogenases (EG12292, EG10036, EG10110, G6755, G7961, and EG11329) resulted in a strain with greatly reduced aromatic aldehyde oxidation activity (the strain was named ROAR for reduced oxidation and reduction of aromatic aldehydes) . BetB: "betaine"

## Biological Role

Repressed by betI (protein.P17446).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17445|protein.P17445]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P17446|protein.P17446]] `RegulonDB` `C` - regulator=BetI; target=betB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001072,ECOCYC:EG10110,GeneID:947376`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:327261-328733:-; feature_type=gene
