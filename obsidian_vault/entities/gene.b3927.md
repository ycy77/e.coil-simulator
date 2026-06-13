---
entity_id: "gene.b3927"
entity_type: "gene"
name: "glpF"
source_database: "NCBI RefSeq"
source_id: "gene-b3927"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3927"
  - "glpF"
---

# glpF

`gene.b3927`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3927`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpF (gene.b3927) is a gene entity. It encodes glpF (protein.P0AER0). Encoded protein function: FUNCTION: Mediates glycerol diffusion across the cytoplasmic membrane via a pore-type mechanism (PubMed:11039922, PubMed:11226336, PubMed:6998951, PubMed:7512955). Is highly permeable to glycerol, but less well permeated by water (PubMed:11226336). Does not transport ions (PubMed:7512955). It may also have limited permeability to various other substrates, including xylitol, erythritol, D-arabitol, L-arabitol, ribitol, D-galactitol, D-mannitol, D-sorbitol, urea, glycine, D/L-glyceraldehyde and the trivalent inorganic forms of arsenic and antimony (PubMed:14970228, PubMed:6998951, PubMed:9150238). {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11226336, ECO:0000269|PubMed:14970228, ECO:0000269|PubMed:6998951, ECO:0000269|PubMed:7512955, ECO:0000269|PubMed:9150238}. EcoCyc product frame: GLPF-MONOMER. Genomic coordinates: 4117245-4118090. EcoCyc protein note: The glycerol facilitator, GlpF, allows the facilitated diffusion of glycerol across the inner membrane for utilization inside the cell. It is a member of the major intrinsic protein (MIP) family of transmembrane channel proteins, along with AqpZ, a water channel. GlpF is predicted to be monomeric . A projection map at a resolution of 3.7 Å reveals GlpF forms a tetramer of four channels...

## Biological Role

Repressed by glpR (protein.P0ACL0). Activated by fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AER0|protein.P0AER0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=glpF; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `S` - regulator=GlpR; target=glpF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012828,ECOCYC:EG10396,GeneID:948422`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4117245-4118090:-; feature_type=gene
