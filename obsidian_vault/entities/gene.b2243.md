---
entity_id: "gene.b2243"
entity_type: "gene"
name: "glpC"
source_database: "NCBI RefSeq"
source_id: "gene-b2243"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2243"
  - "glpC"
---

# glpC

`gene.b2243`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2243`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpC (gene.b2243) is a gene entity. It encodes glpC (protein.P0A996). Encoded protein function: FUNCTION: Electron transfer protein; may also function as the membrane anchor for the GlpAB dimer. EcoCyc product frame: ANGLYC3PDEHYDROGSUBUNITC-MONOMER. Genomic coordinates: 2355521-2356711. EcoCyc protein note: GlpC is the membrane associated subunit of the heterotrimeric glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate a a terminal electron acceptor. Overexpressed GlpC associates with the inner membrane . GlpC contains two cysteine clusters typical of iron-sulfur binding domains . uses the name GlpB for the protein encoded by the third gene in the glp operon.

## Biological Role

Repressed by glpR (protein.P0ACL0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A996|protein.P0A996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpC; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `C` - regulator=GlpR; target=glpC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007426,ECOCYC:EG10393,GeneID:946735`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2355521-2356711:+; feature_type=gene
