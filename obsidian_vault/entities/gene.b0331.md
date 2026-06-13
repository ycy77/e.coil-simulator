---
entity_id: "gene.b0331"
entity_type: "gene"
name: "prpB"
source_database: "NCBI RefSeq"
source_id: "gene-b0331"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0331"
  - "prpB"
---

# prpB

`gene.b0331`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0331`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prpB (gene.b0331) is a gene entity. It encodes prpB (protein.P77541). Encoded protein function: FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the thermodynamically favored C-C bond cleavage of (2R,3S)-2-methylisocitrate to yield pyruvate and succinate via an alpha-carboxy-carbanion intermediate. {ECO:0000255|HAMAP-Rule:MF_01939, ECO:0000269|PubMed:11422389, ECO:0000269|PubMed:15723538}. EcoCyc product frame: G6196-MONOMER. EcoCyc synonyms: yahQ. Genomic coordinates: 348682-349572. EcoCyc protein note: 2-Methylisocitrate lyase (PrpB) catalyzes the cleavage of 2-methylisocitrate to succinate and pyruvate, which is the final step in propionate metabolism via the methylcitrate cycle . The enzyme activity is sensitive to oxidation and is inactivated by 3-bromopyruvate alkylation . Crystal structures of the wild type and mutant enzyme in the apo- and product-bound forms have been solved . The structures enabled modeling of the active site and proposal of a catalytic mechanism involving an α-carboxy-carbanion transition state . Protein production is observed during growth on propionate, but not acetate or glucose . Expression of prpBCDE is regulated by PrpR and catabolite repression and is downregulated in the presence of a variety of sugars .

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

- `encodes` --> [[protein.P77541|protein.P77541]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=prpB; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=prpB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001138,ECOCYC:G6196,GeneID:944990`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:348682-349572:+; feature_type=gene
