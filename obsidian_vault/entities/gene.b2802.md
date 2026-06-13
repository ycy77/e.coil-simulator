---
entity_id: "gene.b2802"
entity_type: "gene"
name: "fucI"
source_database: "NCBI RefSeq"
source_id: "gene-b2802"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2802"
  - "fucI"
---

# fucI

`gene.b2802`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2802`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fucI (gene.b2802) is a gene entity. It encodes fucI (protein.P69922). Encoded protein function: FUNCTION: Converts the aldose L-fucose into the corresponding ketose L-fuculose (PubMed:13319278, PubMed:4632320, PubMed:4928018, PubMed:8564401, PubMed:9367760). Also converts D-arabinose into D-ribulose (PubMed:13319278, PubMed:4632320, PubMed:4928018). In addition, catalyzes the isomerization of L-xylulose to L-xylose (PubMed:22133443). {ECO:0000269|PubMed:13319278, ECO:0000269|PubMed:22133443, ECO:0000269|PubMed:4632320, ECO:0000269|PubMed:4928018, ECO:0000269|PubMed:8564401, ECO:0000269|PubMed:9367760}. EcoCyc product frame: FUCISOM-MONOMER. Genomic coordinates: 2935584-2937359. EcoCyc protein note: FucI can function as both an L-fucose isomerase and a D-arabinose isomerase, the first enzymes of the L-fucose and D-arabinose degradation pathways, respectively. However, production of FucI is only induced by L-fucose . Between the two anomers of L-fucose,only the α-form adopts a position suitable for the ring opening reaction . A crystal structure of the enzyme has been solved at 2.5 Å resolution . An amber mutation has been generated .

## Biological Role

Activated by crp (protein.P0ACJ8), ygfI (protein.P52044).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69922|protein.P69922]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=fucI; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `C` - regulator=SrsR; target=fucI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009189,ECOCYC:EG10349,GeneID:946195`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2935584-2937359:+; feature_type=gene
