---
entity_id: "gene.b4042"
entity_type: "gene"
name: "dgkA"
source_database: "NCBI RefSeq"
source_id: "gene-b4042"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4042"
  - "dgkA"
---

# dgkA

`gene.b4042`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4042`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgkA (gene.b4042) is a gene entity. It encodes dgkA (protein.P0ABN1). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of sn-l,2-diacylglycerol (DAG) to phosphatidic acid (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:6277376, PubMed:6303781, PubMed:9305868). Involved in the recycling of diacylglycerol produced as a by-product during membrane-derived oligosaccharide (MDO) biosynthesis (PubMed:217867, PubMed:6305970). In vitro, phosphorylates various substrates, including sn-1,2-dioleoylglycerol, sn-1,2-dioctanoylglycerol, sn-1,2-dipalmitoylglycerol, sn-1,2-dipalmitate and ceramide (PubMed:218816, PubMed:2828054, PubMed:2984194, PubMed:3009449, PubMed:3021764). Catalyzes direct phosphoryl transfer from Mg-ATP to diacylglycerol and does not form an enzyme-phosphate intermediate (PubMed:9305868). {ECO:0000269|PubMed:217867, ECO:0000269|PubMed:218816, ECO:0000269|PubMed:2828054, ECO:0000269|PubMed:2984194, ECO:0000269|PubMed:3009449, ECO:0000269|PubMed:3021764, ECO:0000269|PubMed:6277376, ECO:0000269|PubMed:6303781, ECO:0000269|PubMed:6305970, ECO:0000269|PubMed:9305868}. EcoCyc product frame: DIACYLGLYKIN-MONOMER. Genomic coordinates: 4256637-4257005.

## Biological Role

Activated by basR (protein.P30843).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABN1|protein.P0ABN1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `C` - regulator=BasR; target=dgkA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013235,ECOCYC:EG10224,GeneID:948543`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4256637-4257005:+; feature_type=gene
