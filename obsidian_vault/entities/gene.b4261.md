---
entity_id: "gene.b4261"
entity_type: "gene"
name: "lptF"
source_database: "NCBI RefSeq"
source_id: "gene-b4261"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4261"
  - "lptF"
---

# lptF

`gene.b4261`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4261`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptF (gene.b4261) is a gene entity. It encodes lptF (protein.P0AF98). Encoded protein function: FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}. EcoCyc product frame: G7888-MONOMER. EcoCyc synonyms: yjgP. Genomic coordinates: 4486218-4487318. EcoCyc protein note: LptF is an essential inner membrane component of the Lpt lipopolysaccharide (LPS) transport system. LptF contains six predicted transmembrane domains with the C-terminus located in the cytoplasm . lptF is essential . Depletion of LptF (and/or LptG) results in a filamenting phenotype, increased sensitivity to hydrophobic antibiotics and an altered form of LPS; LptFG are required for LPS to reach the outer leaflet of the outer membrane . LptF forms a complex with LptG, LptB and LptC . LptF and LptG each contain a coupling helix which mediates their interaction with LptB; the LptFG coupling helices likely coordinate ATPase activity with LPS extraction from the inner membrane but each appears to have a distinct role (see further ). lptF has been the subject of a pilot study to examine genetic interactions involving essential genes .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF98|protein.P0AF98]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013958,ECOCYC:G7888,GeneID:948795`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4486218-4487318:+; feature_type=gene
