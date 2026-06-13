---
entity_id: "gene.b2240"
entity_type: "gene"
name: "glpT"
source_database: "NCBI RefSeq"
source_id: "gene-b2240"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2240"
  - "glpT"
---

# glpT

`gene.b2240`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2240`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpT (gene.b2240) is a gene entity. It encodes glpT (protein.P08194). Encoded protein function: FUNCTION: Responsible for glycerol-3-phosphate uptake. EcoCyc product frame: GLPT-MONOMER. Genomic coordinates: 2351016-2352374. EcoCyc protein note: GlpT is the major E. coli uptake system for sn-glycerol 3-phosphate, and this transporter belongs to the Major Facilitator Superfamily (MFS) of transporters . Uptake of sn-glycerol 3-phosphate via the GlpT transporter leads to the simultaneous counterflow of inorganic phosphate from the cell . GlpT also catalyzes a reversible phosphate:phosphate exchange . Both sn-glycerol 3-phosphate:phosphate and phosphate:phosphate exchange activities were observed in GlpT-reconstituted proteoliposomes . Using phosphate-loaded proteoliposomes, the Km for the transport of sn-glycerol 3-phosphate via GlpT was estimated to be near 20 μM and the Vmax was 130 nmol min-1 mg-1 . GlpT has been crystallized and the structure has been determined by X-ray crystallography to a resolution of 3.3 Å . The functional form of GlpT is the monomer . GlpT exhibits a rocker-switch mechanism of transport although transport via a 'tilted' mechanism has also been proposed . Experiments using PhoA/LacZ fusions revealed GlpT has twelve transmembrane segments...

## Biological Role

Repressed by glpR (protein.P0ACL0), plaR (protein.P37671). Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08194|protein.P08194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glpT; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `C` - regulator=GlpR; target=glpT; function=-
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB|EcoCyc` `S` - regulator=PlaR; target=glpT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007401,ECOCYC:EG10401,GeneID:946704`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2351016-2352374:-; feature_type=gene
