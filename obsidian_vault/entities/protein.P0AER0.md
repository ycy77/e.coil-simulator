---
entity_id: "protein.P0AER0"
entity_type: "protein"
name: "glpF"
source_database: "UniProt"
source_id: "P0AER0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11964478, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11964478}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpF b3927 JW3898"
---

# glpF

`protein.P0AER0`

## Static

- Type: `protein`
- Source: `UniProt:P0AER0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11964478, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11964478}.

## Enriched Summary

FUNCTION: Mediates glycerol diffusion across the cytoplasmic membrane via a pore-type mechanism (PubMed:11039922, PubMed:11226336, PubMed:6998951, PubMed:7512955). Is highly permeable to glycerol, but less well permeated by water (PubMed:11226336). Does not transport ions (PubMed:7512955). It may also have limited permeability to various other substrates, including xylitol, erythritol, D-arabitol, L-arabitol, ribitol, D-galactitol, D-mannitol, D-sorbitol, urea, glycine, D/L-glyceraldehyde and the trivalent inorganic forms of arsenic and antimony (PubMed:14970228, PubMed:6998951, PubMed:9150238). {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11226336, ECO:0000269|PubMed:14970228, ECO:0000269|PubMed:6998951, ECO:0000269|PubMed:7512955, ECO:0000269|PubMed:9150238}. The glycerol facilitator, GlpF, allows the facilitated diffusion of glycerol across the inner membrane for utilization inside the cell. It is a member of the major intrinsic protein (MIP) family of transmembrane channel proteins, along with AqpZ, a water channel. GlpF is predicted to be monomeric . A projection map at a resolution of 3.7 Å reveals GlpF forms a tetramer of four channels . Interactions between purified GlpF show it forms multiple oligomeric complexes . The tetrameric structure has a funnel on its periplasmic surface which help in recruitment of glycerol to the transporter...

## Biological Role

Component of glycerol facilitator (complex.ecocyc.CPLX0-7654).

## Annotation

FUNCTION: Mediates glycerol diffusion across the cytoplasmic membrane via a pore-type mechanism (PubMed:11039922, PubMed:11226336, PubMed:6998951, PubMed:7512955). Is highly permeable to glycerol, but less well permeated by water (PubMed:11226336). Does not transport ions (PubMed:7512955). It may also have limited permeability to various other substrates, including xylitol, erythritol, D-arabitol, L-arabitol, ribitol, D-galactitol, D-mannitol, D-sorbitol, urea, glycine, D/L-glyceraldehyde and the trivalent inorganic forms of arsenic and antimony (PubMed:14970228, PubMed:6998951, PubMed:9150238). {ECO:0000269|PubMed:11039922, ECO:0000269|PubMed:11226336, ECO:0000269|PubMed:14970228, ECO:0000269|PubMed:6998951, ECO:0000269|PubMed:7512955, ECO:0000269|PubMed:9150238}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4 | EcoCyc transporter component coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3927|gene.b3927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AER0`
- `KEGG:ecj:JW3898;eco:b3927;ecoc:C3026_21225;`
- `GeneID:93777971;948422;`
- `GO:GO:0005886; GO:0015168; GO:0015254; GO:0015793; GO:0071288`

## Notes

Glycerol uptake facilitator protein (Aquaglyceroporin) (Glycerol facilitator)
