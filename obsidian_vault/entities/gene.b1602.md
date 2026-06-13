---
entity_id: "gene.b1602"
entity_type: "gene"
name: "pntB"
source_database: "NCBI RefSeq"
source_id: "gene-b1602"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1602"
  - "pntB"
---

# pntB

`gene.b1602`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1602`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pntB (gene.b1602) is a gene entity. It encodes pntB (protein.P0AB67). Encoded protein function: FUNCTION: The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane. EcoCyc product frame: PNTB-MONOMER. Genomic coordinates: 1674972-1676360. EcoCyc protein note: pntB encodes the β subunit of membrane-bound proton-translocating pyridine nucleotide transhydrogenase. The β subunit contains an N-terminal domain with 6 - 8 transmembrane regions and a cytosolic C-terminal domain that binds NADP(H) . Early studies characterized the pnt-1 mutation (PntB G314E ) which causes loss of both energy-dependent and energy-independent pyridine nucleotide transhydrogenase activity .

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB67|protein.P0AB67]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=pntB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005352,ECOCYC:EG10745,GeneID:946144`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1674972-1676360:-; feature_type=gene
