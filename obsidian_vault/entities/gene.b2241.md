---
entity_id: "gene.b2241"
entity_type: "gene"
name: "glpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2241"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2241"
  - "glpA"
---

# glpA

`gene.b2241`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2241`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpA (gene.b2241) is a gene entity. It encodes glpA (protein.P0A9C0). Encoded protein function: FUNCTION: Conversion of glycerol 3-phosphate to dihydroxyacetone. Uses fumarate or nitrate as electron acceptor. EcoCyc product frame: ANGLYC3PDEHYDROGSUBUNITA-MONOMER. Genomic coordinates: 2352647-2354275. EcoCyc protein note: GlpA is the large subunit of a three subunit glycerol-3-phosphate dehydrogenase complex. In anaerobic conditions this respiratory enzyme converts glycerol-3-phosphate to dihydroxyacetone phosphate (DHAP) using fumarate as a terminal electron acceptor. The GlpA subunit contains noncovalently bound FAD. .

## Biological Role

Repressed by glpR (protein.P0ACL0), plaR (protein.P37671). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9C0|protein.P0A9C0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpA; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `C` - regulator=GlpR; target=glpA; function=-
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB|EcoCyc` `C` - regulator=PlaR; target=glpA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007422,ECOCYC:EG10391,GeneID:946713`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2352647-2354275:+; feature_type=gene
