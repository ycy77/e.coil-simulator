---
entity_id: "gene.b3195"
entity_type: "gene"
name: "mlaF"
source_database: "NCBI RefSeq"
source_id: "gene-b3195"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3195"
  - "mlaF"
---

# mlaF

`gene.b3195`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3195`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaF (gene.b3195) is a gene entity. It encodes mlaF (protein.P63386). Encoded protein function: FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. EcoCyc product frame: YRBF-MONOMER. EcoCyc synonyms: yrbF. Genomic coordinates: 3339256-3340065. EcoCyc protein note: mlaF encodes the ATP-binding protein of an inner membrane complex (MlaFEDB) which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaF contains signature motifs conserved in ATP-binding cassette (ABC) proteins . MlaF is implicated in a retrograde phospholipid trafficking pathway; a ΔmlaF mutant displays increased SDS-EDTA sensitivity (also ). MlaF forms a stable complex with MlaE, MlaD and MlaB; an MlaFEB complex containing an MlaF variant (MlaFK47R) has no intrinsic ATPase activity in vitro . Purified, recombinant MlaFB (co-expressed from a single transcript) forms a complex with 1:1 stoichiometry and structures of both MlaF1B1 - the inactive 'half-transporter' - and MlaF2B2 - the fully assembled complex - have been solved...

## Biological Role

Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63386|protein.P63386]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=mlaF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010498,ECOCYC:EG12801,GeneID:947729`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3339256-3340065:-; feature_type=gene
