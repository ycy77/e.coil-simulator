---
entity_id: "gene.b3541"
entity_type: "gene"
name: "dppD"
source_database: "NCBI RefSeq"
source_id: "gene-b3541"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3541"
  - "dppD"
---

# dppD

`gene.b3541`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3541`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dppD (gene.b3541) is a gene entity. It encodes dppD (protein.P0AAG0). Encoded protein function: FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for energy coupling to the transport system (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. EcoCyc product frame: DPPD-MONOMER. Genomic coordinates: 3702865-3703848. EcoCyc protein note: dppD encodes the predicted ATP-binding subunit of a dipeptide ABC transport system; DppD contains conserved ATP binding motifs and an ABC signature motif . DppD contains an FeS-Centers iron-sulfur cluster; purified DppD binds approximately 4 molecules of iron per monomer .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAG0|protein.P0AAG0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dppD; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dppD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppD; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011566,ECOCYC:EG12627,GeneID:948065`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3702865-3703848:-; feature_type=gene
