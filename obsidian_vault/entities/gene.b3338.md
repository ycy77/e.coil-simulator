---
entity_id: "gene.b3338"
entity_type: "gene"
name: "chiA"
source_database: "NCBI RefSeq"
source_id: "gene-b3338"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3338"
  - "chiA"
---

# chiA

`gene.b3338`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3338`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chiA (gene.b3338) is a gene entity. It encodes chiA (protein.P13656). Encoded protein function: FUNCTION: Bifunctional enzyme with lysozyme/chitinase activity. {ECO:0000269|PubMed:10760150}. EcoCyc product frame: EG11237-MONOMER. EcoCyc synonyms: yheB. Genomic coordinates: 3467160-3469853. EcoCyc protein note: ChiA is a large soluble protein with five predicted chitin-binding domains and a C-terminal catalytic domain that is similar to the family 18 glycohydrolases . The purified N-terminal chitin-binding domain binds to chitin with high affinity, but binds only poorly to cellulose . Purified ChiA exhibits endochitinase activity, releasing diacetyl-chitobiose and triacetyl-chitotriose from colloidal chitin . Under standard growth conditions, chiA expression is low and is negatively controlled by H-NS . In mutants lacking H-NS, expression of the gsp locus is derepressed, and a type II secretion machinery can be produced. This allows secretion of ChiA into the culture medium . Expression of chiA is activated by BglJ-RcsB, which may function as an H-NS antagonist . Artificially induced expression of chiA enables growth on pentaacetyl-chitopentaose . ChiA: "chitinase" Review:

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13656|protein.P13656]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=chiA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=chiA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010909,ECOCYC:EG11237,GeneID:947837`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3467160-3469853:-; feature_type=gene
