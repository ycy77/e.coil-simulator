---
entity_id: "gene.b3414"
entity_type: "gene"
name: "nfuA"
source_database: "NCBI RefSeq"
source_id: "gene-b3414"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3414"
  - "nfuA"
---

# nfuA

`gene.b3414`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3414`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfuA (gene.b3414) is a gene entity. It encodes nfuA (protein.P63020). Encoded protein function: FUNCTION: Involved in iron-sulfur cluster biogenesis under severe conditions such as iron starvation or oxidative stress. Binds a 4Fe-4S cluster, can transfer this cluster to apoproteins, and thereby intervenes in the maturation of Fe/S proteins. Could also act as a scaffold/chaperone for damaged Fe/S proteins. Required for E.coli to sustain oxidative stress and iron starvation. Also necessary for the use of extracellular DNA as the sole source of carbon and energy. {ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:18339628}. EcoCyc product frame: G7748-MONOMER. EcoCyc synonyms: yhgI, gntY. Genomic coordinates: 3545624-3546199. EcoCyc protein note: NfuA is a 'non-ISC, non-SUF' iron-sulfur (Fe-S) cluster carrier protein. NfuA can receive Fe-S clusters from the SufBC2D and IscU/HscBA scaffold-containing complexes and can in turn transfer Fe-S clusters to the A-type carrier proteins EG11378-MONOMER SufA and EG12132-MONOMER IscA . NfuA is able to transfer its iron-sulfur cluster to ACONITASE-MONOMER apo-AcnA and ACONITATEDEHYDRB-MONOMER apo-AcnB and appears to be involved in the maturation of EG12087 NuoG, an iron-sulfur cluster-containing subunit of NADH dehydrogenase I . Both NfuA and EG12181-MONOMER "GrxD" interact with G6364-MONOMER "MiaB"...

## Biological Role

Repressed by iscR (protein.P0AGK8). Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63020|protein.P63020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=nfuA; function=+
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=nfuA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011144,ECOCYC:G7748,GeneID:947925`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3545624-3546199:+; feature_type=gene
