---
entity_id: "gene.b3011"
entity_type: "gene"
name: "yqhD"
source_database: "NCBI RefSeq"
source_id: "gene-b3011"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3011"
  - "yqhD"
---

# yqhD

`gene.b3011`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3011`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqhD (gene.b3011) is a gene entity. It encodes yqhD (protein.Q46856). Encoded protein function: FUNCTION: Exhibits NADPH-dependent reductase activity for a broad range of short-chain aldehydes (PubMed:18211903, PubMed:19429550, PubMed:19609521, PubMed:20543070). Shows highest catalytic efficiency toward butanal, propanal and the highly toxic aldehydes acrolein and malondialdehyde (MDA), which are produced mainly during lipid peroxidation (PubMed:18211903, PubMed:20543070). Mediates resistance to reactive oxygen species (ROS) elicitors, such as paraquat and potassium tellurite, probably by protecting the cell against the toxic effects of reactive aldehydes derived from membrane lipid peroxidation (PubMed:18211903). Also acts, with lower efficiency, on acetaldehyde, glyceraldehyde, glycolaldehyde, methylglyoxal, glyoxal and hydroxyacetone (PubMed:18211903, PubMed:19609521, PubMed:20543070). Could be involved in glyoxal metabolism, by catalyzing the reduction of glyoxal to glycolaldehyde, and further to 1,2-ethandiol (PubMed:20543070). Catalyzes the reduction of isobutyraldehyde (2-methylpropanal) to isobutanol, and probably contributes to the production of isobutanol (PubMed:19609521). Can probably catalyze the reduction of glutaraldehyde, a widely used biocide, to 1,5-pentanediol, which is non-toxic (PubMed:34248896)...

## Biological Role

Activated by rpoD (protein.P00579), fur (protein.P0A9A9), yqhC (protein.Q46855).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46856|protein.Q46856]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yqhD; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yqhD; function=+
- `activates` <-- [[protein.Q46855|protein.Q46855]] `RegulonDB` `S` - regulator=YqhC; target=yqhD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009888,ECOCYC:G7564,GeneID:947493`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3155355-3156518:+; feature_type=gene
