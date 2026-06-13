---
entity_id: "gene.b3542"
entity_type: "gene"
name: "dppC"
source_database: "NCBI RefSeq"
source_id: "gene-b3542"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3542"
  - "dppC"
---

# dppC

`gene.b3542`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3542`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dppC (gene.b3542) is a gene entity. It encodes dppC (protein.P0AEG1). Encoded protein function: FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. EcoCyc product frame: DPPC-MONOMER. Genomic coordinates: 3703859-3704761. EcoCyc protein note: dppB encodes the predicted inner membrane subunit of a dipeptide ABC transport system .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEG1|protein.P0AEG1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dppC; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dppC; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppC; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011570,ECOCYC:EG12626,GeneID:948064`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3703859-3704761:-; feature_type=gene
