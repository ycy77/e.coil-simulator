---
entity_id: "gene.b4358"
entity_type: "gene"
name: "lgoD"
source_database: "NCBI RefSeq"
source_id: "gene-b4358"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4358"
  - "lgoD"
---

# lgoD

`gene.b4358`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4358`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lgoD (gene.b4358) is a gene entity. It encodes lgoD (protein.P39400). Encoded protein function: FUNCTION: Catalyzes the oxidation of L-galactonate to D-tagaturonate. Required for growth on L-galactonate as the sole carbon source. In vitro, can also use L-gulonate. {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:24861318}. EcoCyc product frame: G7945-MONOMER. EcoCyc synonyms: yjjN. Genomic coordinates: 4595990-4597012. EcoCyc protein note: LgoD is an L-galactonate oxidoreductase that is required for growth on L-galactonate as the sole carbon source under high-throughput growth conditions with limited aeration . LgoD did not show dehydrogenase activity in a high-throughput screen of purified proteins; however, L-galactonate was not tested as a substrate . LgoD may be the L-galactonate oxidoreductase involved in the degradation of L-galactonate that was described in . Expression of lgoD is increased during growth on L-galactonate compared to growth on L-lactate . UxuR appears to regulate lgoD expression .

## Biological Role

Repressed by exuR (protein.P0ACL2), uxuR (protein.P39161).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39400|protein.P39400]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACL2|protein.P0ACL2]] `RegulonDB` `S` - regulator=ExuR; target=lgoD; function=-
- `represses` <-- [[protein.P39161|protein.P39161]] `RegulonDB` `S` - regulator=UxuR; target=lgoD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014294,ECOCYC:G7945,GeneID:948883`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4595990-4597012:+; feature_type=gene
