---
entity_id: "gene.b0334"
entity_type: "gene"
name: "prpD"
source_database: "NCBI RefSeq"
source_id: "gene-b0334"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0334"
  - "prpD"
---

# prpD

`gene.b0334`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0334`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prpD (gene.b0334) is a gene entity. It encodes prpD (protein.P77243). Encoded protein function: FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the dehydration of 2-methylcitrate (2-MC) to yield the cis isomer of 2-methyl-aconitate. It is also able to catalyze the dehydration of citrate and the hydration of cis-aconitate at a lower rate. Due to its broad substrate specificity, it seems to be responsible for the residual aconitase activity of the acnAB-null mutant. {ECO:0000269|PubMed:11782506, ECO:0000269|PubMed:12473114}. EcoCyc product frame: G6199-MONOMER. EcoCyc synonyms: yahT, acnC. Genomic coordinates: 351215-352666. EcoCyc protein note: 2-Methylcitrate dehydratase (PrpD) catalyzes the stereospecific dehydration of 2-methylcitrate, a reaction in propionate catabolism via the methylcitrate cycle . PrpD is monomeric in solution . Reports disagree on whether or not PrpD contains an iron-sulfur cluster, and on the substrate specificity of the enzyme . prpD also encodes the residual aconitase-like activity, aconitase C , which constitutes 5% or less of cellular aconitase activity and is observed in an acnA acnB double mutant...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77243|protein.P77243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=prpD; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=prpD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001152,ECOCYC:G6199,GeneID:945931`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:351215-352666:+; feature_type=gene
