---
entity_id: "gene.b3193"
entity_type: "gene"
name: "mlaD"
source_database: "NCBI RefSeq"
source_id: "gene-b3193"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3193"
  - "mlaD"
---

# mlaD

`gene.b3193`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3193`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mlaD (gene.b3193) is a gene entity. It encodes mlaD (protein.P64604). Encoded protein function: FUNCTION: Part of the ABC transporter complex MlaFEDB, which is involved in a phospholipid transport pathway that maintains lipid asymmetry in the outer membrane by retrograde trafficking of phospholipids from the outer membrane to the inner membrane (PubMed:19383799, PubMed:27529189). MlaD functions in substrate binding with strong affinity for phospholipids and modulates ATP hydrolytic activity of the complex (PubMed:27529189). {ECO:0000269|PubMed:19383799, ECO:0000269|PubMed:27529189}. EcoCyc product frame: EG12799-MONOMER. EcoCyc synonyms: yrbD. Genomic coordinates: 3337910-3338461. EcoCyc protein note: mlaD encodes an inner membrane anchored subunit of the MlaFEDB transporter complex which functions as part of a retrograde and/or anterograde intermembrane phospholipid trafficking system. MlaD is implicated in a retrograde phospholipid trafficking pathway; a ΔmlaD mutant displays increased SDS-EDTA sensitivity . MlaD is predicted to be a periplasmic facing, inner membrane protein . MlaD is a member of the mammalian cell entry (MCE) family of proteins; MlaD consists of a predicted membrane-anchoring N-terminal α-helix, followed by an MCE domain and a C-terminal α-helical domain, both located in the periplasm...

## Biological Role

Activated by marA (protein.P0ACH5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64604|protein.P64604]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=mlaD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010493,ECOCYC:EG12799,GeneID:947712`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3337910-3338461:-; feature_type=gene
