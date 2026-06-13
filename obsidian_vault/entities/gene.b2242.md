---
entity_id: "gene.b2242"
entity_type: "gene"
name: "glpB"
source_database: "NCBI RefSeq"
source_id: "gene-b2242"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2242"
  - "glpB"
---

# glpB

`gene.b2242`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2242`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpB (gene.b2242) is a gene entity. It encodes glpB (protein.P13033). Encoded protein function: FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses fumarate or nitrate as electron acceptor. EcoCyc product frame: ANGLYC3PDEHYDROGSUBUNITB-MONOMER. EcoCyc synonyms: psi-51. Genomic coordinates: 2354265-2355524. EcoCyc protein note: glpB encodes a subunit of the heterotrimeric glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate as a terminal electron acceptor. GlpB contains a predicted flavin mononucleotide-binding domain glpB was among the genes induced during phosphate starvation .

## Biological Role

Repressed by glpR (protein.P0ACL0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13033|protein.P13033]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpB; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `C` - regulator=GlpR; target=glpB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007424,ECOCYC:EG10392,GeneID:946733`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2354265-2355524:+; feature_type=gene
