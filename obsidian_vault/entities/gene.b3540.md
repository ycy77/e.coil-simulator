---
entity_id: "gene.b3540"
entity_type: "gene"
name: "dppF"
source_database: "NCBI RefSeq"
source_id: "gene-b3540"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3540"
  - "dppF"
---

# dppF

`gene.b3540`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3540`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dppF (gene.b3540) is a gene entity. It encodes dppF (protein.P37313). Encoded protein function: FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. EcoCyc product frame: DPPF-MONOMER. EcoCyc synonyms: dppE. Genomic coordinates: 3701864-3702868. EcoCyc protein note: dppF encodes the predicted ATP-binding subunit of a dipeptide ABC transport system; DppF contains conserved ATP binding motifs .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37313|protein.P37313]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dppF; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dppF; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppF; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppF; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011564,ECOCYC:EG12628,GeneID:948056`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3701864-3702868:-; feature_type=gene
