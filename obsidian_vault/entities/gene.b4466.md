---
entity_id: "gene.b4466"
entity_type: "gene"
name: "yghJ"
source_database: "NCBI RefSeq"
source_id: "gene-b4466"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4466"
  - "yghJ"
---

# yghJ

`gene.b4466`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4466`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yghJ (gene.b4466) is a gene entity. It encodes yghJ (protein.P0CK95). Encoded protein function: FUNCTION: Involved in a type II secretion system (T2SS, formerly general secretion pathway, GSP) for the export of folded proteins across the outer membrane. {ECO:0000305}. EcoCyc product frame: G7541-MONOMER. EcoCyc synonyms: b2974, b2973, sslE. Genomic coordinates: 3114550-3119112. EcoCyc protein note: YghJ is a potentially amyloidogenic protein ; the metalloprotease domain (aa 1081-181) of YghJ (YghJM) contains 3 short amyloidogenic regions; purified YghJM forms detergent- and protease-resistant aggregates with fibrillar morphology; YghJM aggregates have amyloidogenic properties in vitro; YghJM forms amyloid-like fibrils in vivo . In pathogenic (and some commensal) E. coli strains, YghJ (renamed SslE) is a virulence factor secreted by a type II system (known as T2SSΒ); E. coli K-12 does not contain the full set of T2SSβ encoding genes - an examination of T2SSΒ encoding loci in various strains suggests that in K-12, the T2SSΒ - encoding operon experienced an internal deletion . YghJ is detected in in the whole-cell lysate of MG1655 but not in the secreted fraction . yghJ contains a predicted lipoprotein signal .

## Biological Role

Activated by pdeL (protein.P21514).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0CK95|protein.P0CK95]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=yghJ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0174096,ECOCYC:G7541,GeneID:2847716`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3114550-3119112:-; feature_type=gene
