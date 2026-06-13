---
entity_id: "gene.b1396"
entity_type: "gene"
name: "paaI"
source_database: "NCBI RefSeq"
source_id: "gene-b1396"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1396"
  - "paaI"
---

# paaI

`gene.b1396`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1396`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

paaI (gene.b1396) is a gene entity. It encodes paaI (protein.P76084). Encoded protein function: FUNCTION: Thioesterase with a preference for ring-hydroxylated phenylacetyl-CoA esters. Hydrolyzes 3,4-dihydroxyphenylacetyl-CoA, 3-hydroxyphenylacetyl-CoA and 4-hydroxyphenylacetyl-CoA. Inactive towards 4-hydroxybenzoyl-CoA and 4-hydroxyphenacyl-CoA. {ECO:0000269|PubMed:16464851, ECO:0000269|PubMed:9748275}. EcoCyc product frame: G6717-MONOMER. EcoCyc synonyms: ydbV. Genomic coordinates: 1460471-1460893. EcoCyc protein note: PaaI belongs to the acyl-CoA thioesterase subfamily of the hotdog-fold superfamily of enzymes . Among the relevant phenylacetate degradation pathway intermediates, its primary substrate appears to be phenylacetyl-CoA , although it was previously thought that its preferred substrates were ring-hydroxylated phenylacetyl-CoA thioesters . It may be involved in detoxification or salvage reactions for breakdown products of the unstable early intermediates of the phenylacetate degradation pathway . A crystal structure of PaaI has been solved at 2 Å resolution . A paaI mutant does not exhibit a defect in utilization of phenylacetate as a source of carbon . PaaI activity is increased in cells grown on phenylacetate . PaaI: "phenylacetic acid degradation"

## Biological Role

Repressed by paaX (protein.P76086). Activated by rpoD (protein.P00579), slyA (protein.P0A8W2), crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76084|protein.P76084]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=paaI; function=+
- `activates` <-- [[protein.P0A8W2|protein.P0A8W2]] `RegulonDB` `S` - regulator=SlyA; target=paaI; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=paaI; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=paaI; function=+
- `represses` <-- [[protein.P76086|protein.P76086]] `RegulonDB` `C` - regulator=PaaX; target=paaI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004666,ECOCYC:G6717,GeneID:945265`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1460471-1460893:+; feature_type=gene
