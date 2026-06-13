---
entity_id: "gene.b2513"
entity_type: "gene"
name: "yfgM"
source_database: "NCBI RefSeq"
source_id: "gene-b2513"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2513"
  - "yfgM"
---

# yfgM

`gene.b2513`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2513`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfgM (gene.b2513) is a gene entity. It encodes yfgM (protein.P76576). Encoded protein function: FUNCTION: May mediate protein transfer from the SecYEG translocon to the periplasmic chaperone network via its periplasmic C-terminal region (PubMed:24855643). In addition, at the cytosolic site, acts as a negative regulator of RcsB (PubMed:26092727). In stationary phase, the FtsH-dependent degradation of YfgM ensures the release of RcsB from YfgM and thereby permits cellular protection by the Rcs phosphorelay system (PubMed:26092727). May coordinate stress responses across the inner membrane via a dynamic protein-protein interaction network inside and outside of the membrane (PubMed:26092727). {ECO:0000269|PubMed:24855643, ECO:0000269|PubMed:26092727}. EcoCyc product frame: G7321-MONOMER. Genomic coordinates: 2638663-2639283. EcoCyc protein note: YfgM interacts with the SecYEG translocon and may function within a β-barrel trafficking chaperone network. Deletion of yfgM further compromises outer membrane integrity in both ΔsurA and Δskp backgrounds . Proteomic analysis of E.coli membrane preparations suggests that YfgM forms a stable complex with the periplasmic chaperone G6242-MONOMER "PpiD". PpiD co-purifies with his-tagged YfgM . YfgM is predicted to contain an N-terminal transmembrane helix and a large periplasmic domain...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76576|protein.P76576]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008274,ECOCYC:G7321,GeneID:946981`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2638663-2639283:-; feature_type=gene
